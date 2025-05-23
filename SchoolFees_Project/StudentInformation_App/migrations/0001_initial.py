# Generated by Django 5.1.6 on 2025-04-04 03:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('admission_number', models.IntegerField(unique=True)),
                ('grade', models.CharField(max_length=50)),
                ('guardian_name', models.CharField(max_length=100)),
                ('guardian_contact', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('registered_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='registered_students', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
