from fastapi import APIRouter, Response
from controllers import user_controller
from utils.formatters import create_response
from pydantic import BaseModel

router = APIRouter()


class User(BaseModel):
    name: str
    cpf: str
    email: str
    password: str
    type: str
    situation: str


@router.post('/user/')
async def user(response: Response, user: User):
    result, status = await user_controller.post_user(user.dict())
    return create_response(result, status, response)


@router.get('/user/')
async def user(response: Response):
    result, status = await user_controller.get_user()
    return create_response(result, status, response)


@router.put('/user/{user_id}')
async def user(response: Response, user_id: str, user: User):
    result, status = await user_controller.update_user(user_id, user.dict())
    return create_response(result, status, response)
