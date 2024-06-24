from django.shortcuts import render, redirect
from .models import Notificaciones, Colaborador
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Notificaciones
from django.core.paginator import Paginator

# Create your views here.
def listar(request):
    notificaciones = Notificaciones.objects.all()
    paginator = Paginator(notificaciones, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list_notificacion.html', {"page_obj": page_obj})


def listarC(request):
    return render(request, 'list_colaborador.html')

def listarR(request):
    return render(request, 'list_recepcionista.html')

def mostraA(request):
    return render(request, 'add_notificacion.html')

def mostrarC(request):
    return render(request, 'add_colaborador.html')

def crearC(request):
    if request.method == 'POST':
        nombre = request.POST.get('Nombre')
        apellido = request.POST.get('Apellido')

        nuevo_Colaborador = Colaborador(
            nombre=nombre,
            apellido=apellido
        )

        nuevo_Colaborador.save()
        return redirect('http://127.0.0.1:8000/')


def crearN(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        entidad = request.POST.get('entidad')
        numero_exp = request.POST.get('numero_exp')
        dirigido_a = request.POST.get('dirigido_a')
        recepcionista = request.POST.get('recepcionista')

        nueva_notificacion = Notificaciones(
            titulo=titulo,
            entidad=entidad,
            numero_exp=numero_exp,
            dirigido_a=dirigido_a,
            recepcionista=recepcionista
        )
        nueva_notificacion.save()
        
        if 'enviar_email' in request.POST:
            destinatario = 'marlonher0181@gmail.com'
            asunto = 'Nueva notificación creada'
            mensaje = f'Se ha creado una nueva notificación:\n\nTítulo: {titulo}\nEntidad: {entidad}\nNúmero de expediente: {numero_exp}'

            try:
                send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, [destinatario])
            except Exception as e:
                print(f'Error al enviar correo electrónico: {e}')

        return redirect('http://127.0.0.1:8000/')