# Generated by Django 5.1.6 on 2025-04-09 00:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fee_App', '0002_auto_20250406_1711'),
        ('StudentInformation_App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentrecords',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='studentrecords',
            name='guardian_name',
        ),
        migrations.AddField(
            model_name='studentrecords',
            name='fee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Fee_App.fee'),
            preserve_default=False,
        ),
    ]
