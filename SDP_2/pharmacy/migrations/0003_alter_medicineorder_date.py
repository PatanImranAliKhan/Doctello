# Generated by Django 3.2.2 on 2021-05-18 23:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0002_medicineorder_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicineorder',
            name='date',
            field=models.DateField(default=datetime.date(2021, 5, 19)),
        ),
    ]
