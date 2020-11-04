import aiohttp
import json
import os

urlEnv = os.getenv(
    'URLENVORDER',
    'https://smartvit-admin-dev.herokuapp.com/'
)


async def retrieve(session, url):
    header = {
        'Accept': 'application/json'
    }
    async with session.get(
        url,
        headers=header
    ) as response:
        return await response.text(), response.status


async def patch(session, url, data=None):
    header = {
        'Accept': 'application/json'
    }
    async with session.patch(
        url,
        json=data,
        headers=header
    ) as response:
        return await response.text(), response.status


async def get_orders():
    response = dict()
    status = 404

    async with aiohttp.ClientSession() as session:
        response, status = await retrieve(
            session,
            urlEnv + 'orders',
        )

    return json.loads(response), status


async def patch_orders(order_id):
    response = dict()
    status = 404

    async with aiohttp.ClientSession() as session:
        response, status = await patch(
            session,
            urlEnv + 'orders/' + order_id,
        )

    return json.loads(response), status
