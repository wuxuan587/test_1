# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='record',
            fields=[
                ('match_id', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('team_id', models.AutoField(serialize=False, primary_key=True)),
                ('team_name', models.CharField(max_length=5)),
            ],
        ),
    ]
