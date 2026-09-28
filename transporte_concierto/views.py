from django.http import JsonResponse
from . import consultas

# GET: Listar datos
def listar_viajes_pendientes(request):
    if request.method == 'GET':
        try:
            viajes = consultas.get_viajes_pendientes()
            return JsonResponse({'status': 'success', 'data': viajes})
        except Exception as e:
            # Captura el error y lo muestra en formato JSON
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def listar_pagos(request):
    if request.method == 'GET':
        try:
            pagos = consultas.get_pagos_realizados()
            return JsonResponse({'status': 'success', 'data': pagos})
        except Exception as e:
            # Captura el error y lo muestra en formato JSON
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)