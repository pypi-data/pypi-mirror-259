import ast
import asyncio
import urllib.request

import httpx
from tortoise import Tortoise, run_async

from models.delivery import DelLinCity, DelLinRegion
import tempfile

client = httpx.Client()


async def insert(values):
    for city_id, city_name, reg_name, reg_code, *args in values:
        await DelLinRegion.get_or_create(title=reg_name, identifier=reg_code)
        await DelLinCity.get_or_create(
            title=city_name, identifier=city_id, region_id=reg_code
        )


async def csv_reader(url):
    temp_file = tempfile.TemporaryFile()

    data = urllib.request.urlopen(url)

    temp_file.write(data.read())
    temp_file.seek(0)

    c = 0

    values = []

    for line in temp_file.readlines():
        c += 1
        decoded_string = line.decode("utf-8")



        (
            city_id,
            full_name,
            code,
            city_name,
            reg_name,
            reg_code,
            *arg,
        ) = ast.literal_eval(decoded_string)

        if city_id == "cityID":
            continue

        values.append((city_id, city_name, reg_name, reg_code))

    tasks = []

    chunk_size = 1000


    for part in [values[i:i + chunk_size] for i in range(0, len(values), chunk_size)]:
        tasks.append(asyncio.create_task(insert(part)))

    await asyncio.gather(*tasks)

async def del_lin_parser_places(appkey):
    await Tortoise.init(
        db_url="sqlite://db.sqlite3", modules={"models": ["models.delivery"]}
    )
    # Generate the schema
    await Tortoise.generate_schemas()
    url = "https://api.dellin.ru/v1/public/places.json"

    r = client.post(
        url,
        json={
            "appkey": appkey,
        },
    )

    await csv_reader(r.json().get("url"))


asyncio.run(del_lin_parser_places("D344D517-A656-447E-95EE-49523A1343E5"))
