# Generated by Django 3.0.6 on 2020-05-10 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foundations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(max_length=5000)),
                ('foundation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foundations.Foundation')),
            ],
        ),
    ]