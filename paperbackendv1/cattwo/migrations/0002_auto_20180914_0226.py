# Generated by Django 2.1.1 on 2018-09-13 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cattwo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cattwo_papers',
            name='data_dir',
            field=models.FileField(upload_to='cattwofiles'),
        ),
    ]
