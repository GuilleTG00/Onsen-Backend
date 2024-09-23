import traceback
import time

from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from app.api.v1.deps import get_current_user
from app.database.crud.crud_inventario import CRUDInventario
from app.api.v1.global_import import FastApiResponse
from pydantic import BaseModel
from typing import Optional


router = APIRouter()

class Elemento_Inventario(BaseModel):
    nombreProducto: str
    cantidad: int

@router.post('/crear-elemento-inventario')
def crear_reserva(elemento_inventario: Elemento_Inventario, current_user=Depends(get_current_user)):

    try:
        user_id = current_user.get("user_id")
        id_generated = int(time.time() * 1000)
        real_turn = CRUDInventario.create_object( 
            nombreProducto = elemento_inventario.nombreProducto,
            cantidad = elemento_inventario.cantidad,
    )

        return { "id": id_generated }

    except Exception as e:
        print(f"Error: {e}", traceback.format_exc())
        return FastApiResponse.failure(str(e))

@router.post('/actualizar-elemento-inventario')
def cambiar_estado(nombreProducto, cantidad, current_user=Depends(get_current_user)):
    try:
        CRUDInventario.update_inventario_cantidad(nombreProducto, cantidad)

        return FastApiResponse.successful

    except Exception as e:
        print(f"Error: {e}", traceback.format_exc())
        return FastApiResponse.failure(str(e))
    

@router.get('/get-listado-inventario')
def get_reservas_por_estado(current_user=Depends(get_current_user)):
    try:
        list_of_fields = [
            "nombreProducto", 
            "cantidad" 
        ]
        new_items = []
        result = CRUDInventario.get_all_inventario()
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
