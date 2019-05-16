# Generated by Django 2.0.1 on 2019-05-11 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('emails', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Pigeonhole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='owner',
            name='pigeonhole',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pigeonhole.Pigeonhole'),
        ),
    ]