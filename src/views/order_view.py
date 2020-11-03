from fastapi import APIRouter, Response
from controllers import order_controller
from utils.formatters import create_response
from pydantic import BaseModel

router = APIRouter()


@router.get('/orders/')
async def order(response: Response):
    result, status = await order_controller.get_orders()
    return create_response(result, status, response)


@router.patch('/orders/{order_id}')
async def order_update(response: Response, order_id: str):
    result, status = await order_controller.patch_orders(order_id)
    return create_response(result, status, response)
