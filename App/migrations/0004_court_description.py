# Generated by Django 5.0.3 on 2024-03-16 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_court_pre_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='court',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
