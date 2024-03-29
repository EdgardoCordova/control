# Generated by Django 5.0.1 on 2024-02-08 21:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('descriptions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('event_date', models.DateTimeField(blank=True)),
                ('event_date_end', models.DateTimeField(blank=True)),
                ('event_duration', models.SmallIntegerField(default=5)),
                ('circuit_slug', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='descriptions.description')),
            ],
        ),
    ]
