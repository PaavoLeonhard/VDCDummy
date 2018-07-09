from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('patient', views.patient, name='patient'),
    path('exam', views.exam, name='exam'),
    path('behaviour', views.behaviour, name='behaviour'),
    path('find', views.find, name='find')

]


