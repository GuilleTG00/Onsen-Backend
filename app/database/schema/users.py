import datetime

from mongoengine import Document, StringField, DateTimeField

from app.core.config import settings
class Users(Document):
    
    username = StringField(required=False)
    password = StringField(required=False)
    name =StringField(required=False)
    fullname = StringField(required=False)
    id_type =  StringField(required=False)
    id_number = StringField(required=False)
    status = StringField(required=False, default="active")
    createdBy = StringField(required=False)
    modifiedBy = StringField(required=False)
    createdDate = DateTimeField(default=datetime.datetime.now)
    modifiedDate = DateTimeField(default=datetime.datetime.now)
    meta = {
        "db_alias": settings.DB_ALIAS,
    }