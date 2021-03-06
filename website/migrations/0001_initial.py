# Generated by Django 3.1.4 on 2022-07-07 16:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import website.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Berita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Judul', models.CharField(max_length=50)),
                ('isi_berita', tinymce.models.HTMLField()),
                ('gambar', models.FileField(blank=True, null=True, upload_to=website.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['jpg']), website.models.file_size])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Berita',
            },
        ),
        migrations.CreateModel(
            name='Dosen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('email', tinymce.models.HTMLField()),
                ('foto', models.FileField(blank=True, null=True, upload_to=website.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['jpg']), website.models.file_size])),
                ('google_scholar', models.CharField(max_length=50)),
                ('schopus', models.CharField(max_length=50)),
                ('sinta', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Dosen',
            },
        ),
        migrations.CreateModel(
            name='Fasilitas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.PositiveIntegerField(choices=[(1, 'Ruangan'), (2, 'Ruang Baca'), (3, 'Laboratorium'), (3, 'Fasilitas Pendukung')], default=1)),
                ('nama', models.CharField(max_length=50)),
                ('keterangan', tinymce.models.HTMLField()),
                ('gambar', models.FileField(blank=True, null=True, upload_to=website.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['jpg']), website.models.file_size])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Fasilitas',
            },
        ),
        migrations.CreateModel(
            name='Informasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.PositiveIntegerField(choices=[(1, 'indormasi'), (2, 'Seminar'), (3, 'Portal'), (3, 'Perkuliahan')], default=1)),
                ('nama', models.CharField(max_length=50)),
                ('keterangan', tinymce.models.HTMLField()),
                ('gambar', models.FileField(blank=True, null=True, upload_to=website.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['jpg']), website.models.file_size])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Informasi',
            },
        ),
        migrations.CreateModel(
            name='Jurnal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tahun', models.IntegerField(choices=[(2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022, verbose_name='tahun')),
                ('judul', models.CharField(max_length=50)),
                ('file_pdf', models.FileField(blank=True, null=True, upload_to=website.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['[pdf]']), website.models.file_size])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Jurnal',
            },
        ),
        migrations.CreateModel(
            name='Kurikulum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tingkat', models.PositiveIntegerField(choices=[(1, 'S1'), (2, 'S2'), (3, 'S3')], default=1)),
                ('kode', models.CharField(max_length=50)),
                ('nama_mata_kuliah', models.CharField(max_length=50)),
                ('semester', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Kurikulum',
            },
        ),
        migrations.CreateModel(
            name='Pengabdian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tahun', models.IntegerField(choices=[(2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022, verbose_name='tahun')),
                ('judul', models.CharField(max_length=50)),
                ('file_pdf', models.FileField(blank=True, null=True, upload_to=website.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['[pdf]']), website.models.file_size])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Pengabdian',
            },
        ),
        migrations.CreateModel(
            name='Persyaratan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Judul', models.CharField(max_length=50)),
                ('tingkat', models.PositiveIntegerField(choices=[(1, 'S1'), (2, 'S2'), (3, 'S3')], default=1)),
                ('file_pdf', models.FileField(blank=True, null=True, upload_to=website.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['pdf']), website.models.file_size])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Persyaratan',
            },
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gambar', models.FileField(blank=True, null=True, upload_to=website.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['jpg']), website.models.file_size])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roadmap_Penelitian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_pdf', models.FileField(blank=True, null=True, upload_to=website.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['[pdf]']), website.models.file_size])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Roadmap Penelitian',
            },
        ),
        migrations.CreateModel(
            name='Sejarah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Judul', models.CharField(max_length=50)),
                ('gambar', models.FileField(blank=True, null=True, upload_to=website.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['jpg']), website.models.file_size])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Sejarah',
            },
        ),
        migrations.CreateModel(
            name='SOP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Judul', models.CharField(max_length=50)),
                ('tingkat', models.PositiveIntegerField(choices=[(1, 'S1'), (2, 'S2'), (3, 'S3')], default=1)),
                ('file_pdf', models.FileField(blank=True, null=True, upload_to=website.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['pdf']), website.models.file_size])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'SOP',
            },
        ),
        migrations.CreateModel(
            name='Tendik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('foto', models.FileField(blank=True, null=True, upload_to=website.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['jpg']), website.models.file_size])),
                ('NIP', models.CharField(max_length=50)),
                ('Tanggal_Lahir', models.CharField(max_length=50)),
                ('TMT_CPNS', models.DateField()),
                ('TMT_PNS', models.DateField()),
                ('PANGKAT', models.CharField(max_length=50)),
                ('pendidikan', models.CharField(max_length=50)),
                ('instansi', models.CharField(max_length=50)),
                ('unit_kerja', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Tendik',
            },
        ),
        migrations.CreateModel(
            name='Visimisi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Judul', models.PositiveIntegerField(choices=[(1, 'Visi'), (2, 'Misi'), (3, 'Tujuan')], default=1)),
                ('tingkat', models.PositiveIntegerField(choices=[(1, 'Prodi Kimia'), (2, 'S1'), (3, 'S2')], default=1)),
                ('isi', tinymce.models.HTMLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Visimisi',
            },
        ),
        migrations.CreateModel(
            name='Penelitian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tahun', models.IntegerField(choices=[(2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022, verbose_name='tahun')),
                ('judul', models.CharField(max_length=50)),
                ('sumber', models.CharField(max_length=50)),
                ('jumlah', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dosen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.dosen')),
            ],
            options={
                'verbose_name_plural': 'Penelitian',
            },
        ),
        migrations.CreateModel(
            name='Pendidikan_dosen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tingkat', models.PositiveIntegerField(choices=[(1, 'S1'), (2, 'S2'), (3, 'S3')], default=1)),
                ('universitas', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dosen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.dosen')),
            ],
            options={
                'verbose_name_plural': 'Pendidikan_dosen',
            },
        ),
    ]
