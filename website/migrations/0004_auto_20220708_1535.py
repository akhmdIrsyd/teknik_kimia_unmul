# Generated by Django 3.1.4 on 2022-07-08 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20220708_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='dosen',
            name='s1',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dosen',
            name='s2',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dosen',
            name='s3',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Pendidikan_dosen',
        ),
    ]