# Generated by Django 2.2.28 on 2023-03-23 11:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lenivastore', '0008_add_subcategory_field_in_product_modell'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.FloatField(blank=True, null=True, verbose_name='Рейтинг'),
        ),
        migrations.AddField(
            model_name='product',
            name='stars',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5, 'Кол-во звезд от 1 до 5')], verbose_name='Кол-во звезд'),
        ),
    ]
