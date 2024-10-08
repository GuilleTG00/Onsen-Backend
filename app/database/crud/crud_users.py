import datetime

from app.database.schema.users import Users


DOGO_ONSEN_VAR = "DOGO-ONSEN"


class CRUDUsers:
    @staticmethod
    def create_object(username, 
                      password,
                      name,
                      fullname,
                      id_type,
                      id_number,
                      status="active",
                      created_by=DOGO_ONSEN_VAR,
                      modified_by=DOGO_ONSEN_VAR,
                      created_date=datetime.datetime.now,
                      modified_date=datetime.datetime.now,

                      ):
        h = Users(
            username=username,
            password=password,
            name=name,
            fullname=fullname,
            id_type=id_type,
            id_number=id_number,
            status=status,
            createdBy=created_by,
            modifiedBy=modified_by,
            createdDate=created_date,
            modifiedDate=modified_date,
        ).save()
        return h
    

    @staticmethod
    def get_by_username(username, status="active"):
        obj = Users.objects.filter(
            username=username, status=status).limit(1)
        if obj:
            return obj[0]
        else:
            return None
        
    
    @staticmethod
    def user_already_exist(username, status="active"):
        try:
            obj = Users.objects.filter(
                username=username, status=status).limit(1)
            if obj:
                return True
            return False
        except Exception as e:
            print(f"Error: {e}")
            raise e
        
    
    @staticmethod
    def update_password(user_id, new_password):
        query = {
            "_id": user_id,
        }
        try:
            updator = {
                f"set__password": new_password
            }
            Users.objects(**query).update(**updator)
        except Exception as e:
            raise e
