# Generated by Django 3.1.2 on 2021-03-11 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0007_auto_20210311_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
