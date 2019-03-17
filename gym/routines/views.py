from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from routines.models import Routine, Exercise
from routines.forms import RoutineForm, ExerciseForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  DeleteView, UpdateView,)

# Create your views here.
class RoutineListView(ListView):
    model = Routine

class RoutineDetailView(DetailView):
    model = Routine

class CreateRoutineView(CreateView):
    redirect_field_name = 'routines/routine_detail.html'

    form_class = RoutineForm

    model = Routine

class RoutineUpdateView(UpdateView):
    login_url = '/login/'
    redirect_field_name = 'routines/routine_detail.html'

    form_class = RoutineForm

    model = Routine

class RoutineDeleteView(DeleteView):
    model = Routine

    success_url = reverse_lazy('routines:routine_list')

class CreateExerciseView(CreateView):
    redirect_field_name = 'routines/routine_list.html'

    form_class = ExerciseForm

    model = Exercise

class ExerciseUpdateView(UpdateView):
    login_url = '/login/'
    redirect_field_name = 'routines/routine_detail.html'

    form_class = ExerciseForm

    model = Exercise

class ExerciseDeleteView(DeleteView):
    model = Exercise

    success_url = reverse_lazy('routines:routine_list')
