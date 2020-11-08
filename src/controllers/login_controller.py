import aiohttp
import json
import os

urlEnv = os.getenv(
    'URLENVLOGIN',
    'https://smartvit-user-dev.herokuapp.com/login'
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
        return await response.json(), response.status

async def post_login(user):
    response = dict()
    status = 404

    async with aiohttp.ClientSession() as session:
        response, status = await fetch(
            session,
            urlEnv,
            user
        )

    return response, status
