# Generated by Django 5.1.3 on 2024-11-21 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wineitem',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='wineitem',
            name='restaurants',
            field=models.ManyToManyField(related_name='wine_items', to='restaurants.restaurant'),
        ),
        migrations.AddField(
            model_name='wineitem',
            name='wine_type',
            field=models.CharField(blank=True, choices=[('RED', 'Red'), ('WHITE', 'White'), ('ROSE', 'Rosé'), ('SPARKLING', 'Sparkling'), ('DESSERT', 'Dessert'), ('FORTIFIED', 'Fortified')], max_length=50, null=True),
        ),
    ]
