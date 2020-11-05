import aiohttp
import json
import os

urlEnv = os.getenv(
    'URLENVCONTRACT',
    'https://smartvit-admin-dev.herokuapp.com/contracts'
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


async def post_contract(contract):
    response = dict()
    status = 404

    async with aiohttp.ClientSession() as session:
        response, status = await fetch(
            session,
            urlEnv,
            contract
        )

    return json.loads(response), status
