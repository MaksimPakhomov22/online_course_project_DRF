# Generated by Django 4.2.6 on 2023-11-11 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_account_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Stripe аккаунт'),
        ),
    ]
