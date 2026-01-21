from datetime import datetime

from pydantic import BaseModel


class DataUpdate(BaseModel):
    value: float
    timestamp: datetime
