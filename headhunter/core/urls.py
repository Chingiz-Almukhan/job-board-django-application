from django.urls import path

from core.views.base import IndexView
from core.views.vacancy import VacancyCreate, VacancyUpdate, VacancyDetail, vacancy_reload

urlpatterns = [
    path('', IndexView.as_view(), name='main'),

    path('vacancy/create', VacancyCreate.as_view(), name='vacancy_create'),
    path('vacancy/update/<int:pk>', VacancyUpdate.as_view(), name='vacancy_update'),
    path('vacancy/<int:pk>', VacancyDetail.as_view(), name='vacancy_detail'),
    path('vacancy/reload/<int:pk>', vacancy_reload, name='reload'),
]
