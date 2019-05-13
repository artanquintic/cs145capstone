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

def FinderPigeonhole(owner, pholeaction_idNo):
	for i in range(0, owner.count()):
		if owner[i].idNo == pholeaction_idNo:
			return i
	return False		

class PigeonholeActionList(APIView):
	def get(self, request):
		pigeonholeaction = PigeonholeAction.objects.all().filter(emailed=False)
		pigeonhole = Pigeonhole.objects.all()
		owner = Owner.objects.all()
		serializer = PigeonholeActionSerializer(pigeonholeaction, many=True)

		for i in range(0,pigeonholeaction.count()):
			to_list = []
			to_list.append(owner[serializer.data[i]['p_number']-1].email)
			
			# If the Professor taps on his/her pigeonhole to get the things on it
			if FinderPigeonhole(owner,serializer.data[i]['id_number']) != False:
				if owner[FinderPigeonhole(owner,serializer.data[i]['id_number'])].pigeonhole.p_number == serializer.data[i]['p_number']:
					prof_get = Pigeonhole.objects.get(p_number=serializer.data[i]['p_number'])
					prof_get.item = False			# Empty the pigeonhole
					prof_get.save()
					continue

			if serializer.data[i]['name'] == None:
				message = "A student put something on your pigeonhole."
			else:
				message = str(serializer.data[i]['name']) + " put something on your pigeonhole."
			#NotifyProfessor(request, message, to_list)
			#print(pigeonholeaction[i].emailed)	
			#pigeonholeaction[i].emailed = True
			#pigeonholeaction[i].save()	


		return Response(serializer.data)
	
	def post(self, request):
		serializer = PigeonholeActionSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)		

def NotifyProfessor(request, message, to_list):
	#send_mail(subject, message, from_email, to_list, fail_silently=True, )
	subject = 'Pigeonhole Principle'
	from_email = settings.EMAIL_HOST_USER
	

	send_mail(subject, message, from_email, to_list, fail_silently=True)	
	#return HttpResponse('HELLO')

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