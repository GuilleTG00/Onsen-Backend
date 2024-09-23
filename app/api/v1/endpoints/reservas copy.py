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
    fechaDeReserva = str
    nombreHabitacion = str
    tipoHabitacion = str
    fechaDeCheckIn = str
    fechaDeCheckOut = str
    estado = str
    calificacion = str

@router.post('/crear-reserva')
def crear_reserva(reserva: Reserva, current_user=Depends(get_current_user)):

    try:
        user_id = current_user.get("user_id")
        id_generated = int(time.time() * 1000)
        real_turn = CRUDReservas.create_object( 
            fechaDeReserva = reserva.fechaDeReserva,
            nombreHabitacion = reserva.nombreHabitacion,
            tipoHabitacion = reserva.tipoHabitacion,
            fechaDeCheckIn = reserva.fechaDeCheckIn,
            fechaDeCheckOut = reserva.fechaDeCheckOut,
            estado = reserva.estado,
            calificacion=reserva.calificacion,
            user_id = user_id
    )

        return { "id": id_generated }

    except Exception as e:
        print(f"Error: {e}", traceback.format_exc())
        return FastApiResponse.failure(str(e))



@router.post('/cambiar-prioridad')
def cambiar_prioridad(prioridad: Prioridad, current_user=Depends(get_current_user)):
    try:
        # obtengo cita anterior
        cita_anterior = CRUDReservas.get_by_turn(prioridad.turn_number)
        current_cita = CRUDReservas.get_by_id(prioridad.id)
        if cita_anterior:
            CRUDReservas.update_turn_by_id(raw_id=cita_anterior.get("rawId"), payload={ "turnNumber": current_cita.get("turnNumber") })

        payload = { "turnNumber": prioridad.turn_number }
        CRUDReservas.update_turn_by_id(raw_id=prioridad.id, payload=payload)

        return FastApiResponse.successful

    except Exception as e:
        print(f"Error: {e}", traceback.format_exc())
        return FastApiResponse.failure(str(e))
    

@router.post('/atender')
def atender(atender: Atender, current_user=Depends(get_current_user)):
    try:
        payload = {
            "estado": atender.estado,
            "comment": atender.comment,
            "fechaAtencion": datetime.now()
            }

        CRUDReservas.update_turn_by_id(raw_id=atender.id, payload=payload)

        return FastApiResponse.successful

    except Exception as e:
        print(f"Error: {e}", traceback.format_exc())
        return FastApiResponse.failure(str(e))
    

@router.post('/cambiar-estado')
def cambiar_estado(estado: Estado, current_user=Depends(get_current_user)):
    try:
        payload = {
            "estado": estado.estado
            }

        CRUDReservas.update_turn_by_id(raw_id=estado.id, payload=payload)

        return FastApiResponse.successful

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
        result = CRUDReservas.get_items_by_state(estado=estado)
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
