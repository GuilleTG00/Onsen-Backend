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
        calificacion="0",
        userId = 't01'
        ):
        h = Reservas(
            fechaDeReserva = fechaDeReserva,
            nombreHabitacion = nombreHabitacion,
            tipoHabitacion = tipoHabitacion,
            fechaDeCheckIn = fechaDeCheckIn,
            fechaDeCheckOut = fechaDeCheckOut,
            estado = estado,
            calificacion=calificacion,
            userId = userId
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
    def get_reservas_by_state(estado="activo"):
        try:
            data = Reservas.objects.filter(estado=estado).order_by("+fechaDeReserva")
            return list(map(lambda transaction: transaction.to_mongo(), data))
        except Exception as e:
            raise e
        
    @staticmethod
    def get_reservas_by_state_last_check_in(estado="activo"):
        try:
            data = Reservas.objects.filter(estado=estado).order_by("+fechaDeCheckIn")
            return list(map(lambda transaction: transaction.to_mongo(), data))
        except Exception as e:
            raise e




