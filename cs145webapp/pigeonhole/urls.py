from django.urls import include, path

from rest_framework import routers

from . import views
from .views import PigeonholeCreateView, PigeonholeDeleteView, PigeonholeDetailView, OwnerAddView, OwnerUpdateView, OwnerDeleteView

router = routers.DefaultRouter()
router.register('pigeonholeaction', views.PigeonholeActionView)

urlpatterns = [
	path('', views.homepage, name = 'homepage'),
	path('notify/', views.NotifyProfessor),
	path('create-pigeonhole/', views.PigeonholeCreateView.as_view(), name = 'create-pigeonhole'),
	path('delete-pigeonhole/<int:pk>/', views.PigeonholeDeleteView.as_view(), name = 'delete-pigeonhole'),	
	path('add-owner/', views.OwnerAddView.as_view(), name = 'add-owner'),
	path('update-owner/<int:pk>/', views.OwnerUpdateView.as_view(), name = 'update-owner'),
	path('remove-owner/<int:pk>/', views.OwnerDeleteView.as_view(), name = 'remove-owner'),
]