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


Mes = "%s;%s;%s;%s;%s;%s;%s;%s"

def requestInfo(request):
    if request.method == 'POST' :
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
            #print requestform
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
            return resInfo(request)

        else:
            print requestform.errors
    else:
        requestform = RequestForm()

    return render(request,'project_1/requestInfo.html',{'requestform':requestform})


#############################################################
AGES = {'a':(0,17),
    'b':(18,22),
    'c':(23,26),
    'd':(27,35),
    'e':(35,200), 
    }

EDUS={
    1:'初中',
    2:'高中',
    3:'大专',
    4:'大本',
    5:'硕士',
    6:'博士',
        }

def getAllObjects(P_require) :
    ''' P_require Each search condition to ';' Separated
        A total of 7 ';'  
        "sex;ages;height;weight;hometown;education;Occupation;aim"
         -- http://www.bing.com/translator/ '''

    Sel = 'SELECT * FROM project_1_UserProfile WHERE %s'
    req_list = P_require.split(';')
    res = ''
    if req_list[0] :
        res+='sex="%s" and ' % (req_list[0])
    if req_list[1] :
        res+='age >= %d and age <= %d and ' % (AGES[req_list[1]][0], AGES[req_list[1]][1])
            # can't use age in (%d,%d) 
    if req_list[2] :
        res += 'height>=%s and ' %(req_list[2])
    if req_list[3] :
        res += 'weight>=%s and ' %(req_list[3])
    if req_list[4] :
        res += 'hometown="%s" and ' % (req_list[4])
    if req_list[5] :
        res += 'education >= %s and ' % (req_list[5])
    if req_list[6] :
        res += 'Occupation="%s" and ' %(req_list[6])

    if not res.strip(): 
        # res is null or '' 
        res = '1 = 0 '
    else :
        res += '1 = 1'

    res = Sel % (res)
    ret = UserProfile.objects.raw(res)
    return ret  

def getResObjects(objs, src) :
    '''
    objs : The values found in the database contains 'require'
    xx.require : "sex;ages;height;weight;hometown;education;Occupation;aim"
    src : The values use found objs in the database 
    ret list 
    '''
    ret = []
    for obj in objs :
        req_list = obj.require.split(';')
        if req_list[0] and req_list[0] != src.sex:
            continue
        if req_list[1] and (src.age < AGES[req_list[1]][0] or src.age > AGES[req_list[1]][1]) :
            continue
        if req_list[2] and int(req_list[2]) > src.height:
            continue
        if req_list[3] and int(req_list[3]) > src.weight:
            continue
        if req_list[4] and req_list[4] != src.hometown :
            continue
        if req_list[5] and req_list[5] < int(src.education):
            continue
        if req_list[6] and  req_list[6] != src.Occupation:
            continue
        ret.append(obj)
        ret[len(ret)-1].education =  EDUS[ret[len(ret)-1].education]
    return ret 



#############################################################
def resInfo(request):
    '''
    if request.method == 'POST':
        print request.POST
    else:
        preUser = UserProfile.objects.get(OpenID=request.session.get('OpenID',False))
        getAllObjects(preUser.require)
        print "11111"
        return 
    '''
    preUser = UserProfile.objects.get(OpenID=request.session.get('OpenID',False))
    m_objects = getAllObjects(preUser.require)
    #print [x.name for x in m_objects]
    list_res = getResObjects(m_objects, preUser)
    return render(request,'project_1/resInfo.html',{'list_res':list_res})


"""
'''
        reqInfo = preUser.require
        print reqInfo
        
        req_list = reqInfo.split(';')
        sex = req_list[0]
        ages = req_list[1] 
        height = req_list[2]
        weight = req_list[3]
        hometown = req_list[4]
        education = req_list[5]
        Occupation = req_list[6]
        aim = req_list[7]
        '''
        '''
        list_res = []
        res_object = UserProfile.objects.filter(sex=sex)
        for res in res_object:
            reqInfo_other = res.require

            req_otherlist = reqInfo_other.split(';')

            oth_sex = req_otherlist[0]
            oth_ages = req_otherlist[1]
            oth_height = req_otherlist[2]
            oth_weight = req_otherlist[3]
            oth_hometown = req_otherlist[4]
            oth_education = req_otherlist[5]
            oth_Occupation = req_otherlist[6]
            oth_aim = req_otherlist[7]

            if oth_sex == preUser.sex:
                list_res.append(res)
    return render(request,'project_1/resInfo.html',{'list_res':list_res})
    '''
"""

def detail(request,detail_slug):
    context_dict = {}
    try:
        she_he = UserProfile.objects.get(OpenID=detail_slug)
        context_dict['she_he'] = she_he
    except UserProfile.DoseNotExist:
        pass
    return render(request,'project_1/detail.html',context_dict)
