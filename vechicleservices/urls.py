"""vechicleservices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import  include, url,patterns
from vechicle.views import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()
urlpatterns = [
	url(r'^login/$',TemplateView.as_view(template_name ='login.html')),
	url(r'^logout/$',logout,name='logout'),
	url(r'^searchlogin/$',searchlogin,name='searchlogin'),
	url(r'^home/$',TemplateView.as_view(template_name ='index.html')),
	url(r'^register/$',TemplateView.as_view(template_name ='index.html')),
	url(r'^adminhome/$',TemplateView.as_view(template_name ='adminhome.html')),
	url(r'^userhome/$',TemplateView.as_view(template_name ='userhome.html')),
	url(r'^mechanic/$',TemplateView.as_view(template_name ='addmechanic.html')),
	url(r'^vehicle/$',TemplateView.as_view(template_name ='addvehicle.html')),
	url(r'^customerhome/$',TemplateView.as_view(template_name ='customerhome.html')),
	url(r'^services/$',TemplateView.as_view(template_name ='services.html')),
	
	url(r'^$',TemplateView.as_view(template_name ='index.html')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^userinsert/$',userinsert,name='userinsert'),
	url(r'^serviceadviser/$',serviceadviser,name='serviceadviser'),
	url(r'^vmech/$',vmech,name='vmech'),
	url(r'^delmech/$',delmech,name='delmech'),
	url(r'^vuser/$',vuser,name='vuser'),
	url(r'^deluser/$',deluser,name='deluser'),
	url(r'^vehaction/$',vehaction,name='vehaction'),
	url(r'^vvehicles/$',vvehicles,name='vvehicles'),
	url(r'^vservices/$',vservices ,name='vservices'),
	url(r'^servicedone/$',servicedone,name='servicedone'),
	url(r'^aservice/$',aservice,name='aservice'),
	url(r'^rservice/$',rservice,name='rservice'),
	
	url(r'^vehdelete/$',vehdelete,name='vehdelete'),
		
	url(r'^servicedoneaction/$',servicedoneaction,name='servicedoneaction'),
	url(r'^vservicedoneadmin/$',vservicedoneadmin,name='vservicedoneadmin'),
	url(r'^serviceaction/$',serviceaction,name='serviceaction'),
	url(r'^pay/$',pay,name='pay'),
	url(r'^serviceadviserinsert/$',serviceadviserinsert,name='serviceadviserinsert'),

	url(r'^servicedone/$',servicedone,name='servicedone'),
	url(r'^vservicesuser/$',vservicesuser,name='vservicesuser'),
	url(r'^viewvehbookings/$',viewvehbookings,name='viewvehbookings'),
	url(r'^booking/$',booking,name='booking'),
	url(r'^bookaction/$',bookaction,name='bookaction'),
	url(r'^payment/$',payment,name='payment'),
	url(r'^paymentaction/$',paymentaction,name='paymentaction'),
	url(r'^payaction/$',payaction,name='payaction'),
	url(r'^assigninsert/$',assigninsert,name='assigninsert'),
	url(r'^vservices1/$',vservices1 ,name='vservices1'),
	
	]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns() 