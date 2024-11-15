# Generated by Django 5.1.3 on 2024-11-15 11:38

import django.db.models.deletion
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
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estate_property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to='properties.realestateproperty')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'estate_property')},
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('rating', models.IntegerField(choices=[('1', '1 Star'), ('2', '2 Stars'), ('3', '3 Stars'), ('4', '4 Stars'), ('5', '5 Stars')])),
                ('date_time_of_publication', models.DateTimeField(auto_now_add=True)),
                ('estate_property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='properties.realestateproperty')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_time_of_publication'],
                'indexes': [models.Index(fields=['date_time_of_publication'], name='common_revi_date_ti_2617a7_idx')],
                'unique_together': {('user', 'estate_property')},
            },
        ),
    ]
