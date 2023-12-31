# Generated by Django 4.2.5 on 2023-09-24 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_audit_condition_alter_audit_datetime_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audit',
            name='condition',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='audit',
            name='datetime_in',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Date device in'),
        ),
    ]
