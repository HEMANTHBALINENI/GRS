# Generated by Django 3.0 on 2020-02-18 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRSapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
