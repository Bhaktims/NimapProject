# Generated by Django 5.1.1 on 2024-09-22 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_client_created_by_projects_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='users',
        ),
    ]
