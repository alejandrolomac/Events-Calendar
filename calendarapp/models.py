from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


COLOR_CHOICES = (
    ('#f33', 'Rojo'),
    ('#5f33ff', 'Azul'),
    ('#ffd333', 'Amarillo'),
    ('#ff7e33', 'Anaranjado'),
    ('#a3f', 'Morado'),
    ('#3aff33', 'Verde'),
)

class TypeEvents(models.Model):
    name = models.CharField('Tipo de Evento', max_length=200)
    color = models.CharField('Color de Evento', max_length=20)
    
    def __str__(self):
        return self.name

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Titulo', max_length=200)
    color = models.CharField('Color de Evento', max_length=20, choices=COLOR_CHOICES, default='Azul')
    tipo = models.ForeignKey(TypeEvents, on_delete=models.CASCADE, blank=True)
    description = models.TextField('Descripción')
    start_time = models.DateTimeField('Comienzo de Evento')
    end_time = models.DateTimeField('Final de Evento')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('calendarapp:event-detail', args=(self.id,))

    @property
    def get_html_url(self):
        color = self.color
        url = reverse('calendarapp:event-detail', args=(self.id,))
        return f'<a href="{url}"><span style="background: {self.color};"></span> {self.title} </a>'
    
    @property
    def get_color_type(self):
        color = self.color
        return color


class EventMember(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Nombre', max_length=200)
    adults = models.IntegerField('Adultos', default=0)
    kids = models.IntegerField('Niños', default=0)

    #class Meta:
    #    unique_together = ['event', 'user']

    def __str__(self):
        return str(self.name)