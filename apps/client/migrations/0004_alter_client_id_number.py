# Generated by Django 5.0.4 on 2024-04-08 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_alter_client_id_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='id_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]