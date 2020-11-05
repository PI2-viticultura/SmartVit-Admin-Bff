from fastapi import APIRouter, Response
from controllers import winery_controller
from utils.formatters import create_response
from pydantic import BaseModel

router = APIRouter()


class Winery(BaseModel):
    name: str
    address: str
    contract_id: str


@router.post('/winery/')
async def winery(response: Response, winery: Winery):
    result, status = await winery_controller.post_winery(winery.dict())
    return create_response(result, status, response)


@router.get('/winery/')
async def winery_get(response: Response):
    result, status = await winery_controller.get_winery()
    return create_response(result, status, response)


@router.patch('/winery/{winery_id}')
async def winery_patch(response: Response, winery_id: str):
    result, status = await winery_controller.patch_winery(winery_id)
    return create_response(result, status, response)
