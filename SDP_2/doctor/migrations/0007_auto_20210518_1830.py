# Generated by Django 3.2.2 on 2021-05-18 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_auto_20210517_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='idproof',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='resume',
            field=models.CharField(max_length=1000),
        ),
    ]
