# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 12:36
from __future__ import unicode_literals

from django.db import migrations

"""
Note: remember to update user / group permissions after applying this
migration.
"""

class Migration(migrations.Migration):

    dependencies = [
        ('labhamster', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel('Item', 'Product'),
        migrations.RenameField('Order', 'item', 'product'),
    ]
