from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView


from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView

from .models import Owner,Pigeonhole,PigeonholeAction
from .serializers import PigeonholeActionSerializer

# Create your views here.
context = {
	'pigeonhole' : Pigeonhole.objects.all(),
	'owner': Owner.objects.all(),
}

def homepage(request):
	return render(request, 'pigeonhole/home.html', context)

def NotifyProfessor(request):
	#send_mail(subject, message, from_email, to_list, fail_silently=True, )
	subject = 'Pigeonhole Principle'
	message = 'Student' + ' sent you something.'
	from_email = settings.EMAIL_HOST_USER
	to_list = ['clvillamera@up.edu.ph']
	

	send_mail(subject, message, from_email, to_list, fail_silently=True)	
	return HttpResponse('HELLO')

class PigeonholeActionView(viewsets.ModelViewSet):
	queryset = PigeonholeAction.objects.all()
	serializer_class = PigeonholeActionSerializer

class PigeonholeDetailView(DetailView):
	model = Pigeonhole
 
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['owner'] = Owner.objects.filter(pigeonhole = Pigeonhole('p_number'))
		return context

class OwnerAddView(CreateView):
	template_name = 'pigeonhole/add_owner.html'
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