from fastapi import FastAPI, APIRouter,Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import io
from typing import Optional, List, Dict
from pydantic import BaseModel, StrictStr
import json
import uvicorn

import api.routers.face_det as face_det_routers
import api.routers.house_det as house_det_routers

    
router = APIRouter()
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


app.include_router(face_det_routers.router, prefix="/api/v1/model/face")
app.include_router(house_det_routers.router, prefix="/api/v1/model/house")



if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=9000)

