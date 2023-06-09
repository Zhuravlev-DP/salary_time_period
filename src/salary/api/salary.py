from typing import List

from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)

from .. import models
from ..services.auth import get_current_user
from ..services.salary import SalaryService


router = APIRouter(
    prefix='/salary',
    tags=['salary'],
)


@router.get(
    '/',
    response_model=models.Salary,
)
def get_operations(
    user: models.User = Depends(get_current_user),
    operations_service: SalaryService = Depends(),
):
    return operations_service.get(user.id)
