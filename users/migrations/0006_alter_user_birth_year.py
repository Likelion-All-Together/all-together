# Generated by Django 4.2.4 on 2023-08-11 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_birth_year_user_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_year',
            field=models.DateField(blank=True, null=True),
        ),
    ]
