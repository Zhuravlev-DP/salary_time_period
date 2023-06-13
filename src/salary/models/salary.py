from datetime import date
from typing import Optional

from pydantic import BaseModel


class Salary(BaseModel):
    salary: Optional[int] = None
    date_next_promotion: Optional[date]

    class Config:
        orm_mode = True
