# -*- coding:utf-8 -*-
from django.db import models

class UserSecond(models.Model):
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	id = models.PositiveIntegerField(primary_key=True)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	gender = models.CharField(null=True,blank=True,max_length=1,verbose_name = "Стать",choices=GENDER_CHOICES)
	ip_address = models.GenericIPAddressField(null=True,blank=True,verbose_name = "ip адреса")

	def __str__(self):
		return self.first_name

	def get_gender(self):
		return self.GENDER_CHOICES[self.gender]

class Statistic(models.Model):
	user = models.ForeignKey(UserSecond,on_delete=models.CASCADE,)
	date = models.DateField()
	page_views = models.PositiveIntegerField()
	clicks = models.PositiveIntegerField()

	def __str__(self):
		return self.user.first_name
	class Meta:
		ordering = ["date"]
	# def user_name(self]):
	# 	return self.user.first_name
