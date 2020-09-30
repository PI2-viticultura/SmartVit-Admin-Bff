from fastapi import APIRouter, Response, Request
from controllers import bff_controller
from utils.formatters import create_response
from pydantic import BaseModel
from typing import Optional

router = APIRouter()


class Item(BaseModel):
    title: str


@router.post('/bff/')
async def feedback(response: Response, item: Item):
    result, status = await bff_controller.post_bff(item.dict())
    return create_response(result, status, response)
