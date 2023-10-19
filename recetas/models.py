from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Receta(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    ingredientes = models.TextField(help_text='Redacta los ingredientes')
    preparacion = models.TextField()
    tiempo_registro = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    texto = models.TextField(help_text='Tù comentario', verbose_name='Comentario')

    def __str__(self):
        return self.texto





class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.EmailField()
    celular = models.IntegerField()
    
    def __str__(self):
        return self.correo

class Evento(models.Model):
    tipo = models.CharField(max_length=50)
    
    def __str__(self):
        return self.tipo
    
class Registrado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    detalles = models.TextField()
    fec_ini = models.DateTimeField()
    fec_fin = models.DateTimeField()

    def __str__(self):
        return self.evento.tipo +", "+ self.usuario.correo
    









































class EventoRegistrado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fec_ini = models.DateTimeField()
    fec_fin = models.DateTimeField()

    def __str__(self):
        return self.evento.tipo +", "+ self.usuario.correo