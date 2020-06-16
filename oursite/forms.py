from django import forms
from .models import Contact_us

class contactForm(forms.ModelForm):
    firstname =forms.CharField(label='firstname')
    lastname =forms.CharField(label='lastname')
    email =forms.CharField(label='email')
    subject =forms.CharField(label='subject')
    message =forms.CharField(label='message')
    class Meta:
        model = Contact_us
        fields = ('firstname','lastname', 'email', 'subject', 'message')