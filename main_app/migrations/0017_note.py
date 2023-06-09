# Generated by Django 3.1.1 on 2023-05-26 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_delete_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='notes/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
