import re
from typing import Any, Dict, List

from fastapi import HTTPException, Query
from pydantic import BaseModel
from tortoise.expressions import Q
from tortoise.models import Model

DEFAULT_LIMIT = 25
DEFAULT_OFFSET = 0

WRONG_OPERAND = 'Invalid operand {}. Only possible: {}'
WRONG_SORT_OPERAND = 'Invalid sort operand. Only possible: {}'
ERROR_FROM_SERVER = 'Incorrect answer: {}'


class PaginationRequest:
    '''
    Model for queries with pagination and filters

    :param limit: number of records
    :param offset: start with entry no.
    :param field: filtering, specify the field name(s - via ,)
    :param value: filtering, specify value(s - via ,)
    :param op: filtering, specify operation(via , ('=', '!=', '>', '<'))
    :param sort_by: field to sort by: ?sort_by=id (name field)
    :param sort_order: sorting direction ?sort_order=asc (asc desc)
    :param gate: AND or OR: ?gate=and (and or)
    '''

    _OPERANDS = {
        '=': 'Equals',
        '>': 'More',
        '>=': 'More or Equals',
        '<': 'Less',
        '<=': 'Less or Equals',
        'in': 'Matches the value in the list',
        'between': 'Within range',
        'contain': 'Contains value',
        'icontain': 'Contains a case-insensitive value',
        'like': 'Matches',
        'ilike': 'Matches case insensitive',
        'startswith': 'Starts with',
        'istartswith': 'Starts with case insensitive',
        '!=': 'Not equal',
        'not in': 'Does not match the value in the list',
        'not between': 'Out of range',
        'not contain': 'Does not contain a value',
        'not like': 'Does not match',
    }

    _OPERANDS_SORT = {
        'asc': 'Ascending',
        'desc': 'Descending',
    }

    _OPERANDS_GATE = {
        'and': 'And',
        'or': 'Or',
    }

    def __init__(
        self,
        limit: int = DEFAULT_LIMIT,
        offset: int = DEFAULT_OFFSET,
        field: List[str] = Query(default=[]),
        value: List[str] = Query(default=[]),
        op: List[str] = Query(default=['=']),
        sort_by: List[str] = Query(default=[]),
        sort_order: List[str] = Query(default=['desc']),
        gate: str = 'and',
    ):
        self.limit = limit
        self.offset = offset
        self.field = self.validate_field(field)
        self.value = self.validate_value(value)
        self.op = self.validate_op(op)
        self.sort_by = sort_by
        self.sort_order = self.validate_sort_order(sort_order)
        self.gate = self.validate_gate(gate)

    @staticmethod
    def validate_value(v):
        if len(v) == 0:
            return []
        return list(v)

    @staticmethod
    def validate_field(v):
        if len(v) == 0:
            return []
        return list(v)

    def validate_op(self, v):
        if len(v) == 0:
            return []

        for op in v:
            op = op.lower()
            temp_v = op.lstrip('!')
            temp_v = temp_v.lstrip('not ')
            if temp_v not in self._OPERANDS.keys():
                raise HTTPException(
                    status_code=400,
                    detail=WRONG_OPERAND.format('op', self._OPERANDS.keys()),
                )
        return list(v)

    def validate_sort_order(self, v):
        for op in v:
            if op not in self._OPERANDS_SORT.keys():
                raise HTTPException(
                    status_code=400,
                    detail=WRONG_OPERAND.format(
                        'sort_order', self._OPERANDS_SORT.keys()
                    ),
                )
        return list(v)

    def validate_gate(self, v):
        if v not in self._OPERANDS_GATE.keys():
            raise HTTPException(
                status_code=400,
                detail=WRONG_OPERAND.format('gate', self._OPERANDS_GATE.keys()),
            )
        return v

    @classmethod
    def docs_operands(cls):
        result = dict()
        result.update(cls._OPERANDS)
        result.update(cls._OPERANDS_SORT)
        result.update(cls._OPERANDS_GATE)
        return result


