# Generated by Django 5.1.1 on 2024-09-24 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_createdat_blog_updatedat_comment_createdat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
