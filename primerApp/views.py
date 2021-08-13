from django.shortcuts import render
from .models import Usuario
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hola desde el servidor')

def form(request):
    return render(request, 'form.html')

def respform(request):
    # Datos que ingreso el usuario
    text = request.POST['decir']
    to = request.POST['a']

    # Informacion de la base de datos
    try:
        user = Usuario.objects.get(user = text)
        # Verificamos que exista en la base de datos
        if (user.user == text) and (user.password == to):
            return HttpResponse(f'Bienvenido {text} al login secreto')
        else:
            return HttpResponse(f'{user.user} desde el servidor')
    except:
        return HttpResponse(f'{text} {to} desde el servidor')

    