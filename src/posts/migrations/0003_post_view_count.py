# Generated by Django 2.1.7 on 2019-02-25 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='View count'),
        ),
    ]
