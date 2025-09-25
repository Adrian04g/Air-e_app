from django import forms

# Formulario para el login usando el sistema de usuarios de Django
class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Usuario',
            'class': 'form-group'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña',
            'class': 'form-group'
        })
    )
