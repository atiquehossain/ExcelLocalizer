from django import forms
from django.contrib.auth.forms import UserCreationForm
from authorizeapp.models import User

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    organization = forms.CharField(max_length=100)
    role = forms.ChoiceField(choices=[
        ('developer', 'Developer'),
        ('ba', 'BA'),
        ('qa', 'QA')
    ])

    class Meta:
        model = User
        fields = ['email', 'username', 'name', 'organization', 'role', 'password1', 'password2']