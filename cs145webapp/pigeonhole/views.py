from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status

import io

from .models import Owner,Pigeonhole,PigeonholeAction
from .serializers import PigeonholeActionSerializer

# Create your views here.
context = {
	'pigeonhole' : Pigeonhole.objects.all().order_by('p_number'),
	'owner': Owner.objects.all(),
}

def homepage(request):
	context = {
		'pigeonhole' : Pigeonhole.objects.all().order_by('p_number'),
		'owner': Owner.objects.all(),
	}
	return render(request, 'pigeonhole/home.html', context)

# For the ID/Student Number of the tapper check if it a student/prof
def FinderPigeonhole(owner, pholeaction_idNo):
	for i in range(0, owner.count()):
		if owner[i].idNo == pholeaction_idNo:
			return i
	return False		

# Returning the owner itself, based on the phole number
def ReturnPigeonhole(owner, pholeaction_number):
	for i in range(0, owner.count()):
		if owner[i].pigeonhole.p_number == pholeaction_number:
			return owner[i]
	return False		

class PigeonholeActionList(APIView):
	def get(self, request):
		return Response(serializer.data)
	
	def post(self, request):
		serializer = PigeonholeActionSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			NotifyProfessor(request, serializer)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)		


def NotifyProfessor(request, serializer):
	pigeonhole = Pigeonhole.objects.all()
	owner = Owner.objects.all()

	to_list = []
	to_list.append(ReturnPigeonhole(owner, serializer.data['p_number']).email)
			
	# If the Professor taps on his/her pigeonhole to get the things on it
	if FinderPigeonhole(owner,serializer.data['id_number']) != False:
		if owner[FinderPigeonhole(owner,serializer.data['id_number'])].pigeonhole.p_number == serializer.data['p_number']:
			prof_get = Pigeonhole.objects.get(p_number=serializer.data['p_number'])
			prof_get.item = False			# Empty the pigeonhole
			prof_get.save()
			return

	pigeonhole_status = Pigeonhole.objects.get(p_number=serializer.data['p_number'])
	pigeonhole_status.item = True
	pigeonhole_status.save()

	if serializer.data['name'] == 'NULL':
		message = "A student put something on your pigeonhole."
	else:
		message = str(serializer.data['name']) + " put something on your pigeonhole."
		
	
	subject = 'Smart Pigeonhole'
	from_email = settings.EMAIL_HOST_USER
	

class PigeonholeCreateView(CreateView):
	model = Pigeonhole
	fields = ['p_number']

	def form_valid(self, form):
		return super().form_valid(form)


class PigeonholeDeleteView(DeleteView):
	model = Pigeonhole
	success_url = '/'

	def test_func(self):
		pigeonhole = self.get_object()
		return True

class PigeonholeDetailView(DetailView):
	model = Pigeonhole
 
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['owner'] = Owner.objects.filter(pigeonhole = Pigeonhole('p_number'))
		return context

class OwnerAddView(CreateView):
	model = Owner
	fields = ['pigeonhole', 'name', 'email', 'idNo']

	def form_valid(self, form):
		return super().form_valid(form)


class OwnerUpdateView(UpdateView):
	model = Owner
	fields = ['pigeonhole', 'name', 'email', 'idNo']

	def form_valid(self, form):
		return super().form_valid(form)

class OwnerDeleteView(DeleteView):
	model = Owner
	success_url = '/'

	def test_func(self):
		owner = self.get_object()
		return True