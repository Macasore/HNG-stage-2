# Generated by Django 4.1.3 on 2022-11-04 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_main_operationtype_alter_main_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='operationtype',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='main',
            name='x',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='y',
            field=models.IntegerField(blank=True),
        ),
    ]
