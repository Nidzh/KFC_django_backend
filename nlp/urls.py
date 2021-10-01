from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from gigaapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/contact/', ContactViewSet.as_view()),
    path('api/competence/', CompetenceViewSet.as_view()),
    path('api/curator/', CuratorViewSet.as_view()),
    path('api/resource/', ResourceViewSet.as_view()),
    path('api/volunteer/', VolunteerViewSet.as_view()),
    path('api/volunteer/update/<str:pk>', VolunteerUpdateViewSet.as_view()),
]

