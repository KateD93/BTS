# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth import models
from django.db import migrations


def create_admin_user(apps, schema_editor):
    models.User.objects.create_user(
        username=settings.INITIAL_ADMIN_EMAIL,
        email=settings.INITIAL_ADMIN_EMAIL,
        password=settings.INITIAL_ADMIN_PASSWORD
    )


class Migration(migrations.Migration):

    dependencies = []
    operations = [migrations.RunPython(create_admin_user)]

