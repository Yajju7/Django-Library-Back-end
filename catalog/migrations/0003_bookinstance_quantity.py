# Generated by Django 3.2.5 on 2022-08-10 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20220810_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]