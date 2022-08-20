from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile

class UserRegistrationForm(forms.Form):
    username= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        email=self.cleaned_data['email']
        user=User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('this email already exists')
        return email
    def clean_username(self):
        username=self.cleaned_data['username']
        user=User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('this user already exists')
        return username
    def clean(self):
        cd=super().clean()
        p1=cd.get('password')
        p2=cd.get('password1')
        if p1 and p2 and p1 != p2:
            raise ValidationError('passwords must match')

class UserLoginForm(forms.Form):
    username= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class EditeUserForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=Profile
        fields=('age', 'bio')
