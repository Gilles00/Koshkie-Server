#  Copyright (c) Code Written and Tested by Ahmed Emad on 2019

# Generated by Django 3.0 on 2019-12-25 18:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shops', '0006_auto_20191217_2141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmodel',
            old_name='base_price',
            new_name='price',
        ),
        migrations.AddField(
            model_name='shopprofilemodel',
            name='description',
            field=models.TextField(default='  '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productgroupmodel',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_groups',
                                    to='shops.ShopProfileModel'),
        ),
        migrations.AlterField(
            model_name='relyon',
            name='choosed_option_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.OptionGroupModel'),
        ),
        migrations.AlterField(
            model_name='relyon',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.OptionModel'),
        ),
        migrations.AlterField(
            model_name='relyon',
            name='option_group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rely_on',
                                       to='shops.OptionGroupModel'),
        ),
        migrations.AlterField(
            model_name='shopprofilemodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shop_profile',
                                       to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='productgroupmodel',
            unique_together={('shop', 'sort'), ('shop', 'title')},
        ),
    ]