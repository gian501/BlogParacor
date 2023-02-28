from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
#from .forms import User
from django.contrib.auth.models import User


from django import forms

class PulseraFormulario(forms.Form):
    nombre = forms.CharField(label='Nombre:',max_length=15, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre',}))
    descripcion = forms.CheckboxInput()
    imagen = forms.ImageField()
    fechaCreacion = forms.DateField(label='Fecha de nacimiento:',widget=forms.SelectDateWidget(years=range(1900,2001), attrs={'class':'form-control', }))


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email:',max_length=254,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'ejemplo@ejemplo.com',}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
            #saca los mensajes de ayuda
        help_texts = {k: "" for k in fields}


