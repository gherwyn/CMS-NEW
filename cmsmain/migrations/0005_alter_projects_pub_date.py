# Generated by Django 4.1.7 on 2023-03-26 09:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsmain', '0004_alter_projects_pub_date_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 26, 9, 25, 57, 194167, tzinfo=datetime.timezone.utc)),
        ),
    ]
