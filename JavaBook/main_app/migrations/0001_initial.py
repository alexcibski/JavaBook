# Generated by Django 4.2.3 on 2023-07-17 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('roast', models.CharField(max_length=100)),
                ('countryOfOrigin', models.CharField(max_length=100)),
                ('tastingNotes', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('review', models.TextField(max_length=250)),
                ('brewTips', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('description', models.TextField()),
                ('review', models.TextField()),
                ('brewTips', models.TextField()),
            ],
        ),
    ]
