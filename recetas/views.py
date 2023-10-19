from django.shortcuts import render, redirect
from .models import Evento, Usuario, Registrado
import datetime
# Create your views here.
def index(request):
    usuarios = Usuario.objects.order_by('correo')
    eventos = Evento.objects.order_by('tipo')
    registrados = Registrado.objects.order_by('usuario__correo')

    context = {'usuarios':usuarios, 'eventos': eventos, 'registrados': registrados}
    return render(request,'listaTotal.html', context);

def form_user(request):
    titulo = "Crear Usuario"
    boton = "Crear"
    id = request.POST.get("id")
    crud = request.POST.get("crud")
    if crud == "Editar":
        titulo = "Modificar Usuario"
        boton = "Actualizar"
        
        usuario = Usuario.objects.filter(id=id).get()
        lista = {'usuario':usuario,'accion': titulo, 'enviar': boton}

        return render(request,'form_usuario.html',lista)
    
    elif crud == "Eliminar":
        Usuario.objects.get(id=id).delete()
        return redirect('/recetas')
    
    return render(request,'form_usuario.html', {'accion': titulo, 'enviar': boton})

def form_event(request):
    accion = "Crear Evento"
    enviar = "Crear"
    crud = request.POST.get("crud")
    id = request.POST.get("id")

    if crud == "Editar":
        accion = "Modificar Evento"
        enviar = "Actualizar"

        evento = Evento.objects.filter(id=id).get()
        lista = {'evento': evento, 'accion': accion, 'enviar': enviar}
        return render(request,'form_event.html',lista)
    
    elif crud == "Eliminar":
        Evento.objects.get(id=id).delete()
        return redirect('/recetas')
    
    
    return render(request,'form_event.html', {'accion': accion, 'enviar': enviar})

def form_item(request):
    accion = "Crear Registro"
    enviar = "Crear"

    id = request.POST.get("id")
    crud = request.POST.get("crud")

    usuarios = Usuario.objects.order_by('correo')
    eventos = Evento.objects.order_by('tipo')

    if crud == "Editar":
        titulo = "Modificar Registro"
        boton = "Actualizar"
        
        registro = Registrado.objects.filter(id=id).get()
        lista = {'usuarios':usuarios, 'eventos': eventos, 'registro':registro,'accion': titulo, 'enviar': boton}

        return render(request,'form_item.html',lista)
    
    elif crud == "Eliminar":
        Registrado.objects.get(id=id).delete()
        return redirect('/recetas')
    
    

    lista = {'usuarios':usuarios, 'eventos': eventos, 'accion': accion, 'enviar': enviar}
    return render(request,'form_item.html', lista)




def register_user(request):
    nombre = request.POST.get("nombre")
    correo = request.POST.get("correo")
    celular = request.POST.get("celular")
    id = request.POST.get("id")

    u = None

    if request.POST.get("crud") == "actualizar":
        u = Usuario.objects.get(id=id)
    else:
        u = Usuario()
        
    u.nombre = nombre
    u.correo = correo
    u.celular = celular
    u.save()    
    return redirect('/recetas')

def register_event(request):
    tipo = request.POST.get("tipo")
    id = request.POST.get("id")
    
    e = None
    if request.POST.get("crud") == "actualizar":
        e = Evento.objects.get(id=id)
    else:
        e = Evento()
    
    e.tipo = tipo
    e.save()

    return redirect('/recetas')

def register_item(request):

    id_u = request.POST.get("id-usuario")
    id_e = request.POST.get("id-evento")
    detalles = request.POST.get("detalles")
    fec_ini = request.POST.get("fec-ini")
    fec_fin = request.POST.get("fec-fin")
    id = request.POST.get("id")
    i = None

    if request.POST.get("crud") == "actualizar":
        i = Registrado.objects.get(id=id)
    else:
        i = Registrado()

    u = Usuario.objects.get(id=id_u)
    e = Evento.objects.get(id=id_e)
    
    fec_ini = datetime.datetime.strptime(fec_ini, "%Y-%m-%dT%H:%M")
    fec_fin = datetime.datetime.strptime(fec_fin, "%Y-%m-%dT%H:%M")
    i.evento = e
    i.usuario = u
    i.detalles = detalles
    i.fec_ini = fec_ini
    i.fec_fin = fec_fin
    i.save()

    return redirect('/recetas')
