# Generated by Django 5.1.3 on 2024-11-15 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='realestateproperty',
            name='city',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]