from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def testing(request):
	return HttpResponse('HELL')

def NotifyProfessor(request):
	#send_mail(subject, message, from_email, to_list, fail_silently=True, )
	subject = 'Pigeonhole Principle'
	message = 'Student' + ' sent you something.'
	from_email = settings.EMAIL_HOST_USER
	to_list = ['clvillamera@up.edu.ph']
	send_mail(subject, message, from_email, to_list, fail_silently=True)	
	return HttpResponse('HELLO')