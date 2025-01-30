from fastapi import FastAPI, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import uvicorn

import api.routers.face_det as face_det_routers
import api.routers.house_det as house_det_routers
from log import logger
    
app = FastAPI(title="Object Detection Model YOLOV8",
    description="author: Hafidz Erdityo",
    version="0.0.1",
    terms_of_service=None,
    contact=None,
    license_info=None)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    details = exc.errors()
    error_list = []
    for error in details:
        error_list.append(
            {
                "loc": error["loc"],
                "message": error["msg"],
                "type": error["type"],
            }
        )
    modified_response = {
        "resp_data": None,
        "resp_msg": error_list
    }
    logger.error(error_list) 
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(modified_response),
    )



app.include_router(face_det_routers.router, prefix="/api/v1/model/face")
app.include_router(house_det_routers.router, prefix="/api/v1/model/house")



# if __name__ == "__main__":
#     uvicorn.run('main:app', host="0.0.0.0", port=9000)

