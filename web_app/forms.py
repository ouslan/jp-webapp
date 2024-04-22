from django.forms import ModelForm, CharField
from django.contrib.auth.models import User
from .models import Order
from django import forms

class OrderForm(ModelForm):
    """
    Form for creating or updating an Order instance.
    """
    class Meta:
        model = Order
        fields = '__all__'

class SignInForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['unique'])
        return email