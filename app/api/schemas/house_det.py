from typing import Optional, List,Dict, Union
from pydantic import BaseModel, StrictStr, StrictBool
from datetime import date

class ImagesInputSinglePathHouse(BaseModel):
    tensor: StrictStr

class ImagesInputSingleb64House(BaseModel):
    b64str: StrictStr
    b64return: StrictBool