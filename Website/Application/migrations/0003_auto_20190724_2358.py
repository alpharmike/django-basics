# Generated by Django 2.2.1 on 2019-07-24 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=264),
        ),
    ]