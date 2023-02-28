from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppParacord.models import *
from AppParacord.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
#from .models import Usuarios
#from .forms import RegistrarUsuario



def inicio(request):
    return render(request, "AppParacord/inicio.html", )
    
def pulseras(request):
    if request.method == "POST":
 
        miFormulario = PulseraFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            pulsera = Pulsera (nombre=informacion["nombre"], descripcion=informacion["descripcion"],imagen=informacion["imagen"],fechaCreacion=informacion["fechaCreacion"],broche=informacion["broche"])
            pulsera.save()
            return render(request, "AppParacord/inicio.html")
    else:
        miFormulario = PulseraFormulario()
        
    return render(request, 'AppParacord/pulseras.html', {"miFormulario":miFormulario})
class PulseraList(ListView):
    model = Pulsera
    template_name = "AppParacord/pulsera_list.html"   
class PulseraDetalle(DetailView):
    model = Pulsera
    template_name = "AppParacord/pulsera_detalle.html"
    
class PulseraCreacion(CreateView):
    model = Pulsera
    success_url = "/AppParacord/pulsera/list"
    fields = ['id','nombre', 'descripcion', 'imagen', 'fechaCreacion', 'broche']

class PulseraUpdate(UpdateView):
    model = Pulsera
    success_url = "/AppParacord/pulsera/list"
    fields = fields = ['id','nombre', 'descripcion', 'imagen', 'fechaCreacion', 'broche'] 
    
class PulseraDelete(DeleteView):
    model = Pulsera
    success_url = "/AppParacord/pulsera/list"


'''
def profesores(request):
    if request.method == "POST":
 
        miFormulario = ProfesoresFormulario(request.POST) 
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"], profesion=informacion["profesion"])
            profesor.save()
            #return render(request, "AppE03/profesores.html" )
            return render(request, "AppE03/inicio.html")       
    else:
        miFormulario = ProfesoresFormulario()
        
    return render(request, 'AppE03/profesores.html', {"miFormulario":miFormulario})

def estudiantes(request):
    if request.method == "POST":
 
        miFormulario = EstudiantesFormulario(request.POST) 
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"])
            estudiante.save()
            #return render(request, "AppE03/estudiantes.html" )
            return render(request, "AppE03/inicio.html") 
    else:
        miFormulario = EstudiantesFormulario()

    return render(request, 'AppE03/estudiantes.html', {"miFormulario":miFormulario})


def entregables(request):
    if request.method == "POST":
 
        miFormulario = EntregableFormulario(request.POST) 
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            entregable = Entregable (nombre=informacion["nombre"],apellido=informacion["apellido"],email=informacion["email"], fechaEntrega=informacion["fechaEntrega"],entregado=informacion["entregado"])
            entregable.save()
            #return render(request, "AppE03/entregables.html" )
            return render(request, "AppE03/inicio.html") 
    else:
        miFormulario = EntregableFormulario()

    return render(request, 'AppE03/entregables.html', {"miFormulario":miFormulario})

def busquedaComision(request):
    return render(request, "AppE03/busquedaComision.html" )

def buscar(request):
    if request.GET['comision']:
        comision= request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains=comision)
        return render(request, "AppE03/resultadoBusqueda.html", {"cursos":cursos, "comision":comision})
    else:
        respuesta = "No enviaste datos"
    
    #return render(request, 'AppC/inicio.html',{"respuesta": respuesta})
    return HttpResponse(respuesta)
'''

    

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
                
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppParacord/inicio.html", {"mensaje": "Usuario Creado: "})
    
    else:
        form = UserCreationForm()
    
    return render(request, "AppParacord/registro.html", {"form":form})
def login_request(request):

    if request.method =="POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password = contra)
            if user is not None:
                login(request, user)
                return render(request, "AppParacord/inicio.html", {"mensaje":f"BIENVENIDO, {usuario}!!!!"})
            else:
                return render(request, "AppParacord/inicio.html", {"mensaje":f"Error!!!!"})
        else:
            return render(request, "AppParacord/inicio.html", {"mensaje":f"Error FORMULARIO"})

    form = AuthenticationForm()  

    return render(request, "AppParacord/login.html", {"form":form} )


'''def registro(request):
    mis_usuarios = Usuarios.objects.all()
    if request.method == 'POST':
        register_form = RegistrarUsuario(request.POST)
        if register_form.is_valid():
            success = register_form.registrar_usuario()
            return redirect('./')
    else:
        register_form = RegistrarUsuario()
        return render(request, 'AppParacord/registro.html', 
                      {'register_form': register_form,'usuarios': mis_usuarios})   #formulario del profe registro usuario'''