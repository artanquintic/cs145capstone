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

class PigeonholeActionList(APIView):
	def get(self, request):
		pigeonholeaction = PigeonholeAction.objects.all().filter(emailed=False)
		owner = Owner.objects.all()
		serializer = PigeonholeActionSerializer(pigeonholeaction, many=True)

		print(owner[0].email)
		for i in range(0,pigeonholeaction.count()):
			print(serializer.data[i]['p_number'])

		return Response(serializer.data)
	
	def post(self):
		pass	

def NotifyProfessor(request, to_list):
	#send_mail(subject, message, from_email, to_list, fail_silently=True, )
	subject = 'Pigeonhole Principle'
	message = 'Student' + ' sent you something.'
	from_email = settings.EMAIL_HOST_USER
	to_list = ['clvillamera@up.edu.ph']
	

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