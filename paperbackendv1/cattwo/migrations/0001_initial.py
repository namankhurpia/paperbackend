# Generated by Django 2.1.1 on 2018-09-13 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cattwo_papers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('course_code', models.CharField(max_length=10)),
                ('slot', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=20)),
                ('data_dir', models.FileField(upload_to='files')),
            ],
        ),
    ]
