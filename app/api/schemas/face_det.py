from typing import Optional, List,Dict, Union
from pydantic import BaseModel, StrictStr, StrictBool
from datetime import date

class ImagesInputSinglePathFace(BaseModel):
    tensor: StrictStr

class ImagesInputSingleb64Face(BaseModel):
    b64str: StrictStr
    b64return: StrictBool