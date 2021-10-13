# Generated by Django 3.2.8 on 2021-10-13 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_remove_menuitem_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='category',
            field=models.CharField(choices=[('Pizzas', 'Pizzas'), ('Salads', 'Salads'), ('Desserts', 'Desserts'), ('Beverages', 'Beverages')], default='Pizzas', max_length=25, null=True),
        ),
    ]
