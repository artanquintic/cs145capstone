from django.urls import path
from . import views

urlpatterns = [
	path('', views.testing),
	path('notify/', views.NotifyProfessor),
	path('add-owner/', views.OwnerCreateView),
	path('update-owner/', views.OwnerUpdateView),
	path('remove-owner/', views.OwnerDeleteView),
]