# Generated by Django 4.2.7 on 2023-11-18 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CornerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='')),
                ('info', models.CharField(blank=True, max_length=200)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
