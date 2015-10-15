# coding:utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from project_1.forms import Register,RequestForm
from project_1.models import UserProfile
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

#from project_1.models import Female
#from project_1.models import Man


# Create your views here.

def test(request) :
	context_dict = {}
	return render(request, 'project_1/test.html')

def test2(request):
	context_dict={}
	try:
		'''
		female = Female.objects.all()
		man = Man.objects.all()
		context_dict['female'] = female 
		context_dict['man'] = man 
		'''

		userProfile = UserProfile.objects.all()
		context_dict['userProfile'] = userProfile
	except UserProfile.DoesNotExist:
		pass 

	return render_to_response( 'project_1/test2.html',context_dict)
'''
def test3(request) :
	if request.method == 'POST' :
		form = Register(request.POST)
		if form.is_valid() :
			form.save()
			print form.cleaned_data
			return render(request, 'project_1/test.html')
		else :
			print form.errors
	else :
		form = Register()
	return render(request, 'project_1/test3.html', {'form' : form})
'''

def test3(request) :
	if request.method == 'POST' :
		userform = Register(request.POST)
		#print request.POST
		if userform.is_valid() :
			userform.save()
#------------------------------------------------------------------------------
			request.session['OpenID'] = request.POST.get('OpenID')
#------------------------------------------------------------------------------

			#print userform.cleaned_data
			#return render(request,'project_1/test.html')
			#return HttpResponseRedirect('project_1/requestInfo.html')
			#return render_to_response('project_1/requestInfo.html')
			#return render(request,'project_1/requestInfo.html')
			#return HttpResponseRedirect()
			return render(request,'project_1/requestInfo.html',{'requestform':RequestForm()})
		else :
			print userform.errors
	else :
		userform = Register()
	return render(request,'project_1/test3.html', {'userform' : userform})

Mes = "sex:%s,ages:%s,height:%s,weight:%s,hometown:%s,education:%s,Occupation:%s,aim:%s"

def requestInfo(request):
    if request.method == 'POST' and request.POST.get('ages'):
        requestform = RequestForm(request.POST)
        if requestform.is_valid():
            #get infomation from POST
            sex = request.POST.get('sex',False)
            ages = request.POST.get('ages',False)
            height = request.POST.get('height',False)
            weight = request.POST.get('weight',False)
            hometown = request.POST.get('hometown',False)
            education = request.POST.get('education',False)
            Occupation = request.POST.get('Occupation',False)
            aim = request.POST.get('aim',False)
            #
            #info = sex + '_'+ages + '_'+height+'_'+weight+'_'+hometown+'_'+education+'_'+Occupation+'_'+aim
            info = Mes % (sex, ages,height,weight,hometown,education,Occupation,aim)
            #print info 
            #return 
            UserProfile.objects.filter(OpenID=request.session.get('OpenID',False)).update(require = info)

            #db = sqlite3.connect(user='itcast',db='db.sqlite3',password='123',charset='utf-8')
            #db = sqlite3.connect("../db.sqlite3")
            #cursor = connection.cursor()
            #cursor.execute("UPDATE UserProfile SET Require = info where OpenID='3333'")
            #cursor.execute("SELECT * FROM User")
           #transaction.commit_unless_managed()
            #db.close()
            return render_to_response('project_1/test.html')

        else:
            print requestform.errors
    else:
        requestform = RequestForm()

    return render(request,'project_1/requestInfo.html',{'requestform':requestform})


