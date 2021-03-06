# Generated by Django 3.2.8 on 2021-10-23 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
