from django.http import request
from django.shortcuts import render
from django.views import View



class DashboardView(View):
    def get(self, request):
        context = {}
        context['PAGE_TITLE'] = [x for x in 'LDP']
        return render(request, 'index.html', context=context)
