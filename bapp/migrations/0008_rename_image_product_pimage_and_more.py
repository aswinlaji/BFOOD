# Generated by Django 5.0.1 on 2024-02-25 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bapp', '0007_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='pimage',
        ),
        migrations.RenameField(
            model_name='resreg',
            old_name='image',
            new_name='rimage',
        ),
    ]