# Generated by Django 4.2.4 on 2023-08-18 07:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_class_scrap'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='작성일'),
        ),
    ]
