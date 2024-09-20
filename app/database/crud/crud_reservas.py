from app.database.schema.reservas import Reservas


class CRUDReservas:
    @staticmethod
    def create_object(
        fechaDeReserva = '01-01-2024',
        nombreHabitacion = '""',
        tipoHabitacion = '"',
        fechaDeCheckIn = '01-01-2024',
        fechaDeCheckOut = '01-01-2024',
        estado = 'activo',
        userId = 't01'
        ):
        h = Reservas(
            fechaDeReserva = fechaDeReserva,
            nombreHabitacion = nombreHabitacion,
            tipoHabitacion = tipoHabitacion,
            fechaDeCheckIn = fechaDeCheckIn,
            fechaDeCheckOut = fechaDeCheckOut,
            estado = estado,
            userId = userId
        ).save()

        data = Reservas.objects.filter(estado='activo')
        data = list(map(lambda transaction: transaction.to_mongo(), data))
        return data
        
    @staticmethod
    def get_reservas():
        try:
            new_reserva = Reservas.objects.filter(estado='activo')

            return new_reserva

        except Exception as e:
            raise e


    @staticmethod
    def update_turn_by_id(raw_id=123, payload={}):
        try:
            if not payload:
                return
            
            updator = {}
            for key in payload:
                updator[f"set__{key}"] = payload[key]

            Reservas.objects(rawId=raw_id).update(**updator)
        except Exception as e:
            raise e
        

    @staticmethod
    def get_by_turn(turn):
        try:
            data = Reservas.objects.filter(turnNumber=turn, fechaAtencion=None).limit(1)
            data = list(map(lambda transaction: transaction.to_mongo(), data))
            if len(data) > 0:
                return data[0]

            return None
        except Exception as e:
            raise e

    
    @staticmethod
    def get_by_id(raw_id):
        try:
            data = Reservas.objects.filter(rawId=raw_id).limit(1)
            data = list(map(lambda transaction: transaction.to_mongo(), data))
            if len(data) > 0:
                return data[0]

            return None
        except Exception as e:
            raise e

    
    @staticmethod
    def get_items(atendidos="false"):
        try:
            filters = {}
            if atendidos.lower() == "false":
                filters["fechaAtencion"] = None
            else:
                filters["fechaAtencion__ne"] = None

            data = Reservas.objects.filter(**filters).order_by("+turnNumber")
            return list(map(lambda transaction: transaction.to_mongo(), data))
        except Exception as e:
            raise e


