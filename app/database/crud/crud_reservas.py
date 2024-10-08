from app.database.schema.reservas import Reservas


class CRUDReservas:
    @staticmethod
    def create_object(
        fechaDeReserva = '01-01-2024',
        habitacionData = {},
        habitacionId = '',
        fechaDeCheckIn = '01-01-2024',
        fechaDeCheckOut = '01-01-2024',
        estado = 'activo',
        calificacion="0",
        userId = '',
        total = 0,
        serviciosEspeciales = [],
        acompañantes = 0,
        ):
        h = Reservas(
            fechaDeReserva = fechaDeReserva,
            habitacionData = habitacionData,
            habitacionId = habitacionId,
            fechaDeCheckIn = fechaDeCheckIn,
            fechaDeCheckOut = fechaDeCheckOut,
            estado = estado,
            userId = userId,
            calificacion = calificacion,
            total = total,
            serviciosEspeciales = serviciosEspeciales,
            acompañantes = acompañantes,
        ).save()

        data = Reservas.objects.filter(estado='activo')
        data = list(map(lambda transaction: transaction.to_mongo(), data))
        return data
    
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
    def get_reservas_by_state(estado="activo", userId= ""):
        try:
            data = Reservas.objects.filter(estado=estado, userId=userId).order_by("+fechaDeReserva")
            return data
        except Exception as e:
            raise e
        
    @staticmethod
    def get_reservas_by_state_last_check_in(estado="activo", userId =""):
        try:
            data = Reservas.objects.filter(estado=estado, userId=userId).order_by("-fechaDeCheckIn").first()
            return [data]
        except Exception as e:
            raise e




