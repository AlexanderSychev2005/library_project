from django import forms
from .models import StudentOrder


class OrderForm(forms.ModelForm):
    class Meta:
        model = StudentOrder
        fields = ['created_at', 'return_at', 'status', 'book', 'student']