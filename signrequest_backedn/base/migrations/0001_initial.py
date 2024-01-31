# Generated by Django 5.0.1 on 2024-01-05 09:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalRecipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='CreatedDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('signed', 'Signed'), ('unsigned', 'Unsigned'), ('sent', 'Sent'), ('viewed', 'Viewed')], default='unsigned', max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Signing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_signed', models.BooleanField(default=False)),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.externalrecipient')),
            ],
        ),
        migrations.CreateModel(
            name='UploadedDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='uploaded_documents/')),
                ('message', models.TextField(default='Default message')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_documents', to=settings.AUTH_USER_MODEL)),
                ('signings', models.ManyToManyField(blank=True, related_name='signed_documents', through='base.Signing', to='base.externalrecipient')),
            ],
        ),
        migrations.AddField(
            model_name='signing',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.uploadeddocument'),
        ),
    ]
