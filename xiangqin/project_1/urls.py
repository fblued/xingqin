from django.conf.urls import patterns, include, url
from project_1 import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xiangqin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^test/$', views.test, name='test'),
)