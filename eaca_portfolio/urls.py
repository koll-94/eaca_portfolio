# -*- coding: utf-8 -*-
"""test_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^$', views.LoginFormView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^main/$', views.main),
    url(r'^grid_document/([0-9]*)$', views.grid_document),
    url(r'^form_document/([0-9]*)/$', views.form_document),
    url(r'^save_document/([0-9]*)/([0-9]*)$', views.save_document),
    url(r'^delete_document/([0-9]*)/([0-9]*)$', views.delete_document),
    url(r'^main_correct/$', views.main_correct),
]

