# Generated by Django 4.2.4 on 2023-08-17 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informations', '0013_afterschool_url_regionandmulticultural_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionandmulticultural',
            name='support_cycle',
            field=models.CharField(max_length=50, verbose_name='지원 주기'),
        ),
    ]
