from pydantic import BaseModel
from typing import Set

class DataScheme(BaseModel):
    src: str
    attributeHeaders: Set[str]
    classHeader: str