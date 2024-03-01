from db import app_lifespan
from core.config import config
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from cabinet import admin, user, delivery, requisites, employees, warehouses, categories, basket, organizations
import uvicorn
import common
import auth
import os


routes = (
    ('cabinet', admin),
    ('cabinet', user),
    ('cabinet', delivery),
    ('requisites', requisites),
    ('employees', employees),
    ('warehouses', warehouses),
    ('categories', categories),
    ('basket', basket),
    ('organization', organizations)
)
route_version = None
app = FastAPI(lifespan=app_lifespan)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
router_default = APIRouter()


def make_router_version(route_version, routes):
    router = APIRouter(prefix=f'/{route_version}')
    for prefix, route in routes:
        router.include_router(
            route.router,
            prefix=f'/{prefix}',
            tags=[f'{prefix}'],
        )
    return router


if route_version is not None:
    router = make_router_version(route_version, routes)
    app.include_router(router, prefix='/api')

for prefix, route in routes:
    router_default.include_router(
        route.router,
        prefix=f'/{prefix}',
        tags=[f'{prefix}'],
    )


app.include_router(router_default, prefix='/api')


if __name__ == '__main__':
    print(config.system_info)
    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=8000,
        reload=config.reload,  # run code with --reload to enable
        workers=1,
    )
    os._exit(0)

