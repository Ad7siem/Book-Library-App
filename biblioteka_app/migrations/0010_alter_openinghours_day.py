# Generated by Django 4.1.6 on 2023-05-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteka_app', '0009_alter_listphoto_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openinghours',
            name='day',
            field=models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], max_length=10, unique=True),
        ),
    ]
