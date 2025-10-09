"""Health check endpoint for the GymApp API."""
from fastapi import APIRouter

router = APIRouter()


@router.get("", summary="API health check")
async def health_check() -> dict[str, str]:
    """Return a simple response indicating the API status."""
    return {"status": "ok"}
