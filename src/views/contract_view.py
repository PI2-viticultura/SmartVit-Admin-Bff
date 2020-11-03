from fastapi import APIRouter, Response
from controllers import contract_controller
from utils.formatters import create_response
from pydantic import BaseModel
from typing import Any

router = APIRouter()


class Contract(BaseModel):
    contractor: Any
    cpf_cnpj: str
    address: str
    phoneNumber: str
    status: str
    initialDate: str
    endDate: str
    winery: Any


@router.post('/contracts/')
async def contrats(response: Response, contract: Contract):
    result, status = await contract_controller.post_contract(contract.dict())
    return create_response(result, status, response)
