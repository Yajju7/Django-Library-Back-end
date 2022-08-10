# Generated by Django 3.2.5 on 2022-08-10 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['first_name']},
        ),
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['issued_at']},
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='due_back',
        ),
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='borrower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='issued',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='issued_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='returned',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'available'), ('r', 'reserved')], default='m', max_length=1),
        ),
    ]