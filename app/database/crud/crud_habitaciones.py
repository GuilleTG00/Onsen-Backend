from app.database.schema.habitaciones import Habitaciones


class CRUDHabitaciones:
    @staticmethod
    def create_object(
    title = '',
    subtitle = '',
    roomDescription = '',
    camas = '',
    predcioDia = 1,
    details = [],
    extraServices = [],
    images = []
        ):
        h = Habitaciones(
            title = title,
            subtitle = subtitle,
            roomDescription = roomDescription,
            camas = camas,
            predcioDia = predcioDia,
            details = details,
            extraServices = extraServices,
            images = images
        ).save()

        data = Habitaciones.objects.filter()
        data = list(map(lambda transaction: transaction.to_mongo(), data))
        return data
        
    @staticmethod
    def get_all_habitaciones():
        try:
            new_habitaciones_list = Habitaciones.objects()

            return new_habitaciones_list

        except Exception as e:
            raise e
