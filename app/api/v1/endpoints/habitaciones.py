import traceback
import time

from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from app.api.v1.deps import get_current_user
from app.database.crud.crud_habitaciones import CRUDHabitaciones
from app.api.v1.global_import import FastApiResponse
from pydantic import BaseModel
from typing import Optional


router = APIRouter()

class Habitacion(BaseModel):
    title: str
    subtitle: str
    roomDescription: str
    camas: str
    precioDia: int
    details: list
    extraServices: list
    images: list

@router.post('/crear-habitacion')
def crear_habitacion(habitacion: Habitacion, current_user=Depends(get_current_user)):

    try:
        user_id = current_user.get("user_id")
        id_generated = int(time.time() * 1000)
        real_turn = CRUDHabitaciones.create_object( 
            title = habitacion.title,
            subtitle = habitacion.subtitle,
            roomDescription = habitacion.roomDescription,
            camas = habitacion.camas,
            precioDia = habitacion.precioDia,
            details = habitacion.details,
            extraServices = habitacion.extraServices,
            images = habitacion.title
    )

        return { "id": id_generated }

    except Exception as e:
        print(f"Error: {e}", traceback.format_exc())
        return FastApiResponse.failure(str(e))


@router.get('/get-listado-habitaciones')
def get_listado_habitaciones(current_user=Depends(get_current_user)):
    try:
        list_of_fields = [
            "title",
            "subtitle",
            "roomDescription",
            "camas",
            "precioDia",
            "details",
            "extraServices",
            "images"
        ]
        new_items = []
        result = CRUDHabitaciones.get_all_habitaciones()
        for obt in result:
            item = {}
            item["id"] = obt.get("rawId")
            for field in list_of_fields:
                item[field] = obt.get(field)
            
            new_items.append(item)

        return new_items

    except Exception as e:
        print(f"Error: {e}", traceback.format_exc())
        return FastApiResponse.failure(str(e))
