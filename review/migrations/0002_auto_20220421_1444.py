# Generated by Django 3.2.7 on 2022-04-21 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewproduk',
            name='kondisi',
        ),
        migrations.RemoveField(
            model_name='reviewproduk',
            name='tanggal_penjualan',
        ),
        migrations.AlterField(
            model_name='reviewproduk',
            name='rating',
            field=models.ImageField(upload_to='motogpmerch-images'),
        ),
    ]