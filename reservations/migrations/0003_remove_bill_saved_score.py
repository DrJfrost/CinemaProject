# Generated by Django 3.0.7 on 2020-08-16 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_bill_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='saved_score',
        ),
    ]
