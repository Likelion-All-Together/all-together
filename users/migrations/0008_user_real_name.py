# Generated by Django 4.2.4 on 2023-08-11 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_user_birth_year_remove_user_nationality'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='real_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
