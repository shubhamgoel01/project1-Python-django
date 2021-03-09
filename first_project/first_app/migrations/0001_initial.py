# Generated by Django 3.0 on 2021-03-06 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=22)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
