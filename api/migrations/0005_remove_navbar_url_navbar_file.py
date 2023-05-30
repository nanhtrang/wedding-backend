# Generated by Django 4.1.3 on 2023-03-29 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_navbar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navbar',
            name='url',
        ),
        migrations.AddField(
            model_name='navbar',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=None),
        ),
    ]
