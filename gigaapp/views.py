from .models import *
from rest_framework import generics
from .serializers import *
from rest_framework.exceptions import ValidationError
from .constants import list_of_moscow_area


class ContactViewSet(generics.ListAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        queryset = Contact.objects.all()
        city = self.request.query_params.get('city')
        company = self.request.query_params.get('company')

        if city is not None and company is None:
            city = city.capitalize()
            if city in list_of_moscow_area:
                city = 'Московская область'

            queryset = queryset.filter(city=city)

            if not queryset.exists():
                raise ValidationError(detail='Город не найден')

        elif city and company is not None:
            city = city.capitalize()
            if city in list_of_moscow_area:
                city = 'Московская область'
            queryset_city = queryset.filter(city=city)
            queryset_company = queryset.filter(company=company)

            if not queryset_city.exists():
                raise ValidationError(detail='Город не найден')
            elif not queryset_company.exists():
                queryset = queryset.filter(city=city)
            else:
                queryset = queryset.filter(city=city, company=company)

            if not queryset.exists():
                raise ValidationError(detail='Город не найден')

        return queryset


class CompetenceViewSet(generics.ListAPIView):
    serializer_class = CompetenceSerializer

    def get_queryset(self):
        queryset = Competence.objects.all()
        competence_name = self.request.query_params.get('competence_name')
        if competence_name is not None:
            queryset = queryset.filter(competence_name=competence_name)

            if not queryset.exists():
                raise ValidationError(detail='Ошибка 400')

        return queryset


class ResourceViewSet(generics.ListAPIView):
    serializer_class = ResourceSerializer

    def get_queryset(self):
        queryset = Resource.objects.all()
        course = self.request.query_params.get('course')
        if course is not None:
            queryset = queryset.filter(course=course)

            if not queryset.exists():
                raise ValidationError(detail='Ошибка 400')

        return queryset


class CuratorViewSet(generics.ListAPIView):
    serializer_class = CuratorSerializer

    def get_queryset(self):
        queryset = Curator.objects.all()
        city = self.request.query_params.get('city')
        if city is not None:
            queryset = queryset.filter(city=city)

            if not queryset.exists():
                raise ValidationError(detail='Ошибка 400')

        return queryset


class VolunteerViewSet(generics.ListCreateAPIView):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer

class VolunteerUpdateViewSet(generics.RetrieveUpdateAPIView):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer


