# Generated by Django 4.2.7 on 2024-01-06 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0011_remove_passenger_seat_num_alter_passenger_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]
