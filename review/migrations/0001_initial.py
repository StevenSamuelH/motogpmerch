# Generated by Django 3.2.7 on 2022-04-21 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewProduk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('kondisi', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('tanggal_penjualan', models.DateField()),
                ('review', models.TextField()),
                ('gambar', models.ImageField(upload_to='motogpmerch-images')),
            ],
        ),
    ]
