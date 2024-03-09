from django.db import models

# calorie models

class CalorieModel(models.Model):
    food = models.CharField('food', max_length=250, blank=True)
    calorie = models.PositiveSmallIntegerField('calorie', blank=True)
    description = models.CharField('description', max_length=450, blank=True)
    created_time = models.DateTimeField('created_time', blank=True, auto_now_add = True)

    class Meta:
        db_table = 'caloriemodel'
        verbose_name = 'CalorieModel'
        verbose_name_plural = 'CalorieModels'

    def __str__(self):
      return self.food