from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['nombre', 'apellido', 'edad', 'usuario', 'correo', 'contraseña']
