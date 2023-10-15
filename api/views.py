# -*- encoding: utf-8 -*-

from django.http import JsonResponse
from rest_framework import status, filters, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from django.utils.datastructures import MultiValueDict
from django.utils.datastructures import MultiValueDictKeyError

from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist



from django.views.decorators.csrf import csrf_exempt
from .Functions import LibgenScraper, GET_DOWNLOADLINK
import requests
#----------------------------------------------------
# INTERNAL CALLS
#----------------------------------------------------

from rest_framework import generics
from .models import Search_Results, Search_Query
from .serializers import *

class Search_ResultsListCreateView(generics.ListCreateAPIView):
    queryset = Search_Results.objects.all()
    serializer_class = Search_ResultsSerializer

class Search_QueryListCreateView(generics.ListCreateAPIView):
    queryset = Search_Query.objects.all()
    serializer_class = Search_QuerySerializer


@csrf_exempt  # For demonstration purposes; use proper CSRF protection
def scrape_and_populate(request):
    if request.method == 'POST':
        Search_Query.objects.all().delete()
        query = request.POST.get('query', '')  # Get the query from the frontend
        if query != '':
            # Record the search query and increment its count
            query_obj, created = Search_Query.objects.get_or_create(query=query.upper())
            query_obj.count += 1
            query_obj.save()

        # Initialize a session and headers for scraping (you may need to adjust these)
        session = requests.Session()
        headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            }

        # Call your scraping function
        scraping_result = LibgenScraper(session,query=query, headers=headers)
        print(scraping_result)
        if scraping_result['status'] == '200':
            # If scraping was successful, populate the database
            results = scraping_result['results']
            Search_Results.objects.all().delete()
            print(results)
            for result in results:
                search_instance = Search_Results(
                    md5_id      =   result['md5_ID'],
                    searchquery =   query_obj,
                    title       =   result['Title'],
                    link        =   result['Link'],
                    author      =   result['Author(s)'],
                    publisher   =   result['Publisher'],
                    year        =   result['Year'],
                    pages       =   result['Pages'],
                    language    =   result['Language'],
                    size        =   result['Size'],
                    extension   =   result['Extension'],
                )
                search_instance.save()
            # # Optionally, call another function to get download links
            # md5_ids = [result['md5_ID'] for result in results]
            # download_links = GET_DOWNLOADLINK(session, md5_ids, headers)

            # Return a JSON response with the scraping and database population results
            return JsonResponse({
                'status': 'success',
                'message': 'Data successfully scraped and populated to the database',
                # 'download_links': download_links,
            })

        # Handle other status codes (e.g., 403, 402, 404) and return appropriate responses

    # Handle invalid or non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})