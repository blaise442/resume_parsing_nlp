"""
we will define the URL patterns for the parse_resume view. 
"""
from django.urls import path
from .views import parse_resume_view
from django.contrib import admin
from django.urls import  include

urlpatterns = [
    path('parse_resume/', parse_resume_view, name='parse_resume'),
    path('admin/', admin.site.urls),
    path('', include('resume_app.urls')),
]
