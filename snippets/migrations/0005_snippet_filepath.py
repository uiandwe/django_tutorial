# Generated by Django 2.1.2 on 2019-01-11 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_snippet_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='filePath',
            field=models.TextField(default=''),
        ),
    ]
