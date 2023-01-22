from django.contrib import admin
from api.models import Country, State


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """ admin's Country """

    list_display = ('name', 'code')


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    """ admin's State """

    list_display = ('name', 'code')

