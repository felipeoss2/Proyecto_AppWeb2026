from django.http import JsonResponse
from django.db import connection


def test_db(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1;")
        resultado = cursor.fetchone()

    return JsonResponse({
        "mensaje": "Hola cony",
        "resultado": resultado[0]
    })