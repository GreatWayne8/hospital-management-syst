from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model =Patient
        fields='__all__'
        widgets = {
            "date_of_birth" : forms.DateInput(attrs ={"type":"date"}),
            "medical_history":forms.Textarea(attrs={"rows":3}),
            "current_medications":forms.Textarea(attrs={"rows":3}),
            "allergies":forms.Textarea(attrs={"rows":3}),
            }