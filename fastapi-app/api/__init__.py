from fastapi import APIRouter

import core.config
from .api_v1 import router as router_api_v1

router = APIRouter(
    prefix=core.config.settings.api.v1.prefix,
)
router.include_router(router_api_v1)

