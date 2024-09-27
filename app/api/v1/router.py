from fastapi import APIRouter

from app.api.v1.endpoints import users, reservas, inventario, habitaciones,  health

api_router = APIRouter()

# Users
api_router.include_router(users.router, prefix="/users", tags=["Users"])

# Reservas
api_router.include_router(reservas.router, prefix="/reservas", tags=["Reservas"])

# Inventario
api_router.include_router(inventario.router, prefix="/inventario", tags=["Inventario"])

# Habitaciones
api_router.include_router(habitaciones.router, prefix="/habitaciones", tags=["Habitaciones"])

# Health
api_router.include_router(health.router, prefix="/health", tags=["Health"])
