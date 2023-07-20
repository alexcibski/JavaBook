# Generated by Django 4.2.3 on 2023-07-19 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='maker',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='coffee',
            name='brewTips',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='coffee',
            name='countryOfOrigin',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='coffee',
            name='rating',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='coffee',
            name='review',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='coffee',
            name='roast',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='coffee',
            name='tastingNotes',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='maker',
            name='brewTips',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='maker',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='maker',
            name='rating',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='maker',
            name='review',
            field=models.TextField(blank=True),
        ),
    ]
