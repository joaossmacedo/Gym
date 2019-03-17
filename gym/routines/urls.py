"""routines URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'routines'

urlpatterns = [
    path('', views.RoutineListView.as_view(), name='routine_list'),
    path('<int:pk>/', views.RoutineDetailView.as_view(), name='routine_detail'),
    path('new/', views.CreateRoutineView.as_view(), name='routine_new'),
    path('<int:pk>/edit/', views.RoutineUpdateView.as_view(), name='routine_edit'),
    path('<int:pk>/remove/', views.RoutineDeleteView.as_view(), name='routine_remove'),
    path('new_exercise/', views.CreateExerciseView.as_view(), name='exercise_new'),
    path('exercise/<int:pk>/edit/', views.ExerciseUpdateView.as_view(), name='exercise_edit'),
    path('exercise/<int:pk>/remove/', views.ExerciseDeleteView.as_view(), name='exercise_remove'),
]
