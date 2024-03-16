from django.shortcuts import render
from django.http import * 

from .forms import CalorieForm
from .models import CalorieModel


# Our views

def ShowView(request):
    if request.method == 'POST':
        form = CalorieForm(request.POST)
        modelloop = CalorieModel.objects.all()

        try:
            deleted = request.POST.get('delta')
            x = CalorieModel.objects.filter(id=deleted)
            x.delete()
        except:
            pass

        
        try:
            if form.is_valid():
                form.save()
        except:
            pass

    else :
        form = CalorieForm()


    my_list = []

    for summ in modelloop:
        my_list.append((summ.calorie))
    x = (sum(my_list))


    

    context = {
        'form' : form, 
        'show' : CalorieModel.objects.all(),
        'sum' : x
        }

    return render(request, 'html/html.html', context = context)
            