"""GymApp application entry point."""
from fastapi import FastAPI


def create_application() -> FastAPI:
    """Create and configure the FastAPI application instance."""
    application = FastAPI(title="GymApp API", version="0.1.0")
    from app.api.v1.api import api_router

    application.include_router(api_router, prefix="/api/v1")
    return application


app = create_application()
