# Generated by Django 3.0 on 2020-02-23 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRSapp', '0006_auto_20200222_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='itemslist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=50)),
                ('itemdesc', models.CharField(max_length=100)),
                ('itempic', models.ImageField(default='Image Not Found', upload_to='itemspics')),
            ],
        ),
    ]
