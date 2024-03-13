from django.shortcuts import render
from django.http import * 

from .forms import CalorieForm
from .models import CalorieModel


# Our views

def ShowView(request):
    if request.method == 'POST':
        form = CalorieForm(request.POST)
        

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/calorie/')


        # title = request.POST.get('food')
        # calorie = request.POST.get('calorie')
        # description = request.POST.get('description')

    else :
        form = CalorieForm()

    context = {
        'form' : form, 
        'show' : CalorieModel.objects.all()
        }

    return render(request, 'html/html.html', context = context)
            