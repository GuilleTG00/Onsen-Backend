from mongoengine import Document, StringField, IntField, ListField, DictField
from app.core.config import settings

class Reservas(Document):
    fechaDeReserva = StringField(required=False)
    habitacionData = DictField(required=False)
    habitacionId = StringField(required=False)
    fechaDeCheckIn = StringField(required=False)
    fechaDeCheckOut = StringField(required=False)
    estado = StringField(required=False)
    calificacion = StringField(required=False)
    userId = StringField(required=False)
    total = IntField(required=False)
    serviciosEspeciales = ListField(required=False) 
    acompañantes = IntField(required=False)

    meta = {
        "db_alias": settings.DB_ALIAS,
    }