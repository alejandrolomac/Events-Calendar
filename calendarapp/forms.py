from django.forms import ModelForm, DateInput
from calendarapp.models import Event, EventMember
from django import forms

class EventForm(ModelForm):
  title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre del Evento'}))
  description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Descripción del Evento'}))

  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    exclude = ['user']

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['title'].required=True
    self.fields['color'].required=True
    self.fields['tipo'].required=True
    self.fields['description'].required=True
    self.fields['start_time'].required=True
    self.fields['end_time'].required=True


class SignupForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class AddMemberForm(forms.ModelForm):
  name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre Completo'}))

  class Meta:
    model = EventMember
    fields = ['name', 'adults', 'kids']
