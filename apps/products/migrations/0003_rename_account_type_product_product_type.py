# Generated by Django 5.0.4 on 2024-04-08 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_account_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='account_type',
            new_name='product_type',
        ),
    ]
