# Generated by Django 4.2.7 on 2023-11-19 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corner_detect', '0007_remove_cornerimage_picture_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cornerimage',
            name='picture_id',
            field=models.CharField(blank=True, max_length=13),
        ),
    ]
