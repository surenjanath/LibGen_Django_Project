from django.http import request
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import os
from tempfile import NamedTemporaryFile

class DashboardView(View):
    def get(self, request):
        context = {}
        context['PAGE_TITLE'] = [x for x in 'LDP']
        return render(request, 'index.html', context=context)



@csrf_exempt
def download_with_progress(request):
    # Simulate a long-running download operation
    download_url = "https://www.africau.edu/images/default/sample.pdf"  # Replace with the actual download URL
    response = requests.get(download_url, stream=True)

    if response.status_code != 200:
        return JsonResponse({'error': 'Unable to download file'})

    file_size = int(response.headers.get('content-length', 0))
    progress = 0  # Initialize the progress variable

    def generate_file_chunks():
        progress = 0
        with NamedTemporaryFile(delete=False) as temp_file:
            for chunk in response.iter_content(chunk_size=1024):
                if not chunk:
                    break
                temp_file.write(chunk)
                yield chunk

                # Simulate progress update (you should replace this with actual progress tracking)
                progress += len(chunk)
                progress_percent = int((progress / file_size) * 100)
                data = {'progress': progress_percent}
                yield JsonResponse(data)

        # After the download is complete, return an empty JSON response to signal completion
        yield JsonResponse({})

    # Set response headers
    response = HttpResponse(generate_file_chunks(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="downloaded_file.pdf"'
    response['Content-Length'] = file_size
    print('Completed Download... ')
    return response
