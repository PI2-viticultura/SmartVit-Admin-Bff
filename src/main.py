from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
import asyncio

from settings import load_configuration
from views import (
    contract_view,
    order_view,
    sensor_view,
    system_view,
    user_view,
    winery_view
)

app = FastAPI()

origins = [
    'http://localhost',
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contract_view.router)
app.include_router(order_view.router)
app.include_router(sensor_view.router)
app.include_router(system_view.router)
app.include_router(user_view.router)
app.include_router(winery_view.router)

if __name__ == "__main__":
    server_config = load_configuration()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(uvicorn.run('main:app', **server_config))
