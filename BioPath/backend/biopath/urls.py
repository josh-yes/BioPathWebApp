"""
File: urls.py
Description: Defines urls to views. This is the project urls.py which just map admin
    and api to the urls.py at backend/api/urls.py.
Modified: 11/17 - Josh Schmitz
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(route='admin/', view=admin.site.urls),
    path(route='api/', view=include('api.urls')), # this essentially just includes the urls from api/urls.py

]
