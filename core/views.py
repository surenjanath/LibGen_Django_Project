from django.http import request
from django.shortcuts import render
from django.views import View



class DashboardView(View):
    def get(self, request):
        return render(request, 'index.html')
