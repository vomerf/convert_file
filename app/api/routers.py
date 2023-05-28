from fastapi import APIRouter

from app.api.endpoints import (download_file_router, load_file_router,
                               user_router)

main_router = APIRouter()

main_router.include_router(
    download_file_router, tags=["Download file"],
)
main_router.include_router(
    user_router, tags=["Create user"],
)
main_router.include_router(
    load_file_router, tags=["Load file"],
)
