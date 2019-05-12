from django.urls import include, path

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('pigeonholeaction', views.PigeonholeActionView)

urlpatterns = [
	path('', views.testing),
	path('notify/', views.NotifyProfessor),
	path('add-owner/', views.OwnerCreateView),
	path('update-owner/', views.OwnerUpdateView),
	path('remove-owner/', views.OwnerDeleteView),
]