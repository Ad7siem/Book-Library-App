# Generated by Django 4.1.6 on 2023-04-26 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteka_app', '0004_listphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listphoto',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='listphoto',
            name='image',
            field=models.ImageField(upload_to='static/'),
        ),
    ]
