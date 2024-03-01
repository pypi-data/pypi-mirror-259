from contextlib import asynccontextmanager
from tortoise import Tortoise
from tortoise.exceptions import ConfigurationError
import core.config as config
import asyncio
import signal
import redis
import os

from models.users import User, Device, ConfirmationCode
from models.organizations import Organization, Employee, OnBoardEmployee, DeliveryService
from models.products import (Category, Product, MinimumQuantity, MinimumQuantityToProduct, OfferCategory,
                             SelectedCategory)
from models.orders import Order, OrderItem
from models.payments import PaymentMethod, PaymentLog
from models.prices import PriceItemStructure
from models.notifications import Notification
from models.requisites import Props
from models.warehouses import Warehouse, PointDeliveryCompany
from models.basket import ProductInBasket
from models.delivery import DeliveryCompany, DelLinRegion, DelLinCity
from scheduler import scheduler


def shutdown(signal, frame):
    os._exit(0)


async def init():
    signal.signal(signal.SIGINT, shutdown)
    scheduler.start()
    db_url = config.config.db_url
    try:
        await Tortoise.init(
            db_url=db_url,
            modules={"models": ["db"]},
        )
    except ConfigurationError:
        print(f'invalid database url {db_url}, please change it')
        os._exit(0)
    max_attempts = 60
    attempt = 0
    while attempt < max_attempts:
        try:
            await Tortoise.generate_schemas()
            print('sucessfully connected to database')
            return
        except OSError:
            attempt += 1
            print(
                f'waiting for postgresql to be ready, attempt {attempt}/{max_attempts}'
            )
            await asyncio.sleep(1)
    raise TimeoutError('failed to start postgresql')


@asynccontextmanager
async def app_lifespan(_):
    await init()
    yield
    os._exit(0)


if os.environ.get('AUTOTEST'):
    import fakeredis
    fakedb = fakeredis.FakeRedis(decode_responses=True)


async def create_redis_connection():
    if os.environ.get('DOCKER_ENV'):
        connection = redis.StrictRedis(host='refresh_token', port=6379, db=0, decode_responses=True)
    elif os.environ.get('AUTOTEST') and fakedb is not None:
        return fakedb
    else:
        connection = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
    return connection

