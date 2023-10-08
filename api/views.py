# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from api.models import Tablet_Type, Tablet_Entry, Tablet_Comment, Wordpress_Creds, Tablet_Monthly_Analytics, Tablet_Daily_Analytics

from api.serializers import Tablet_TypeSerializer, Tablet_EntrySerializer, Tablet_CommentSerializer, Wordpress_CredsSerializer, Tablet_TypeNormSerializer, Tablet_EntryONLYSerializer, Tablet_Daily_AnalyticsSerializer, Tablet_Monthly_AnalyticsSerializer
from rest_framework import status, filters, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from django.utils.datastructures import MultiValueDict
from django.utils.datastructures import MultiValueDictKeyError

from django.forms.models import model_to_dict



from .models import Wordpress_Creds
from django.core.exceptions import ObjectDoesNotExist

#----------------------------------------------------
# INTERNAL CALLS
#----------------------------------------------------

from rest_framework import generics
from .models import SearchResult, SearchQuery
from .serializers import SearchResultSerializer, SearchQuerySerializer

class SearchResultListCreateView(generics.ListCreateAPIView):
    queryset = SearchResult.objects.all()
    serializer_class = SearchResultSerializer

class SearchQueryListCreateView(generics.ListCreateAPIView):
    queryset = SearchQuery.objects.all()
    serializer_class = SearchQuerySerializer