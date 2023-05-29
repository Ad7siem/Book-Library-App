# Generated by Django 4.1.6 on 2023-05-10 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteka_app', '0008_openinghours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listphoto',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='closing_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='opening_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]