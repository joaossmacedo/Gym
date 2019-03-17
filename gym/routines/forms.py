from django import forms
from routines.models import Routine, Exercise

class RoutineForm(forms.ModelForm):
    class Meta():
        model = Routine
        fields = ('name', )


class ExerciseForm(forms.ModelForm):
    class Meta():
        model = Exercise
        fields = ('routine', 'name', 'reps', 'weight')
