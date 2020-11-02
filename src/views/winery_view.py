from fastapi import APIRouter, Response
from controllers import winery_controller
from utils.formatters import create_response
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    title: str


@router.post('/bff/')
async def feedback(response: Response, item: Item):
    result, status = await winery_controller.post_bff(item.dict())
    return create_response(result, status, response)
