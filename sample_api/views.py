# --*-- coding: utf-8  --*--

import json
import collections
from sample_api import common


from .models import User, Entry, Affi
from .serializer import UserSerializer, EntrySerializer, AffiSerializer
from .affiliate import SearchKeyword
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse


def affi_list(request):

    if "keyword" in request.GET:
        # query_paramが指定されている場合の処理
        keyword = request.GET.get("keyword")
    else:
        # query_paramが指定されていない場合の処理
        return HttpResponse('<h1>Param Not Found</h1>')

    amazon = SearchKeyword.get_amazon('self', keyword)
    yahoo = SearchKeyword.get_yahoo('self', keyword)
    itunes = SearchKeyword.get_itunes('self', keyword)


    chain_map = collections.ChainMap(amazon, yahoo, itunes)
    url_list = dict(chain_map)

    if "sort" in request.GET:
        sort = request.GET.get("sort")
        contents = common.sort(url_list, sort)
    else:
        contents = common.sort(url_list, "Default")

    res = json.dumps(contents, ensure_ascii=False)
    return HttpResponse(res)


def amazon_list(request):

    if "keyword" in request.GET:
        # query_paramが指定されている場合の処理
        keyword = request.GET.get("keyword")
    else:
        # query_paramが指定されていない場合の処理
        return HttpResponse('<h1>Param Not Found</h1>')

    result = SearchKeyword.get_amazon('self', keyword)
    res = json.dumps(result, ensure_ascii=False)
    return HttpResponse(res)

def yahoo_list(request):

    if "keyword" in request.GET:
        # query_paramが指定されている場合の処理
        keyword = request.GET.get("keyword")
    else:
        # query_paramが指定されていない場合の処理
        return HttpResponse('<h1>Param Not Found</h1>')

    result = SearchKeyword.get_yahoo('self', keyword)
    res = json.dumps(result, ensure_ascii=False)
    return HttpResponse(res)

def itunes_list(request):

    if "keyword" in request.GET:
        # query_paramが指定されている場合の処理
        keyword = request.GET.get("keyword")
    else:
        # query_paramが指定されていない場合の処理
        return HttpResponse('<h1>Param Not Found</h1>')

    result = SearchKeyword.get_itunes('self', keyword)
    res = json.dumps(result, ensure_ascii=False)
    return  HttpResponse(res)



# 以降今回のAPIには関係ない

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
