from django import forms
from .models import PrayerRequest
from django.utils.translation import gettext_lazy as _  


class PrayerRequestForm(forms.ModelForm):
    class Meta:
        model = PrayerRequest
        fields = ['full_name', 'email', 'prayer_request']

        # forms.py
from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['full_name', 'email', 'phone', 'category', 'additional_details']
        widgets = {
            'additional_details': forms.Textarea(attrs={'rows': 4}),
        }

    # Custom email validation to check if the email already exists
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Registration.objects.filter(email=email).exists():
            raise forms.ValidationError(_('Email already exists. Please use a different email address.'))
        return email