# Generated by Django 2.2.3 on 2020-02-23 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_auto_20200223_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
