from django import forms
from .models import MenuItem, User
from django.core.validators import EmailValidator

class SignupForm(forms.Form):
    registration_number = forms.CharField(
        label="Registration number",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your registration number',
        })
    )

    username = forms.CharField(
        label="Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name',
        })
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        validators=[EmailValidator()],
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
        })
    )

    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        })
    )

    role = forms.ChoiceField(
        label="Role",
        choices=[
            ('Admin', 'Admin'),
            ('Worker', 'Worker'),
            ('Student/Staff', 'Student/Staff'),
        ],
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    def save(self):
        registration_number = self.cleaned_data['registration_number']
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        role = self.cleaned_data['role']
        user = User.objects.create_user(registration_number=registration_number,username=username, email=email, password=password, role=role)
        return user

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'is_available']  # Adjust fields accordingly