def get_filters_for_list_values(args: Dict) -> List:
    filters = []
    field: List[str] = args.get('field', [])
    value: List[str] = args.get('value', [])
    op: List[str] = args.get('op', [])
    if field is not None and op is not None and value is not None:
        for i, name in enumerate(field):
            filters.append({'field': name, 'value': value[i], 'op': op[i]})
    return filters


def generate_filter(field: str, value: str, op: str) -> dict:

    op = op or '='
    simple_ops = {
        '=': '',
        '>': '__gt',
        '>=': '__gte',
        '<': '__lt',
        '<=': '__lte',
        'in': '__in',
        'between': '__range',
        'icontain': '__icontains',
        'contain': '__contains',
        'ilike': '__icontains',
        'like': '__contains',
        'istartswith': '__istartswith',
        'startswith': '__startswith',
    }
    try:
        op_position = simple_ops[op.lower()]
    except IndexError:
        raise UserWarning('Bad operation: %s', op)
    return {f'{field}{op_position}': value}


def make_sort_list(pagination: PaginationRequest) -> List:
    sort_list: List = []
    for i, sort in enumerate(pagination.sort_by):
        if pagination.sort_order[i] == 'desc':
            sort_list.append(f'-{sort}')
        else:
            sort_list.append(f'{sort}')
    return sort_list


async def filter_query_builder(
    model: Model,
    pagination: PaginationRequest,
):
    _filter = {}
    _exclude = {}

    filters = get_filters_for_list_values(
        {
            'field': pagination.field,
            'value': pagination.value,
            'op': pagination.op,
            'gate': pagination.gate,
        }
    )

    for w in filters:
        if re.search(r'\!|not', w['op']):
            _operand = w['op'].lstrip('!')
            _operand = _operand.lstrip('not ')
            _exclude.update(generate_filter(w['field'], w['value'], _operand))
        else:
            _filter.update(generate_filter(w['field'], w['value'], w['op']))

    for f in _filter.keys():
        if len(f) > 3 and f[-3:] == '_in':
            l = _filter.get(f, '').split(',')
            _filter[f] = l

    count: int = 0
    if pagination.gate == 'or':
        query = Q(*[Q(**{k: v}) for k, v in _filter.items()], join_type='OR')
        query_set = (
            await model.filter(query)
            .offset(pagination.offset)
            .limit(pagination.limit)
            .exclude(**_exclude)
            .order_by(*make_sort_list(pagination))
            .distinct()
        )
        count = await model.filter(query).exclude(**_exclude).distinct().count()
    else:
        query_set = (
            await model.filter(**_filter)
            .offset(pagination.offset)
            .limit(pagination.limit)
            .exclude(**_exclude)
            .order_by(*make_sort_list(pagination))
            .distinct()
        )
        count = await model.filter(**_filter).exclude(**_exclude).distinct().count()

    return dict(items=query_set, count=count)


class BaseDataModel(BaseModel):
    id: int


class BaseDao:
    def __init__(self, model):
        self._model = model

    async def check_exist_object(self, obj_id) -> bool:
        obj = await self._model.filter(id=obj_id).first()
        return False if obj is None else True

    async def create(self, model):
        obj = await self._model.create(**model.model_dump())
        return obj

    async def get(self, obj_id: int):
        obj = await self._model.get_or_none(id=obj_id)
        return obj

    async def list(self, params) -> Dict:
        r = await filter_query_builder(self._model, params)
        return {'items': r.get('items'), 'count': r.get('count')}

    async def delete(self, obj_id: int) -> bool:
        obj = await self.get(obj_id)
        if obj is None:
            return False
        else:
            await obj.delete()
            return True

    async def update(self, data: Any) -> bool:
        obj = await self.get(data.id)
        if obj is None:
            return False
        await obj.update_from_dict(data.model_dump()).save()
        return True
