# Generated by Django 3.1.2 on 2021-03-11 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0009_auto_20210311_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='types',
            field=models.CharField(choices=[('image', 'Image'), ('video', 'Video')], default='image', max_length=10),
        ),
    ]