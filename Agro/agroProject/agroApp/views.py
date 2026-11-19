from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.views.decorators.http import require_POST
from .models import RegistroActividad
from .forms import RegistroActividadForm

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

@user_passes_test(es_administrador,login_url='login_administrador')
def dashboard(request):
    busqueda = request.GET.get('buscar', '').strip()
    registros = RegistroActividad.objects.all()
    if busqueda:
        registros = registros.filter(
            Q(responsable__icontains=busqueda) |
            Q(actividad__icontains=busqueda) |
            Q(parcela__icontains=busqueda)
        )
    total_registros = RegistroActividad.objects.count()
    context = {
        'registros': registros,
        'total_registros': total_registros,
        'busqueda': busqueda
    }
    return render(request,'administrador/dashboard.html',context)

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