# Generated by Django 3.2.13 on 2022-06-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bukti', '0004_merge_0003_auto_20220612_1532_0003_auto_20220613_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapembeli',
            name='bukti_img',
            field=models.URLField(),
        ),
    ]
