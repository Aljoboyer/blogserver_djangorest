# Generated by Django 5.1.1 on 2024-09-21 06:28

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('about', models.JSONField()),
                ('profileImg', models.ImageField(null=True, upload_to='profile_images/')),
            ],
        ),
    ]
