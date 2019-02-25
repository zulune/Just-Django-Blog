# Generated by Django 2.1.7 on 2019-02-25 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
            ],
        ),
    ]
