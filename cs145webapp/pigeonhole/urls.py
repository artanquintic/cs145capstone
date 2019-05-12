from django.urls import include, path

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import PigeonholeActionList, PigeonholeDetailView, OwnerAddView, OwnerUpdateView, OwnerDeleteView

#router = routers.DefaultRouter()
#router.register('pigeonholeaction', views.PigeonholeActionList)

urlpatterns = [
	path('', views.homepage),
	path('notify/', views.NotifyProfessor),
	path('add-owner/<int:p_number>/', views.OwnerAddView.as_view(), name = 'add-owner'),
	path('update-owner/<int:p_number>/', views.OwnerUpdateView.as_view(), name = 'update-owner'),
	path('remove-owner/<int:p_number>/', views.OwnerDeleteView.as_view(), name = 'remove-owner'),
	path('sending/', views.PigeonholeActionList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)