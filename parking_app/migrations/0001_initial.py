# Generated by Django 5.1 on 2024-09-27 08:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=30, unique=True, verbose_name='building address')),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('floor_number', models.PositiveSmallIntegerField()),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking_app.building')),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('local_id', models.PositiveSmallIntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking_app.building')),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking_app.floor')),
            ],
            options={
                'verbose_name': 'Parking Slot',
                'verbose_name_plural': 'Parking Slots',
                'unique_together': {('floor', 'local_id')},
            },
        ),
    ]
