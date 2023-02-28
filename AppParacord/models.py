from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pulsera(models.Model):
    nombre = models.CharField('Título', max_length = 255, blank = False, null = False)
    descripcion = models.TextField('Descripción',null = True,blank = True)
    imagen = models.ImageField('Imagen', upload_to='libros/',max_length=255,null = True,blank = True)
    fechaCreacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)

    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha de creacion: {self.fecha_creacion}"
# crear otra clase para cada elemento
class Accesorio(models.Model):

    nombre = models.CharField('Título', max_length = 255, blank = False, null = False)
    descripcion = models.TextField('Descripción',null = True,blank = True)
    imagen = models.ImageField('Imagen', upload_to='libros/',max_length=255,null = True,blank = True)
    fechaCreacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)

    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha de creacion: {self.fecha_creacion}"
class Nudo(models.Model):
    nombre = models.CharField('Título', max_length = 255, blank = False, null = False)
    descripcion = models.TextField('Descripción',null = True,blank = True)
    imagen = models.ImageField('Imagen', upload_to='libros/',max_length=255,null = True,blank = True)
    fechaCreacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)
  

    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha de creacion: {self.fecha_creacion}"
class Mascota(models.Model):
    nombre = models.CharField('Título', max_length = 255, blank = False, null = False)
    descripcion = models.TextField('Descripción',null = True,blank = True)
    imagen = models.ImageField('Imagen', upload_to='libros/',max_length=255,null = True,blank = True)
    fechaCreacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)

    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha de creacion: {self.fecha_creacion}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    


