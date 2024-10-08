# Generated by Django 5.1.1 on 2024-09-20 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=50)),
                ('client_email', models.EmailField(max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
