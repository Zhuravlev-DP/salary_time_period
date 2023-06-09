from typing import (
    List,
    Optional,
)

from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from .. import (
    models,
    tables,
)
from ..database import get_session


class SalaryService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get(self, user_id: int) -> tables.Salary:
        salary = (
            self.session
            .query(tables.Salary)
            .filter(tables.Salary.user_id == user_id).first()
        )
        print(salary)
        return salary
