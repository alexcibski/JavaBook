# Generated by Django 4.2.3 on 2023-07-20 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_coffee_image_alter_maker_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, verbose_name='Rating'),
        ),
        migrations.AlterField(
            model_name='coffee',
            name='roast',
            field=models.CharField(choices=[('L', 'Light'), ('M', 'Medium'), ('D', 'Dark')], max_length=1, verbose_name='Roast'),
        ),
        migrations.AlterField(
            model_name='maker',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, verbose_name='Rating'),
        ),
    ]
