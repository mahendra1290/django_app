# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-09-05 18:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='check',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='products',
            name='dt',
            field=models.DateField(default=datetime.date(2020, 9, 5)),
        ),
        migrations.AddField(
            model_name='products',
            name='mail',
            field=models.EmailField(default='abc@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='products',
            name='summary',
            field=models.TextField(default='this is a product'),
        ),
        migrations.AlterField(
            model_name='products',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=6, max_digits=8),
        ),
        migrations.AlterField(
            model_name='products',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
