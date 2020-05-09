# Generated by Django 3.0.6 on 2020-05-05 21:09

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foundation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000)),
                ('headquarters_address', models.CharField(max_length=50)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
    ]
