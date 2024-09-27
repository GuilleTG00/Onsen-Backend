

from mongoengine import Document, StringField, ListField, IntField

from app.core.config import settings
class Habitaciones(Document):
    title = StringField(required=False)
    subtitle = StringField(required=False)
    roomDescription = StringField(required=False)
    camas = StringField(required=False)
    precioDia = IntField(required=False)
    details = ListField(required=False)
    extraServices =ListField(required=False)
    images = ListField(required=False)
    meta = {
        "db_alias": settings.DB_ALIAS,
    }