from django.db import models

from accounts.models import Profile

CATEGORY = (
    ('IT', 'IT'),
    ('DESIGN', 'Дизайн'),
    ('MANAGEMENT', 'Менеджмент'),
    ('MEDICINE', 'Медицина'),
    ('ENGINEERING', 'Инженерное дело'),
    ('ART', 'Искусство'),
    ('TRANSPORT', 'Транспорт'),
    ('MARKETING', 'Маркетинг'),
    ('TRADE', 'Торговля'),
    ('ECONOMY', 'Экономика')
)


class Vacancy(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название вакансии', null=False, blank=False)
    salary = models.DecimalField(verbose_name='Заработная плата', decimal_places=1, max_digits=10, null=False,
                                 blank=False)
    author = models.ForeignKey(Profile, verbose_name='Работодатель', on_delete=models.CASCADE)
    description = models.TextField(max_length=3000, verbose_name='Описание вакансии', null=False, blank=False)
    experience = models.FloatField(verbose_name='Опыт работы', null=False, blank=False)
    category = models.TextField(verbose_name='Категория вакансии', null=False, blank=False, choices=CATEGORY)
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')
    is_active = models.BooleanField(verbose_name='Скрыть вакансию', default=False)

