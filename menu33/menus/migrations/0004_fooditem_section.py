# Generated by Django 5.1.3 on 2024-11-22 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0003_alter_drinkitem_slug_alter_fooditem_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='section',
            field=models.CharField(choices=[('Starters', 'Starters'), ('Main Course', 'Main Course'), ('Desserts', 'Desserts'), ('Other', 'Other')], default='Other', max_length=20),
        ),
    ]
