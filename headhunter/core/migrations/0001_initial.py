# Generated by Django 3.2 on 2022-11-25 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название вакансии')),
                ('salary', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Заработная плата')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание вакансии')),
                ('experience', models.FloatField(verbose_name='Опыт работы')),
                ('category', models.TextField(choices=[('IT', 'IT'), ('DESIGN', 'Дизайн'), ('MANAGEMENT', 'Менеджмент'), ('MEDICINE', 'Медицина'), ('ENGINEERING', 'Инженерное дело'), ('ART', 'Искусство'), ('TRANSPORT', 'Транспорт'), ('MARKETING', 'Маркетинг'), ('TRADE', 'Торговля'), ('ECONOMY', 'Экономика')], verbose_name='Категория вакансии')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
                ('is_active', models.BooleanField(default=False, verbose_name='Скрыть вакансию')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to=settings.AUTH_USER_MODEL, verbose_name='Работодатель')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Название резюме')),
                ('category', models.TextField(blank=True, choices=[('IT', 'IT'), ('DESIGN', 'Дизайн'), ('MANAGEMENT', 'Менеджмент'), ('MEDICINE', 'Медицина'), ('ENGINEERING', 'Инженерное дело'), ('ART', 'Искусство'), ('TRANSPORT', 'Транспорт'), ('MARKETING', 'Маркетинг'), ('TRADE', 'Торговля'), ('ECONOMY', 'Экономика')], null=True, verbose_name='Категория вакансии')),
                ('about', models.TextField(max_length=3000, verbose_name='О себе')),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Желаемая зарплата')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='Email')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Последние изменение')),
                ('is_active', models.BooleanField(default=True, verbose_name='Скрыть резюме')),
                ('telegram', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссылка на телеграм')),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссылка на Linkedin')),
                ('facebook', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссылка на Facebook')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Соискатель')),
            ],
        ),
        migrations.CreateModel(
            name='ResponseChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.resume')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vacancy')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(max_length=500)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='core.responsechat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Обязанности')),
                ('company', models.CharField(max_length=100, verbose_name='Название компании')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Начал работать')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Закончил работать')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study', models.CharField(max_length=100, verbose_name='Место обучения')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Начал обучаться')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Закончил обучаться')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.resume')),
            ],
        ),
    ]
