def criterios_orden(objeto):
    hp = objeto.get('hp')
    cambio_estado = objeto.get('cambioEstado')
    nivel = objeto.get('nivel')
    created_at = objeto.get('createdAt')

    return (hp, not cambio_estado, nivel, created_at)
