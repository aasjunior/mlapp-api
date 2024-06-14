from pydantic import BaseModel, Field
from typing import Set
import json

class DataScheme(BaseModel):
    attributeHeaders: Set[str]
    classHeader: str

    @classmethod
    def from_string(cls, data_string: str):
        data_dict = json.loads(data_string)
        return cls(**data_dict)
