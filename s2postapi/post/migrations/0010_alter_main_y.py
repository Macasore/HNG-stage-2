# Generated by Django 4.1.3 on 2022-11-05 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_alter_main_y'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='y',
            field=models.IntegerField(default=0),
        ),
    ]
