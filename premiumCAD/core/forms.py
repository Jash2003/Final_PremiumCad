from django import forms
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['jobrole', 'name', 'email', 'phone', 'location', 'experience', 'resume']
