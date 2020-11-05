import aiohttp
import json
import os

urlEnv = os.getenv(
    'URLENVSENSOR',
    'https://smartvit-winery-dev.herokuapp.com/sensor'
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


async def post_sensor(sensor):
    response = dict()
    status = 404

    async with aiohttp.ClientSession() as session:
        response, status = await fetch(
            session,
            urlEnv,
            sensor
        )

    return json.loads(response), status
