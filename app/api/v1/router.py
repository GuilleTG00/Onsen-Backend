from fastapi import APIRouter

from app.api.v1.endpoints import users, reservas, health

api_router = APIRouter()

# Users
api_router.include_router(users.router, prefix="/users", tags=["Users"])

# Reservas
api_router.include_router(reservas.router, prefix="/reservas", tags=["Reservas"])

# Health
api_router.include_router(health.router, prefix="/health", tags=["Health"])
