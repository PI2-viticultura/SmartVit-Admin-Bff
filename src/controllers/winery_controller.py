import aiohttp
import json
import os

urlEnv = os.getenv(
    'URLENVUSER',
    'https://smartvit-winery-dev.herokuapp.com/winery'
)


async def fetch(session, url, data=None):
    header = {
        'Accept': 'application/json'
    }
    async with session.post(
        url,
        json=data,
        headers=header
    ) as response:
        return await response.text(), response.status


async def retrieve(session, url, data=None):
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
        headers=header
    ) as response:
        return await response.text(), response.status


async def post_winery(winery):
    response = dict()
    status = 404

    async with aiohttp.ClientSession() as session:
        response, status = await fetch(
            session,
            urlEnv,
            winery
        )

    return json.loads(response), status


async def get_winery():
    response = dict()
    status = 404

    async with aiohttp.ClientSession() as session:
        response, status = await retrieve(
            session,
            urlEnv
        )

    return json.loads(response), status


async def patch_winery(winery_id):
    response = dict()
    status = 404

    async with aiohttp.ClientSession() as session:
        response, status = await patch(
            session,
            urlEnv + '/' + winery_id
        )

    return json.loads(response), status
