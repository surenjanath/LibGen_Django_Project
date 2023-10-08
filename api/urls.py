# -*- encoding: utf-8 -*-


from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path



urlpatterns = [
    path('search-results/', views.SearchResultListCreateView.as_view(), name='search-result-list'),
    path('search-queries/', views.SearchQueryListCreateView.as_view(), name='search-query-list'),

]
urlpatterns = format_suffix_patterns(urlpatterns)
