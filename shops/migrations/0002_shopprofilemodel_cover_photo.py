#  Copyright (c) Code Written and Tested by Ahmed Emad in 21/02/2020, 20:11

# Generated by Django 3.0.3 on 2020-02-21 17:29

from django.db import migrations, models

import shops.models


class Migration(migrations.Migration):
    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopprofilemodel',
            name='cover_photo',
            field=models.ImageField(default=None, upload_to=shops.models.shop_photo_upload),
            preserve_default=False,
        ),
    ]
