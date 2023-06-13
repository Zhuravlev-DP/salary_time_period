from fastapi import APIRouter

from . import auth, salary


router = APIRouter()
router.include_router(auth.router)
router.include_router(salary.router)
