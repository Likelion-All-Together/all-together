# Generated by Django 4.2.4 on 2023-08-18 08:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_class_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='등록일'),
        ),
    ]