# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.models import User
from django.conf import settings


def create_admin_user(apps, schema_editor):
    User.objects.create_user(
        username=settings.INITIAL_ADMIN_EMAIL,
        email=settings.INITIAL_ADMIN_EMAIL,
        password=settings.INITIAL_ADMIN_PASSWORD
    )


class Migration(migrations.Migration):

    dependencies = []
    operations = [migrations.RunPython(create_admin_user)]

