# Generated by Django 5.0.2 on 2024-03-24 12:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_review_date_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='estimated_price',
            field=models.DecimalField(decimal_places=2, help_text='Introduzca el coste en euros', max_digits=7, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='service',
            name='city',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='service',
            name='profession',
            field=models.IntegerField(choices=[(1, 'Lavandero'), (2, 'Celador'), (3, 'Albañil'), (4, 'Carpintero'), (5, 'Cerrajero'), (6, 'Mecánico'), (7, 'Electricista'), (8, 'Conductor'), (9, 'Pintor'), (10, 'Herrero'), (11, 'Sastre'), (12, 'Profesor particular')]),
        ),
    ]
