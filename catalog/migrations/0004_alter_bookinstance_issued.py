# Generated by Django 3.2.5 on 2022-08-11 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_bookinstance_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='issued',
            field=models.BooleanField(default=True),
        ),
    ]
