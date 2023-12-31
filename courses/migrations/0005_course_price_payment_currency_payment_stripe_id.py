# Generated by Django 4.2.6 on 2023-11-11 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_owner_lesson_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='payment',
            name='currency',
            field=models.CharField(default='USD', max_length=50, verbose_name='Валюта'),
        ),
        migrations.AddField(
            model_name='payment',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Stripe ID'),
        ),
    ]
