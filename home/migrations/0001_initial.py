# Generated by Django 3.0.2 on 2020-04-12 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uid', models.IntegerField(default=None)),
                ('Title', models.CharField(max_length=100)),
                ('Url', models.TextField()),
                ('Author', models.CharField(max_length=100)),
                ('Genre', models.CharField(max_length=100)),
            ],
        ),
    ]
