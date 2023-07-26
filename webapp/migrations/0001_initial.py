# Generated by Django 4.2 on 2023-06-29 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='regdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rname', models.CharField(blank=True, max_length=100, null=True)),
                ('remail', models.CharField(blank=True, max_length=100, null=True)),
                ('rmobile', models.IntegerField(blank=True, max_length=100, null=True)),
                ('rpas', models.CharField(blank=True, max_length=100, null=True)),
                ('rimage', models.ImageField(blank=True, null=True, upload_to='user')),
            ],
        ),
    ]
