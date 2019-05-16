# Generated by Django 2.0.1 on 2019-05-12 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pigeonhole', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PigeonholeAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('p_number', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='emails',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='pigeonhole',
            old_name='number',
            new_name='p_number',
        ),
        migrations.AddField(
            model_name='owner',
            name='id_number',
            field=models.IntegerField(default=201500666, max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pigeonhole',
            name='item',
            field=models.BooleanField(default=False),
        ),
    ]
