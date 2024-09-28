

from mongoengine import Document, StringField, IntField, BooleanField

from app.core.config import settings
class Inventario(Document):
    nombreProducto = StringField(required=False)
    cantidad = IntField(required=False)
    image = StringField(required=False)
    inventario = BooleanField(required=False)
    precio = IntField(required = False)
    meta = {
        "db_alias": settings.DB_ALIAS,
    }