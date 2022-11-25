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
    salary = models.DecimalField(verbose_name='Заработная плата', decimal_places=0, max_digits=10, null=False,
                                 blank=False)
    author = models.ForeignKey(Profile, related_name='company', verbose_name='Работодатель', on_delete=models.CASCADE)
    description = models.TextField(max_length=3000, verbose_name='Описание вакансии', null=False, blank=False)
    experience = models.FloatField(verbose_name='Опыт работы', null=False, blank=False)
    category = models.TextField(verbose_name='Категория вакансии', null=False, blank=False, choices=CATEGORY)
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')
    is_active = models.BooleanField(verbose_name='Скрыть вакансию', default=False)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-updated_at']


class Resume(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название резюме', null=True, blank=True)
    category = models.TextField(verbose_name='Категория вакансии', choices=CATEGORY, null=True, blank=True)
    about = models.TextField(max_length=3000, verbose_name='О себе')
    salary = models.DecimalField(verbose_name='Желаемая зарплата', max_digits=10, decimal_places=2, null=True,
                                 blank=True)
    email = models.CharField(verbose_name='Email', max_length=100, null=True, blank=True)
    author = models.ForeignKey(Profile, verbose_name='Соискатель', on_delete=models.CASCADE)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=20, null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name='Последние изменение', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='Скрыть резюме', default=True)
    telegram = models.CharField(verbose_name='Ссылка на телеграм', max_length=100, null=True, blank=True)
    linkedin = models.CharField(verbose_name='Ссылка на Linkedin', max_length=100, null=True, blank=True)
    facebook = models.CharField(verbose_name='Ссылка на Facebook', max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.author}'


class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    study = models.CharField(max_length=100, verbose_name='Место обучения')
    start_date = models.DateField(blank=True, null=True, verbose_name='Начал обучаться')
    end_date = models.DateField(blank=True, null=True, verbose_name='Закончил обучаться')


class Job(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, verbose_name='Обязанности')
    company = models.CharField(max_length=100, verbose_name='Название компании')
    start_date = models.DateField(blank=True, null=True, verbose_name='Начал работать')
    end_date = models.DateField(blank=True, null=True, verbose_name='Закончил работать')


class ResponseChat(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    chat = models.ForeignKey(ResponseChat, on_delete=models.CASCADE, related_name='messages')
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=500)
