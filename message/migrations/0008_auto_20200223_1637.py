# Generated by Django 2.2.3 on 2020-02-23 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0007_auto_20200223_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(verbose_name='时间'),
        ),
    ]