# Generated by Django 3.1.4 on 2022-07-09 08:32

import django.core.validators
from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20220709_0046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Akreditasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tingkat', models.PositiveIntegerField(choices=[(1, 'S1'), (2, 'S2'), (3, 'S3')], default=1)),
                ('gambar', models.FileField(blank=True, null=True, upload_to=website.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['jpg']), website.models.file_size])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Berita',
            },
        ),
        migrations.AlterField(
            model_name='informasi',
            name='jenis',
            field=models.PositiveIntegerField(choices=[(1, 'informasi'), (2, 'Seminar'), (3, 'Portal'), (3, 'Perkuliahan')], default=1),
        ),
        migrations.AlterField(
            model_name='pengabdian',
            name='file_pdf',
            field=models.FileField(blank=True, null=True, upload_to=website.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['pdf']), website.models.file_size]),
        ),
        migrations.AlterField(
            model_name='roadmap_penelitian',
            name='file_pdf',
            field=models.FileField(blank=True, null=True, upload_to=website.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['jpg', 'png']), website.models.file_size]),
        ),
    ]
