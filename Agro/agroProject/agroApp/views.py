from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.views.decorators.http import require_POST
from .models import RegistroActividad
from .forms import RegistroActividadForm
from datetime import datetime, timedelta
from django.utils import timezone

def es_administrador(user):
    return user.is_authenticated and user.is_staff

def inicio(request):
    return render(request, 'inicio.html')

def formulario_registro(request):
    if request.method == 'POST':
        formulario = RegistroActividadForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Actividad registrada correctamente.')
            return redirect('formulario_registro')
        messages.error(request,'Revisa los datos ingresados.')
    else:
        formulario = RegistroActividadForm()
    return render(request,'registro/formulario.html',{'formulario': formulario})

def login_administrador(request):
    if es_administrador(request.user):
        return redirect('dashboard')
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')
        user = authenticate(
            request,
            username=usuario,
            password=contrasena
        )
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard')
        messages.error(request,'Usuario o contraseña incorrectos, o sin permisos.')
    return render(request,'administrador/login.html')


@user_passes_test(es_administrador, login_url='login_administrador')
def dashboard(request):
    busqueda_id = request.GET.get('id', '').strip()
    busqueda_responsable = request.GET.get('responsable', '').strip()
    busqueda_fecha = request.GET.get('fecha', '').strip()
    busqueda_parcela = request.GET.get('parcela', '').strip()
    busqueda_actividad = request.GET.get('actividad', '').strip()
    registros = RegistroActividad.objects.all()
    if busqueda_id:
        if busqueda_id.isdigit():
            registros = registros.filter(id=int(busqueda_id))
        else:
            registros = registros.none()
    if busqueda_responsable:
        registros = registros.filter(responsable__icontains=busqueda_responsable)
    if busqueda_fecha:
        try:
            fecha = datetime.strptime(busqueda_fecha, '%Y-%m-%d').date()
            inicio_dia = timezone.make_aware(datetime.combine(fecha, datetime.min.time()),timezone.get_current_timezone())
            fin_dia = inicio_dia + timedelta(days=1)
            registros = registros.filter(fecha_registro__gte=inicio_dia,fecha_registro__lt=fin_dia)
        except ValueError:
            registros = registros.none()
    if busqueda_parcela:
        registros = registros.filter(parcela__icontains=busqueda_parcela)
    if busqueda_actividad:
        registros = registros.filter(actividad__icontains=busqueda_actividad)
    total_registros = RegistroActividad.objects.count()
    context = {
        'registros': registros,
        'total_registros': total_registros,
        'busqueda_id': busqueda_id,
        'busqueda_responsable': busqueda_responsable,
        'busqueda_fecha': busqueda_fecha,
        'busqueda_parcela': busqueda_parcela,
        'busqueda_actividad': busqueda_actividad,
    }
    return render(request, 'administrador/dashboard.html', context)

@user_passes_test(es_administrador,login_url='login_administrador')
def agregar_registro(request):
    if request.method == 'POST':
        formulario = RegistroActividadForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Registro agregado correctamente.')
            return redirect('dashboard')
    else:
        formulario = RegistroActividadForm()
    return render(request,'administrador/formulario.html',{'formulario': formulario,'titulo': 'Agregar registro'})

@user_passes_test(es_administrador,login_url='login_administrador')
def editar_registro(request, id):
    registro = get_object_or_404(RegistroActividad,id=id)
    if request.method == 'POST':
        formulario = RegistroActividadForm(
            request.POST,
            instance=registro
        )
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Registro modificado correctamente.')
            return redirect('dashboard')
    else:
        formulario = RegistroActividadForm(instance=registro)
    return render(request,'administrador/formulario.html',{'formulario': formulario,'titulo': 'Editar registro'})

@user_passes_test(es_administrador,login_url='login_administrador')
def eliminar_registro(request, id):
    registro = get_object_or_404(RegistroActividad,id=id)
    if request.method == 'POST':
        registro.delete()
        messages.success(request,'Registro eliminado correctamente.')
        return redirect('dashboard')
    return render(request,'administrador/eliminar.html',{'registro': registro})

@require_POST
@user_passes_test(
    es_administrador,
    login_url='login_administrador'
)
def cerrar_sesion(request):
    logout(request)
    return redirect('login_administrador')