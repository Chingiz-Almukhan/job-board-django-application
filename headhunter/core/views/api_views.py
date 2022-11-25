from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from core.models import Vacancy


def vacancy_list_view(request, *args, **kwargs):
    if request.method == "GET":
        search = request.GET.get('search')
        vacancy = Vacancy.objects.filter(name__icontains=search) if search else Vacancy.objects.all()
        return JsonResponse(list(vacancy.values(*('id', 'name', 'salary', 'author', 'updated_at', 'category'))), safe=False)
