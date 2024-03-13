from django import forms

from .models import CalorieModel
# making our forms

class CalorieForm(forms.ModelForm):
    class Meta:
        model = CalorieModel
        fields = ['food', 'calorie', 'description']
    
        