from django import forms
from .models import User
import hashlib


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'phone_number', 'email', 'age']

    def clean(self):
        hash_object = hashlib.sha256()
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        if len(password) < 6:
            raise forms.ValidationError("Password must contain at least 6 characters")

        hash_object.update(cleaned_data.get('password').encode('utf-8'))
        hashed_password = hash_object.hexdigest()

        hash_object.update(cleaned_data.get('confirm_password').encode('utf-8'))
        hashed_confirm_password = hash_object.hexdigest()

        cleaned_data['password'] = hashed_password
        cleaned_data['confirm_password'] = hashed_confirm_password

        return cleaned_data
