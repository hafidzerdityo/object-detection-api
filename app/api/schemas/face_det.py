from typing import Optional, List,Dict, Union
from pydantic import BaseModel, StrictStr, StrictBool
from datetime import date

class ImagesInputSinglePathFace(BaseModel):
    tensor: StrictStr

class ImagesInputSingleb64Face(BaseModel):
    b64str: StrictStr
    b64return: StrictBool
class FaceSimReq(BaseModel):
    img_b64str1: StrictStr
    img_b64str2: StrictStr