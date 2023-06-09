from datetime import date
from typing import Optional

from pydantic import BaseModel


class Salary(BaseModel):
    id: Optional[int]
    user_id: Optional[int]
    salary: Optional[int]
    date_next_promotion: Optional[date]

    class Config:
        orm_mode = True
