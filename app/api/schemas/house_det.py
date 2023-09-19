from typing import Optional, List,Dict, Union
from pydantic import BaseModel, StrictStr, StrictBool
from datetime import date

class ImagesInputSinglePath(BaseModel):
    tensor: StrictStr

class ImagesInputSingleb64(BaseModel):
    b64str: StrictStr
    b64return: StrictBool