# Generated by Django 4.1.3 on 2023-05-03 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_confirm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('password', models.CharField(blank=True, default='', max_length=50, null=True)),
            ],
        ),
    ]
