# Generated by Django 3.2.2 on 2021-05-18 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0008_consult_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='consult',
            name='problem',
            field=models.CharField(default='', max_length=100),
        ),
    ]