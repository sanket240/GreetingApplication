# Generated by Django 3.1.5 on 2021-01-29 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Greeting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='greet',
            name='date',
        ),
    ]