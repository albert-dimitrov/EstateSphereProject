# Generated by Django 5.1.3 on 2024-11-15 11:38

import django.db.models.deletion
import estatesphere.images.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('properties', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', validators=[estatesphere.images.validators.FileSizeValidator(5)])),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('estate_property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='properties.realestateproperty')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
