from django.contrib import admin

from core.models import Vacancy


class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'updated_at']


admin.site.register(Vacancy, VacancyAdmin)