# -*- coding:utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import  Statistic, UserSecond

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
	list_display = ('id','__str__', 'date','page_views','clicks')	

@admin.register(UserSecond)
class UserSecondAdmin(admin.ModelAdmin):
	list_display = ('id','first_name', 'last_name','email','gender','ip_address')	
