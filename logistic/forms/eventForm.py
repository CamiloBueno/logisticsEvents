from django.forms import ModelForm, ValidationError, DateTimeInput, ModelChoiceField, HiddenInput
from django.contrib.auth.models import User
from ..models import Event


class EventForm(ModelForm):
    # Definir el campo de usuario dinámico
    user = ModelChoiceField(queryset=User.objects.all(),
                            label="Usuario", required=False)

    class Meta:
        model = Event
        fields = ["name", "executionDate", "place",
                  "progress", "finishDate", "important", "user"]

        widgets = {
            'executionDate': DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
            'finishDate': DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
        }

        labels = {
            'name': 'Nombre',
            'executionDate': 'Fecha de Ejecución',
            'place': 'Lugar',
            'progress': 'Progreso',
            'finishDate': 'Fecha de Finalización',
            'important': 'Importante',
            'user': 'Usuario',
        }

    def __init__(self, *args, **kwargs):
        # Obtenemos el usuario del kwargs, si se pasa desde la vista
        user = kwargs.pop('user', None)
        super(EventForm, self).__init__(*args, **kwargs)

        # Forzar el input_formats para los campos datetime
        self.fields['executionDate'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['finishDate'].input_formats = ('%Y-%m-%dT%H:%M',)

        # Si el usuario NO es superuser, se bloquea la selección de usuario y se asigna automático
        if user and not user.is_superuser:
            self.fields['user'].queryset = User.objects.filter(id=user.id)
            self.fields['user'].initial = user
            self.fields['user'].widget = HiddenInput()

    def clean_progress(self):
        progress = self.cleaned_data.get('progress')
        if progress is None:
            raise ValidationError("El progreso es obligatorio.")
        if progress < 0:
            raise ValidationError("No puede ser negativo.")
        if progress > 100:
            raise ValidationError("No puede ser mayor a 100.")
        return progress
