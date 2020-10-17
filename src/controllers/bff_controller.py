import aiohttp


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


async def post_bff(item):
    response = dict()
    status = 404

    async with aiohttp.ClientSession() as session:
        response, status = await fetch(
            session,
            'http://localhost:8000/bff',
            item
        )

    return response, status
