# Generated by Django 2.1.7 on 2019-02-25 21:04

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='Lorem ipsum emmet'),
            preserve_default=False,
        ),
    ]