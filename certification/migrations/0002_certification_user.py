# Generated by Django 5.1.1 on 2024-10-26 16:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
    model_name='certification',
    name='user',
    field=models.ForeignKey(
        on_delete=django.db.models.deletion.CASCADE,
        related_name='certifications',
        to=settings.AUTH_USER_MODEL,
        null=True,  # Allow null values temporarily
        blank=True  # Allow blank values in forms (if applicable)
    ),
),
    ]