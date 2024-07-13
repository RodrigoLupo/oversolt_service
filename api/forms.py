from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Usuario, Administrador, Inspector, Analista, Cliente

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role')

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['correo', 'username', 'contraseña']

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['usuario']

class InspectorForm(forms.ModelForm):
    class Meta:
        model = Inspector
        fields = ['usuario']

class AnalistaForm(forms.ModelForm):
    class Meta:
        model = Analista
        fields = ['usuario']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['RUC', 'DNI', 'NOMBRE', 'APELLIDO', 'EMPRESA', 'usuario']
