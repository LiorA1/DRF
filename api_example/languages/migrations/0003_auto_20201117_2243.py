# Generated by Django 3.1.2 on 2020-11-17 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0002_auto_20201117_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paradigm',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
