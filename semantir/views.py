from django.shortcuts import render
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import News


@api_view(['GET', 'POST'])
def my_api_view(request):
    data = {
        'text': 'Welcome to Semantir !'
    }
    return Response(data)


@api_view(['GET'])
def newslist_view(request):
    news = News.objects.all()
    serializer = TaskSerializer(news, many=True)

    return Response(serializer.data)
