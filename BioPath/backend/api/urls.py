"""
File: serialzers.py
Description: Maps url endpoints to the viewsets in views.py. We are using DRF routers to
    abstract this so we can just deal with viewsets and not individual views. This helps
    insure CRUD compliance and means there's less code for us to write. Note that these 
    the given routes here are actually all prefixed with api/ as this file is routed to
    from the projects base urls.py in backend/biopath.
Modified: 11/17 - Josh Schmitz
"""

from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'enzymes', views.EnzymeViewSet, basename="enzymes")
router.register(r'molecules', views.MoleculeViewSet, basename="molecules")
router.register(r'pathways', views.PathwayViewSet, basename="pathways")
router.register(r'pathway_enzyme', views.PathwayEnzymeViewSet)
router.register(r'pathway_molecule', views.PathwayMoleculeViewSet)

urlpatterns = [
    path(route='', view=include(router.urls)),
    path(route='api-auth/', view=include('rest_framework.urls', namespace='rest_framework')),
]
