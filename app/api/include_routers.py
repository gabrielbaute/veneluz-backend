from fastapi import FastAPI

from app.api.routes.electric_event_routes import router as events_router
from app.api.routes.health_routes import router as health_router

def include_routers(app: FastAPI, prefix: str = ""):
    """
    Include routers for API routes
    """
    app.include_router(events_router, prefix=prefix)
    app.include_router(health_router, prefix=prefix)
