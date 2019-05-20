# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrix', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comments',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.IntegerField(default=1),
        ),
    ]
