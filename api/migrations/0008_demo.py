# Generated by Django 4.1.3 on 2023-03-29 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_navbar_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
            ],
        ),
    ]
