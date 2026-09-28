from django.db import connection

def dictfetchall(cursor):
    """Retorna todas las filas de un cursor como un diccionario."""
    if cursor.description is None:
        return None
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

# =======================
# 1. CONSULTAS SELECT (3)
# =======================
def get_pagos_realizados():
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT "id_pago", "monto" 
            FROM "Pago";
        ''')
        return dictfetchall(cursor)

def get_pasajeros_con_reserva():
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT DISTINCT 
                pas."nombre_completo",
                pas."telefono",
                pas."correo_electronico",
                ar."asientos_reserva"
            FROM "Pasajero" pas
            INNER JOIN "Reserva" r ON pas."id_pasajero" = r."id_pasajero"
            INNER JOIN "asientos_reserva" ar ON r."id_reserva" = ar."id_reserva";
        ''')
        return dictfetchall(cursor)

def get_viajes_pendientes():
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT 
                v."modelo",
                v."patente",
                vc."id_viaje",
                vc."direccion_origen",
                vc."direccion_destino"
            FROM "Viaje_a_concierto" vc
            INNER JOIN "Viaje_a_concierto_usa_Vehiculo" vv ON vc."id_viaje" = vv."id_viaje"
            INNER JOIN "Vehiculo" v ON vv."patente" = v."patente"
            WHERE vc."estado" = 'pendiente';
        ''')
        return dictfetchall(cursor)