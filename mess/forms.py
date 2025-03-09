from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Hides password input

    class Meta:
        model = User
        fields = ['username', 'password', 'role']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-control'}),
        }
