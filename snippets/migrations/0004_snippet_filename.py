# Generated by Django 2.1.2 on 2019-01-11 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_snippet_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='fileName',
            field=models.TextField(default=''),
        ),
    ]
