from django.urls import path
from . import views

urlpatterns = [
	path('', views.testing),
	path('notify/', views.NotifyProfessor),
]