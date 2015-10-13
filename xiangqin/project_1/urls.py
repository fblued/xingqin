from django.conf.urls import patterns, include, url
from project_1 import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xiangqin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^test/$', views.test, name='test'),
    url(r'^test2/$', views.test2, name='test2'),
    url(r'^test3/$', views.test3, name='test3'),
)