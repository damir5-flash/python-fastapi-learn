from fastapi import APIRouter

import core.config
from .users import router as users_router

router = APIRouter(
    prefix=core.config.settings.api.v1.prefix,
)
router.include_router(users_router)