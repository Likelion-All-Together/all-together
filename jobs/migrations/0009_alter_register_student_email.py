# Generated by Django 4.2.4 on 2023-08-16 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_register_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='student_email',
            field=models.TextField(verbose_name='이메일'),
        ),
    ]
