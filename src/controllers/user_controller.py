import aiohttp
import json
import os

urlEnv = os.getenv(
    'URLENVUSER',
    'https://smartvit-user-dev.herokuapp.com/user'
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


async def put(session, url, data=None):
    header = {
        'Accept': 'application/json'
    }
    async with session.put(
        url,
        json=data,
        headers=header
    ) as response:
        return await response.text(), response.status


async def post_user(user):
    response = dict()
    status = 404

    async with aiohttp.ClientSession() as session:
        response, status = await fetch(
            session,
            urlEnv,
            user
        )

    return json.loads(response), status


async def get_user():
    response = dict()
    status = 404

    async with aiohttp.ClientSession() as session:
        response, status = await retrieve(
            session,
            urlEnv
        )

    return json.loads(response), status


async def update_user(user_id, user):
    response = dict()
    status = 404

    async with aiohttp.ClientSession() as session:
        response, status = await put(
            session,
            urlEnv + '/' + user_id,
            user
        )

    return json.loads(response), status
