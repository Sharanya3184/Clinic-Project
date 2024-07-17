from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ( 'name','message',)


from django import forms

class MyForm(forms.Form):
    # your form fields here
    name = forms.CharField(max_length=255)
    email = forms.EmailField()

    cancel = forms.CharField(widget=forms.HiddenInput, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
from django import forms
from .models import EmergencyCase

class EmergencyCaseForm(forms.ModelForm):
    class Meta:
        model = EmergencyCase
        fields = ('patient_name', 'contact_number', 'emergency_type', 'description')

