# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-13 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0116_initialmentorfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='initialmentorfeedback',
            name='organizer_payment_approved',
            field=models.NullBooleanField(default=None, help_text='Outreachy organizers approve or do not approve to pay this intern.'),
        ),
    ]