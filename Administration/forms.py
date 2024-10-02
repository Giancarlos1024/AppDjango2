from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'role')
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico',
            'username': 'Nombre de Usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
            'role': 'Rol',
        }


class CustomUserUpdateForm(forms.ModelForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput,
        required=False,
        label='Nueva contraseña'
    )

    new_password2 = forms.CharField(
        widget=forms.PasswordInput,
        required=False,
        label='Confirmar nueva contraseña'
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'username', 'role', 'new_password1', 'new_password2')
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico',
            'username': 'Nombre de Usuario',
            'role': 'Rol',
            'new_password1': 'Nueva contraseña',
            'new_password2': 'Confirmar nueva contraseña'
        }

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')
        if new_password1 and new_password2 and new_password1 != new_password2:
            self.add_error('new_password2', 'Las contraseñas no coinciden.')
