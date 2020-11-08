from fastapi import APIRouter, Response
from controllers import login_controller
from utils.formatters import create_response
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    email: str
    password: str
    role: str


@router.post('/login/')
async def login(response: Response, user: User):
    result, status = await login_controller.post_login(user.dict())
    return create_response(result, status, response)
