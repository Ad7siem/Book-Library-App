# Generated by Django 4.1.6 on 2023-04-26 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteka_app', '0003_rename_team_scout_listpeople_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]