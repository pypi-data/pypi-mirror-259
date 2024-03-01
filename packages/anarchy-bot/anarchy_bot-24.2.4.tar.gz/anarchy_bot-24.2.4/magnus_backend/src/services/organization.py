from dadata import Dadata
from fastapi import HTTPException


# put in config in future (10.000 per/day)
token = '6a674af158a3ee27946c293b1047288dabefdbc5'
dadata = Dadata(token)


def post_website_request(inn_or_ogrn: str) -> dict | None:
    response = dadata.suggest('party', query=inn_or_ogrn, count=1)
    if response:
        return response[0]


def get_organization(inn_or_ogrn: str) -> dict:
    response = post_website_request(inn_or_ogrn)
    if response is None:
        raise HTTPException(status_code=200, detail='organization not found')
    result = dict()
    data = response.get('data', None)
    if data is not None:
        result['name'] = response.get('value', '')
        result['inn'] = data.get('inn', '')
        result['ogrn'] = data.get('ogrn', '')
        address = data.get('address')
        result['legal_address'] = address.get('unrestricted_value') if address else ''
        try:
            phones = data.get('phones')[0]
            result['phone_number'] = phones.get('value', '')
        except:
            result['phone_number'] = ''
        try:
            management = data.get('management')
            fio = management.get('name', '').split()
            result['firstname'] = fio[0]
            result['lastname'] = fio[1]
        except:
            result['firstname'] = ''
            result['lastname'] = ''
    return result


# if __name__ == '__main__':
#     get_organization('165506asd324960')
