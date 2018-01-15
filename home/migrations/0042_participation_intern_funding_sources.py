# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-15 19:04
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_auto_20180115_0406'),
    ]

    operations = [
        migrations.AddField(
            model_name='participation',
            name='intern_funding_sources',
            field=ckeditor.fields.RichTextField(default='Coordinator did not provide funding information', help_text='<p>For each source of funding for interns:<ol><li>What is the sponsor name?</li><li>What is the sponsorship dollar amount?</li><li>Is the funding is secured or tentative?</li><li>If the funding is tentative, please provide a date by which you will have a decision on your funding. Funding must be secured by intern selection time for this round.</li><li>Any additional information you need Outreachy organizers to know about this sponsorship.</li></ol><p>Outreachy organizers will be in touch with coordinators later to gather invoicing information.</p>'),
            preserve_default=False,
        ),
    ]