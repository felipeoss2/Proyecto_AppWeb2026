from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Django funcionando correctamente")