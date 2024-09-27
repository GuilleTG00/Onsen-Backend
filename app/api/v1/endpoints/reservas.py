import traceback
import time

from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from app.api.v1.deps import get_current_user
from app.database.crud.crud_reservas import CRUDReservas
from app.api.v1.global_import import FastApiResponse
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class Reserva(BaseModel):
    fechaDeReserva: str
    habitacionData: dict
    habitacionId: str
    fechaDeCheckIn: str
    fechaDeCheckOut: str
    estado: str
    total: int
    serviciosEspeciales: list
    calificacion: Optional[int] 
    acompañantes: int

@router.post('/crear-reserva')
def crear_reserva(reserva: Reserva, current_user=Depends(get_current_user)):

    try:
        user_id = current_user.get("user_id")
        id_generated = int(time.time() * 1000)
        CRUDReservas.create_object( 
            fechaDeReserva = reserva.fechaDeReserva,
            fechaDeCheckIn = reserva.fechaDeCheckIn,
            fechaDeCheckOut = reserva.fechaDeCheckOut,
            estado = reserva.estado,
            calificacion=reserva.calificacion,
            total = reserva.total,
            serviciosEspeciales = reserva.serviciosEspeciales,
            acompañantes=reserva.acompañantes,
            habitacionData=reserva.habitacionData,
            habitacionId=reserva.habitacionId,
    )

        return { "id": id_generated }

    except Exception as e:
        print(f"Error: {e}", traceback.format_exc())
        return FastApiResponse.failure(str(e))


@router.get('/get-last-reserva')
def get_last_reserva(estado="activo", current_user=Depends(get_current_user)):
    try:
        list_of_fields = [
            "fechaDeReserva",
            "fechaDeCheckIn",
            "fechaDeCheckOut",
            "estado",
            "calificacion",
            "total",
            "serviciosEspeciales",
            "acompañantes",
            "habitacionData",
            "habitacionId"
        ]
        new_items = []
        result = CRUDReservas.get_reservas_by_state_last_check_in(estado=estado)
        for obt in result:
            item = {}
            item["id"] = str(obt.id)
            for field in list_of_fields:
                item[field] = getattr(obt, field, None)
            
            new_items.append(item)

        return new_items

    except Exception as e:
        print(f"Error: {e}", traceback.format_exc())
        return FastApiResponse.failure(str(e))



@router.get('/get-reservas-por-estado')
def get_reservas_por_estado(estado="activo", current_user=Depends(get_current_user)):
    try:
        list_of_fields = [
            "fechaDeReserva",
            "nombreHabitacion",
            "tipoHabitacion",
            "fechaDeCheckIn",
            "fechaDeCheckOut",
            "estado",
            "calificacion",
            "userId"
        ]
        new_items = []
        result = CRUDReservas.get_reservas_by_state(estado=estado)
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
