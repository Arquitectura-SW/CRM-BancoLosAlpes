# Generated by Django 5.0.4 on 2024-04-07 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='id_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
