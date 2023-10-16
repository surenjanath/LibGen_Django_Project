from django.http import request
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from api.models import Search_Results
from api.Functions import *

class DashboardView(View):
    def get(self, request):
        context = {}
        context['PAGE_TITLE'] = [x for x in 'LDP']
        return render(request, 'index.html', context=context)



@csrf_exempt
def download_with_progress(request):
    unique_id = request.GET.get("id")

    session = requests.Session()
    headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            }


    search_result = Search_Results.objects.get(uniqueId=unique_id)
    links = GET_DOWNLOADLINK(session, search_result.md5_id, headers)  # Call your GET_DOWNLOADLINK function
    print(links)
    if links :
        return  JsonResponse({
        'search_result_title': search_result.title,
        'download_links': links,
        })


    return JsonResponse({'error': 'Unable to fetch links'})

