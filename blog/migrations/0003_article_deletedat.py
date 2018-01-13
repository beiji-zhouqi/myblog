# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171210_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='deletedAt',
            field=models.DateTimeField(default=None, null=True, verbose_name='\u5220\u9664\u65f6\u95f4'),
        ),
    ]
