"""
we are creating a view named parse_resume_view that is decorated with csrf_exempt. 
This view takes a POST request with a file named resume as input. 
It then reads the file and passes it to the parse_resume function to parse the resume. 
The parsed data is then returned as a JSON response.


"""
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .parser import parse_resume

@csrf_exempt
def parse_resume_view(request):
    if request.method == 'POST' and request.FILES['resume']:
        resume = request.FILES['resume'].read().decode('utf-8')
        parsed_data = parse_resume(resume)
        return JsonResponse(parsed_data, status=200)
    return JsonResponse({'error': 'Invalid Request'}, status=400)

