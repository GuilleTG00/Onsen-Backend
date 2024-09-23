from app.database.schema.inventario import Inventario


class CRUDInventario:
    @staticmethod
    def create_object(
        nombreProducto = '',
        cantidad = 1,
        ):
        h = Inventario(
            nombreProducto = nombreProducto,
            cantidad = cantidad,
        ).save()

        data = Inventario.objects.filter()
        data = list(map(lambda transaction: transaction.to_mongo(), data))
        return data
        
    @staticmethod
    def get_all_inventario():
        try:
            new_reserva = Inventario.objects()

            return new_reserva

        except Exception as e:
            raise e


    @staticmethod
    def update_inventario_cantidad(nombreProducto='', cantidad=1):
        try:
            return Inventario.objects.filter(nombreProducto=nombreProducto).update_one(
                set__cantidad = cantidad
                )
        except Exception as e:
            raise e
