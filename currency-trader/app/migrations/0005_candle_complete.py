# Generated by Django 2.2.4 on 2020-01-25 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='candle',
            name='complete',
            field=models.CharField(default='empty', max_length=10),
        ),
    ]