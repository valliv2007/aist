# Generated by Django 2.2.28 on 2023-03-26 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lenivastore', '0011_change_validators_in_rating_and_stars_fields_in_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_popular',
            field=models.BooleanField(default=False, verbose_name='Популярный'),
        ),
    ]
