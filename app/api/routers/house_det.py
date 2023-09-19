from fastapi import APIRouter, HTTPException, status, Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer

import api.schemas.house_det as house_det_schema
import services.house_det as house_det_model
from log.log import logger

router = APIRouter()

@router.post('/house_det', tags=["Main"])
async def house_detection_single_path(request: house_det_schema.ImagesInputSinglePath):
    try:
        predict = house_det_model.predict_house(request.tensor)
        return {
            'resp_data': predict,
            'resp_msg': 'success predict house'
        }
    except Exception as e:
        logger.error(str(e)) 
        return JSONResponse(
            status_code=400,
            content={
                  "resp_data": None,
                  "resp_msg": str(e),},
        )

@router.post('/house_det_b64',tags=["Main"])
async def house_detection_single_b64(request: house_det_schema.ImagesInputSingleb64):
    predict = house_det_model.predict_house_b64(request.b64str, request.b64return)
    if 'error' in predict.keys():
        logger.error(predict.get('error',None)) 
        return JSONResponse(
            status_code=400,
            content={"resp_msg":predict.get('error',None),
                     "resp_data": None},
        )
    return {
        'resp_data': predict,
        'resp_msg': 'success predict house'
        }

