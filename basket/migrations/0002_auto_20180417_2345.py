# Generated by Django 2.0.4 on 2018-04-17 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match',
            field=models.TextField(max_length=200),
        ),
    ]
