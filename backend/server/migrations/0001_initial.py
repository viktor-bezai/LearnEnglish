# Generated by Django 5.1 on 2025-02-04 01:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(db_index=True, max_length=300, unique=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('transcript', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'youtube_video',
            },
        ),
        migrations.CreateModel(
            name='YoutubeWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(db_index=True, max_length=100)),
                ('language', models.CharField(choices=[('ENG', 'English')], default='ENG', max_length=3)),
                ('timestamped_url', models.CharField(max_length=500)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.youtubevideo')),
            ],
            options={
                'db_table': 'youtube_word',
            },
        ),
    ]
