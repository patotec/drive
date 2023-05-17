from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import *
from .forms import *
from django.contrib import messages
from user.models import Plan
from django.core.mail import EmailMessage
from django.conf import settings


def myindex(request):
	qs = Plan.objects.all()
	qs2 = Review.objects.all()
	context = {'inv':qs,'rev':qs2}
	return render(request, 'index/index.html',context)

def myapp(request):
	return render(request, 'index/app.html')


def mycontact(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		name = request.POST.get('name')
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		cre = Contact.objects.create(email=email,name=name,subject=subject,message=message)
		msg = EmailMessage('support', cre.email  +  "wants ur help  " + cre.message ,
		settings.DEFAULT_FROM_EMAIL,['hanspilgaard01@gmail.com'],)
		msg.send()
		messages.success(request, 'Thanks for your message we will repyl you shortly')
	return render(request, 'index/contact.html')

def myabout(request):
	return render(request, 'index/about.html')
def myse(request):
	qs = Plan.objects.all()
	qs2 = Review.objects.all()
	context = {'inv':qs,'rev':qs2}
	return render(request, 'index/service.html',context)
def myfunding(request):
	return render(request, 'index/funding-methods.html')
def myplat(request):
	return render(request, 'index/platform.html')
def mypoli(request):
	return render(request, 'index/policies.html')
def myref(request):
	return render(request, 'index/refferal.html')
def mytrade(request):
	return render(request, 'index/trading-assets.html')
def mywith(request):
	return render(request, 'index/withdrawals-methods.html')
def myadvan(request):
	return render(request, 'index/our-advantages.html')