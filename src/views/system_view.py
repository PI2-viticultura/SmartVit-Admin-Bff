from fastapi import APIRouter, Response
from controllers import system_controller
from utils.formatters import create_response
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    title: str


@router.post('/bff/')
async def feedback(response: Response, item: Item):
    result, status = await system_controller.post_bff(item.dict())
    return create_response(result, status, response)
