# Generated by Django 2.0.1 on 2019-05-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pigeonhole', '0006_auto_20190512_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pigeonholeaction',
            name='id_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pigeonholeaction',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]