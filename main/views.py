from django.shortcuts import render
from django.http import * 

from .forms import CalorieForm
from .models import CalorieModel


# Our views

def ShowView(request):
    if request.method == 'POST':
        form = CalorieForm(request.POST)
        
        try:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/calorie/')
        except:
            return HttpResponseForbidden('not allowed')


        # title = request.POST.get('food')
        # calorie = request.POST.get('calorie')
        # description = request.POST.get('description')

    else :
        form = CalorieForm()

    modelloop = CalorieModel.objects.all()


    my_list = []

    for summ in modelloop:
        my_list.append((summ.calorie))
    x = (sum(my_list))
    print(x)


    context = {
        'form' : form, 
        'show' : CalorieModel.objects.all(),
        'sum' : x
        }

    return render(request, 'html/html.html', context = context)
            