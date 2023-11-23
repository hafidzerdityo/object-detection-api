from fastapi import APIRouter, HTTPException, status, Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer

import api.schemas.face_det as face_det_schema
import services.face_det as face_det_model
from log import logger

router = APIRouter()

@router.post('/face_det', tags=["Main"])
async def face_detection_single_path(request: face_det_schema.ImagesInputSinglePath):
    try:
        predict = face_det_model.predict_face(request.tensor)
        return {
            'resp_data': predict,
            'resp_msg': 'success predict face'
        }
    except Exception as e:
        logger.error(str(e)) 
        return JSONResponse(
            status_code=400,
            content={
                  "resp_data": None,
                  "resp_msg": str(e),},
        )

@router.post('/face_det_b64',tags=["Main"])
async def face_detection_single_b64(request: face_det_schema.ImagesInputSingleb64):
    predict = face_det_model.predict_face_b64(request.b64str, request.b64return)
    if 'error' in predict.keys():
        logger.error(predict.get('error',None)) 
        return JSONResponse(
            status_code=400,
            content={"resp_msg":predict.get('error',None),
                     "resp_data": None},
        )
    return {
        'resp_data': predict,
        'resp_msg': 'success predict face'
        }
