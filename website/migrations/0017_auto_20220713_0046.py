# Generated by Django 3.1.4 on 2022-07-12 16:46

import django.core.validators
from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20220712_1811'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jadwal_kuliah',
            options={'verbose_name_plural': 'Jadwal Kuliah'},
        ),
        migrations.AlterModelOptions(
            name='statistik_mhs',
            options={'verbose_name_plural': 'Statistik Mahasiswa'},
        ),
        migrations.AlterField(
            model_name='jurnal',
            name='file_pdf',
            field=models.FileField(upload_to=website.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['pdf']), website.models.file_size]),
        ),
        migrations.AlterField(
            model_name='tendik',
            name='PANGKAT',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tendik',
            name='TMT_CPNS',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tendik',
            name='TMT_PNS',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tendik',
            name='foto',
            field=models.FileField(default=1, upload_to=website.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['jpg']), website.models.file_size]),
            preserve_default=False,
        ),
    ]
