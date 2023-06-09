# Generated by Django 4.1.7 on 2023-03-26 09:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsmain', '0003_projects_user_image_alter_projects_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 26, 9, 23, 36, 415136, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='null', max_length=254)),
                ('body', models.TextField(default='null')),
                ('created_on', models.DateTimeField(verbose_name='date commented')),
                ('active', models.BooleanField(default=False)),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='cmsmain.projects')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
