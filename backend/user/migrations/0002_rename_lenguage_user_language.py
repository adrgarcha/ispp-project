# Generated by Django 5.0.2 on 2024-02-29 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='lenguage',
            new_name='language',
        ),
    ]
