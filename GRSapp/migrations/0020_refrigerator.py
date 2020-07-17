# Generated by Django 3.0 on 2020-03-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRSapp', '0019_auto_20200315_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refrigerator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandname', models.CharField(max_length=50)),
                ('modelname', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('colour', models.CharField(max_length=50)),
                ('refrig_pic', models.ImageField(default='Image Not Found', upload_to='refrigerator')),
                ('Capacity', models.IntegerField()),
                ('Warranty', models.IntegerField()),
                ('double_door', models.BooleanField()),
                ('single_door', models.BooleanField()),
            ],
        ),
    ]