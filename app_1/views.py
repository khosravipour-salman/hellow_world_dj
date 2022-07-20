from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail



def index(request):
	if request.method == 'POST':
		send_mail('this is not a subject',
			    'this is my messageeeee',
			    'mailserver.django@gmail.com',
			    ['salmankhosravipour2015@gmail.com'],
		)

	return render(request, 'app_1/test.html')


def index2(request):
	# bademjoon = request.GET.get('name')
	return render(request, 'app_1/test1.html',)


def user_profile(request):
	return HttpResponse('usre_profile it isss')
# settings.py --> TEMPLATES --> TEMPLATES_DIR --> template
# app dir     --> templates --> <app_name> 
