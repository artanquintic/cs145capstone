# Generated by Django 2.0.1 on 2019-05-13 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pigeonhole', '0008_auto_20190513_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pigeonholeaction',
            name='emailed',
        ),
    ]