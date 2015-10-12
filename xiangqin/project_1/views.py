from django.shortcuts import render


# Create your views here.

def test(request) :
	context_dict = {}
	return render(request, 'project_1/test.html')
