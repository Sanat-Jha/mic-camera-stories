# Generated by Django 5.1.3 on 2024-12-16 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentmanagement', '0005_channel_founder_channel_story_channel_whoarewe'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorySubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('organization', models.CharField(max_length=200)),
                ('story', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('feedback', models.TextField(default='')),
                ('status', models.CharField(default='Pending', max_length=200)),
            ],
        ),
    ]