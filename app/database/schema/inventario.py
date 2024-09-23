

from mongoengine import Document, StringField, IntField

from app.core.config import settings
class Inventario(Document):
    nombreProducto = StringField(required=False)
    cantidad = IntField(required=False)
    meta = {
        "db_alias": settings.DB_ALIAS,
    }