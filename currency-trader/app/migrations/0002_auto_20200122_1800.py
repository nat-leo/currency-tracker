# Generated by Django 2.2.4 on 2020-01-22 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candle',
            old_name='candle_close',
            new_name='c',
        ),
        migrations.RenameField(
            model_name='candle',
            old_name='candle_high',
            new_name='h',
        ),
        migrations.RenameField(
            model_name='candle',
            old_name='candle_low',
            new_name='l',
        ),
        migrations.RenameField(
            model_name='candle',
            old_name='candle_open',
            new_name='o',
        ),
    ]