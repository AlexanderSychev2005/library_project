from django import forms
from .models import StudentOrder


class StudentOrderForm(forms.ModelForm):
    class Meta:
        model = StudentOrder
        fields = '__all__'