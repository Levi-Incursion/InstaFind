# Generated by Django 5.0.6 on 2024-09-17 03:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_advocate_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Handle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('channel_info', models.CharField(max_length=1000)),
                ('posts', models.CharField(max_length=1000)),
                ('followers', models.CharField(max_length=1000)),
                ('avg_likes', models.CharField(max_length=1000)),
                ('profile_pic', models.TextField(blank=True, max_length=1000, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.category')),
            ],
        ),
        migrations.DeleteModel(
            name='Advocate',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]
