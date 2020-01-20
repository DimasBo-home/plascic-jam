# -*- coding:utf-8 -*-
"""page_user URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from .views import  how_many_users, UserViewSet, StatisticViewSet, UserList

from rest_framework import routers
# from .routes import api_router

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'statistic', StatisticViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/$',UserList.as_view()),
    url(r'^users/how-many/$',how_many_users),
    url(r'^api/', include(router.urls)),
]
