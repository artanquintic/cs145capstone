from django.urls import include, path

from rest_framework import routers

from . import views
from .views import PigeonholeDetailView, OwnerAddView, OwnerUpdateView, OwnerDeleteView

router = routers.DefaultRouter()
router.register('pigeonholeaction', views.PigeonholeActionView)

urlpatterns = [
	path('', views.homepage),
	path('notify/', views.NotifyProfessor),
	path('add-owner/<int:p_number>/', views.OwnerAddView.as_view(), name = 'add-owner'),
	path('update-owner/<int:p_number>/', views.OwnerUpdateView.as_view(), name = 'update-owner'),
	path('remove-owner/<int:p_number>/', views.OwnerDeleteView.as_view(), name = 'remove-owner'),
]