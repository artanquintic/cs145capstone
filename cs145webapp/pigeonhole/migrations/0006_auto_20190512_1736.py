# Generated by Django 2.0.1 on 2019-05-12 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pigeonhole', '0005_pigeonholeaction_emailed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='pigeonhole',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='pigeonhole.Pigeonhole'),
        ),
        migrations.AlterField(
            model_name='pigeonhole',
            name='p_number',
            field=models.IntegerField(verbose_name='Pigeonhole number'),
        ),
    ]
