from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from project_1.models import Female
from project_1.models import Man


# Create your views here.

def test(request) :
	context_dict = {}
	return render(request, 'project_1/test.html')

def test2(request):
	context_dict={}
	try:
		female = Female.objects.all()
		man = Man.objects.all()
		context_dict['female'] = female 
		context_dict['man'] = man 
	except Female.DoesNotExist:
		pass 

	return render_to_response( 'project_1/test2.html',context_dict)

