# --*-- coding: utf-8  --*--

import json
import django_filters

from .models import User, Entry, Affi
from .serializer import UserSerializer, EntrySerializer, AffiSerializer
from sample_api.affiliate import SearchKeyword
from rest_framework import viewsets, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse


def amazon_list(request):

    #検索キーワード設定（get値からなど）※今回は固定
    keyword = 'iphone'

    result = SearchKeyword.get_amazon('self', keyword)
    return HttpResponse(result)

def yahoo_list(request):

    #検索キーワード設定（get値からなど）※今回は固定
    keyword = 'iphone'

    result = SearchKeyword.get_yahoo('self', keyword)
    return HttpResponse(result)

def itunes_list(request):

    #検索キーワード設定（get値からなど）※今回は固定
    keyword = 'iphone'

    result = SearchKeyword.get_itunes('self', keyword)
    return  HttpResponse(result)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class AffiViewSet():

    queryset = Affi.objects.all()
    serializer_class = AffiSerializer


    @api_view(['GET', 'POST'])
    def get(self, request, format=None):

        sample = Affi.objects.all()
        serializer = AffiSerializer(sample, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = AffiSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
