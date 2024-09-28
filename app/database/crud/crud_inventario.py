from app.database.schema.inventario import Inventario


class CRUDInventario:
    @staticmethod
    def create_object(
        nombreProducto = '',
        cantidad = 1,
        image = '',
        inventario = True,
        precio = 1
        ):
        h = Inventario(
            nombreProducto = nombreProducto,
            cantidad = cantidad,
            image = image,
            inventario = inventario,
            precio = precio
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
    def update_inventario_cantidad(nombreProducto='', cantidad=1, id = ''):
        try:
            return Inventario.objects.filter(id=id).update_one(
                set__cantidad = cantidad,
                set__nombreProducto = nombreProducto
                )
        except Exception as e:
            raise e
