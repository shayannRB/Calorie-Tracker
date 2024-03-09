from django import forms

# making our forms

class CalorieForm(forms.ModelForm):
    class Meta:
        fields = ['__all__']