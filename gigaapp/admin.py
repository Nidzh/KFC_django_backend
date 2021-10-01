from django.contrib import admin
from django_filters import widgets
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

from .models import *


class VolunteerResource(resources.ModelResource):
    uid = Field(attribute='uid', column_name='ID в BotMother')
    name = Field(attribute='name', column_name='Имя')
    surname = Field(attribute='surname', column_name='Фамилия')
    email = Field(attribute='email', column_name='Email')
    phone = Field(attribute='phone', column_name='Телефон')
    city = Field(attribute='city', column_name='Город')
    company = Field(attribute='company', column_name='Компания')
    position = Field(attribute='position', column_name='Должность')
    competence__competence_name = Field(attribute='competence__competence_name', column_name='Выбранная компетенция')
    resource__course = Field(attribute='resource__course', column_name='Направление волонетрской деятельности')
    myfield = Field(column_name='-------------')

    contacts_city = Field(attribute='contacts', column_name='Контакты лидеров: Город',
                    widget=ManyToManyWidget(Contact, field='city', separator='\n'))
    contacts_leader_name = Field(attribute='contacts', column_name='Контакты лидеров: Имя лидера',
                     widget=ManyToManyWidget(Contact, field='leader_name', separator='\n'))
    contacts_company = Field(attribute='contacts', column_name='Контакты лидеров: Компания',
                    widget=ManyToManyWidget(Contact, field='company', separator='\n'))
    contacts_position = Field(attribute='contacts', column_name='Контакты лидеров: Должность',
                    widget=ManyToManyWidget(Contact, field='position', separator='\n'))
    contacts_phone = Field(attribute='contacts', column_name='Контакты лидеров: Телефон',
                    widget=ManyToManyWidget(Contact, field='phone', separator='\n'))
    contacts_email = Field(attribute='contacts', column_name='Контакты лидеров: Email',
                    widget=ManyToManyWidget(Contact, field='email', separator='\n'))


    class Meta:
        model = Volunteer
        skip_unchanged = True
        report_skipped = True
        fields = ('uid', 'name', 'surname', 'email', 'phone', 'city', 'company', 'position',
                  'competence__competence_name', 'resource__course', 'contacts_city', 'contacts_leader_name',
                  'contacts_company', 'contacts_position', 'contacts_phone', 'contacts_email')


class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact
        skip_unchanged = True
        report_skipped = True


class CompetenceResource(resources.ModelResource):
    class Meta:
        model = Competence
        skip_unchanged = True
        report_skipped = True


class ResourceResource(resources.ModelResource):
    class Meta:
        model = Resource
        skip_unchanged = True
        report_skipped = True


class CuratorResource(resources.ModelResource):
    class Meta:
        model = Curator
        skip_unchanged = True
        report_skipped = True


class VolunteerAdmin(ImportExportModelAdmin):
    list_display = ('uid', 'name', 'surname', 'city', 'email', 'phone', 'company',
                    'position', 'consent',)
    resource_class = VolunteerResource
    list_display_links = ('uid', 'name', 'surname',)
    search_fields = ('name', 'surname', 'city', 'company')
    list_filter = ('city', 'company')


class CompetenceAdmin(ImportExportModelAdmin):
    list_display = ('competence_name', 'box1', 'box2')
    resource_class = CompetenceResource


class ResourceAdmin(ImportExportModelAdmin):
    list_display = ('course', 'contact')
    resource_class = ResourceResource
    list_display_links = ('course', 'contact')
    search_fields = ('course', 'contact')


class CuratorAdmin(ImportExportModelAdmin):
    list_display = ('city', 'course', 'contact')
    resource_class = CuratorResource
    list_display_links = ('city', 'course', 'contact')
    search_fields = ('city', 'course', 'contact')


class ContactAdmin(ImportExportModelAdmin):
    resource_class = ContactResource
    list_display = ('city', 'company', 'leader_name', 'position', 'phone', 'email')
    list_filter = ('company', 'city')
    list_display_links = ('city', 'leader_name', 'company')
    search_fields = ('city', 'company', 'leader_name')


admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Competence, CompetenceAdmin)
admin.site.register(Curator, CuratorAdmin)
admin.site.register(Resource, ResourceAdmin)
