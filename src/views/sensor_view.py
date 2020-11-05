from fastapi import APIRouter, Response
from controllers import sensor_controller
from utils.formatters import create_response
from pydantic import BaseModel
from typing import Optional

router = APIRouter()


class Sensor(BaseModel):
    location: str
    identifier: str
    type: str
    situation: str
    last_register: Optional[str] = None
    system_id: str


@router.post('/sensor/')
async def sensor(response: Response, sensor: Sensor):
    result, status = await sensor_controller.post_sensor(sensor.dict())
    return create_response(result, status, response)
