# Generated by Django 3.2.9 on 2022-02-07 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='msg',
            name='message',
            field=models.CharField(default='', max_length=1000),
        ),
    ]