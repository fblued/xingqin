#coding:utf-8
from django import forms
from django.contrib.auth.models import User
from project_1.models import UserProfile

SOURCES_CHOICES=(
	('m','boy'),
	('f','girl'),
	)

class Register(forms.ModelForm) :
	required_css_class = 'register'
	sex = forms.ChoiceField(label=("性别"), widget=forms.Select(), choices=SOURCES_CHOICES,
		initial=SOURCES_CHOICES[1])
	name = forms.CharField(label=("Username"), max_length=30, help_text=("Register"))
	car = forms.BooleanField(required=False,initial=True)
	OpenID = forms.CharField(label=("OpenID"), max_length =128)

	class Meta:
     		model = UserProfile



"""
'''
E = 'e'
A = 'a'
SOURCES_CHOICES = (
	(A, 'A'),
	(E, 'E'),
	)
'''
SOURCES_CHOICES = (
	('f', '女' ),
	('m', '男' ),
	)
	# (get value, show in page)


class Register(forms.Form) :
	required_css_class = 'register'
	username = forms.CharField(label=("Username"), max_length=30, help_text=("Register"))
	provider = forms.ChoiceField(widget=forms.Select(), choices=SOURCES_CHOICES,
		initial=SOURCES_CHOICES[1])
	car = forms.BooleanField(required=False)
"""

'''
error
FAVORITE_COLORS_CHOICES =({'sex' : 'f'}, {'sex' : 'm'})

class Register(forms.Form) :
	sex = forms.ChoiceField(label=u'FM',
		choices=FAVORITE_COLORS_CHOICES)
	name = forms.CharField(max_length=100)
'''