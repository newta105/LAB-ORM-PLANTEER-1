# Generated by Django 5.0.6 on 2024-07-22 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='price',
        ),
        migrations.AddField(
            model_name='plant',
            name='type',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
