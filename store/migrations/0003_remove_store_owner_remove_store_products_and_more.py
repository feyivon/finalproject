# Generated by Django 5.0.3 on 2024-03-25 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='store',
            name='products',
        ),
        migrations.AddField(
            model_name='store',
            name='location',
            field=models.CharField(default='null', max_length=225),
        ),
        migrations.AddField(
            model_name='store',
            name='name',
            field=models.CharField(default='null', max_length=255),
        ),
    ]
