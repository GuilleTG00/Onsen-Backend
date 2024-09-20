

from mongoengine import Document, StringField

from app.core.config import settings
class Reservas(Document):
    fechaDeReserva = StringField(required=False)
    nombreHabitacion = StringField(required=False)
    tipoHabitacion = StringField(required=False)
    fechaDeCheckIn = StringField(required=False)
    fechaDeCheckOut = StringField(required=False)
    estado = StringField(required=False)
    userId = StringField(required=False)
    meta = {
        "db_alias": settings.DB_ALIAS,
    }