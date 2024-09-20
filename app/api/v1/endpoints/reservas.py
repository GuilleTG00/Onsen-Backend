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

class Prioridad(BaseModel):
    id: int
    turn_number: int

class Atender(BaseModel):
    id: int
    estado: str = "atender"
    comment: str = ""


class Estado(BaseModel):
    id: int
    estado: str = "atender"


class AtencionesResults(BaseModel):
    hp: Optional[int] = None
    trainerName: Optional[str] = None
    trainerId: Optional[str] = None
    cambioEstado: Optional[dict] = None
    nivel: Optional[int] = None
    pokemonName: Optional[str] = None
    createdAt: Optional[str] = None
    pokemonId: Optional[int] = None
    pokemonInfo: Optional[dict] = None
    turnNumber: Optional[int] = None
    id: Optional[int] = None
    estado: Optional[str] = None
    comment: Optional[str] = None
    fechaAtencion: Optional[str] = None


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
    

@router.get('/get-atenciones')
def get_atenciones(atendidos="false", current_user=Depends(get_current_user)):
    try:
        list_of_fields = ["hp", "trainerName", "trainerId", "cambioEstado", "nivel", "pokemonName", "createdAt", "pokemonId", "pokemonInfo", "turnNumber", "estado", "comment", "fechaAtencion"]
        new_items = []
        result = CRUDReservas.get_items(atendidos=atendidos)
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
