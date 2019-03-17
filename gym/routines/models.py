from django.db import models
from django.urls import reverse


# Create your models here.
class Routine(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("routines:routine_detail",kwargs={'pk':self.pk})


class Exercise(models.Model):
    routine = models.ForeignKey('routines.Routine',related_name='exercises',on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    reps = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("routines:exercise_new")
