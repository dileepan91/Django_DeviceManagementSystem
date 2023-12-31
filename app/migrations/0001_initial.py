# Generated by Django 4.2.5 on 2023-09-23 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=20)),
                ('camera_id', models.CharField(max_length=30)),
                ('lens_id', models.CharField(max_length=30)),
                ('SD_card', models.CharField(max_length=30)),
                ('datetime_out', models.DateTimeField(verbose_name='Date device out')),
                ('datetime_in', models.DateTimeField(verbose_name='Date device in')),
                ('condition', models.CharField(max_length=500)),
            ],
        ),
    ]
