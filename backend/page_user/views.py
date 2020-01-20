from django.shortcuts import render
from django.views.generic import ListView
from .models import UserSecond,Statistic
from django.contrib.auth.models import User
from rest_framework import  serializers, viewsets

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view,renderer_classes

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = UserSecond
		fields = ['id','first_name', 'last_name', 'email', 'gender','ip_address']

class StatisticSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Statistic
		fields = ['id','date', 'user','page_views', 'clicks']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
	queryset = UserSecond.objects.all()
	serializer_class = UserSerializer
	renderer_classes = [JSONRenderer]

# ViewSets define the view behavior.
class StatisticViewSet(viewsets.ModelViewSet):
	renderer_classes = [JSONRenderer]
	queryset = Statistic.objects.all()[:10]
	serializer_class = StatisticSerializer

	def get_queryset(self):
		statistics = super().get_queryset()
		if 'user_id' in  self.request.GET:
			user_id = self.request.GET.get('user_id')
			user = UserSecond.objects.get(id=user_id)
			statistics = Statistic.objects.filter(user=user)
		if 'date1' in  self.request.GET and  'date2' in  self.request.GET:
			date1 = self.request.GET.get('date1')
			date2 = self.request.GET.get('date2')
			statistics = statistics.filter(date__range=[date1, date2])
		return  statistics

class UserList(mixins.ListModelMixin,
				  mixins.CreateModelMixin,
				  generics.GenericAPIView):
	queryset = UserSecond.objects.all()
	serializer_class = UserSerializer
	renderer_classes = [JSONRenderer]

	def get(self, request, *args, **kwargs):
		response = self.list(request, *args, **kwargs)
		context = []
		for user in response.data:
			statistic = Statistic.objects.filter(user_id=user.get("id"))
			statistic = statistic[len(statistic)-1]
			user['total_clicks'] = statistic.clicks
			user['total_page_views'] = statistic.page_views
			context.append(user)
		return Response(context)

@renderer_classes([JSONRenderer])
@api_view(['GET'])
def how_many_users(request):
	count = UserSecond.objects.all().count()
	context={"user_count":count,"paginate_by":50}
	return Response(context)