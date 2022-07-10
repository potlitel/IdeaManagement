from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS
import secretballot
# Create your models here.


class Topico(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Topicos'
        verbose_name = 'Topico'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

class Idea(models.Model):
      AVAILABLE = 'AV'
      NOT_AVAILABLE = 'Not_AV'
      Fhases = (
	        (AVAILABLE, 'Available'),
	        (NOT_AVAILABLE, 'Not available')
	    )
      titulo = models.CharField(max_length=128, unique=True, verbose_name='Title')
      descripcion = models.CharField(max_length=2555, unique=True, verbose_name='Description')
      fecha_adicion = models.DateTimeField(auto_now_add=True)
	    # indica si el propietario a llegado a un acuerdo con un inversionista para implementar
      estado = models.CharField(max_length=6,choices=Fhases,default=AVAILABLE, verbose_name='State')
      topico = models.ForeignKey(Topico, verbose_name='Topic')
      owner = models.ForeignKey(User, null=True, blank=True)
      project = models.CharField(max_length=2555, null=True, blank=True, verbose_name='Project')
	    #publicada = ?
      class Meta:
        verbose_name_plural = 'Ideas'
        verbose_name = 'Idea'
        ordering = ['titulo']
      def __str__(self):
        return u"%s" % self.titulo   
      # def save(self, *args, **kwargs):
      #   self.owner = self.request.user
      #   self.save()
		
class Feedback(models.Model):

    url = models.URLField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    update_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return self.url		

secretballot.enable_voting_on(Feedback)
secretballot.enable_voting_on(Idea)