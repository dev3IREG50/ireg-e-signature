# Generated by Django 5.0.1 on 2024-01-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_signing_document_log_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='signing',
            name='signature_image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
