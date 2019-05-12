from django.urls import include, path

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('pigeonholeaction', views.PigeonholeActionView)

urlpatterns = [
	path('', include(router.urls)),
	path('notify/', views.NotifyProfessor), 
]