from fastapi import (
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session


class SalaryService:
    """Получение данных о зарплате пользователя."""
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get(self, user_id: int) -> tables.Salary:
        salary = (
            self.session
            .query(tables.Salary)
            .filter(tables.Salary.user_id == user_id).first()
        )
        if not salary:
            raise HTTPException(
                status_code=404,
                detail='Данные о зарплате отсутствуют'
            )
        return salary
