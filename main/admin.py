from django.contrib import admin

from .models import CalorieModel

# Register your models here.


class CalorieAdmin(admin.ModelAdmin):
    fields = ['food', 'calorie', 'description']

admin.site.register(CalorieModel, CalorieAdmin)