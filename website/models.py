from django.db import models
from django.core.validators import FileExtensionValidator
import datetime

from tinymce.models import HTMLField

# Create your models here.

def _upload_path(instance, filename):
    return instance.get_upload_path(filename)


def file_size(value):  # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MB.')


class Profil(models.Model):
    gambar = models.FileField(upload_to=_upload_path, validators=[
                              FileExtensionValidator(['jpg', 'png']), file_size])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_upload_path(self, filename):
        return "uploads/profil"+"/"+filename

    def __str__(self):
        return str(self.id)

class Sejarah(models.Model):
    isi = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)\

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Sejarah"

class Visimisi(models.Model):
    NAMA_TYPE_CHOICES = (
        (1, 'Visi'),
        (2, 'Misi'),
        (3, 'Tujuan'),
    )
    TINGKAT_TYPE_CHOICES = (
        (1, 'Prodi Kimia'),
        (2, 'S1'),
        (3, 'S2'),
    )
    Judul = models.PositiveIntegerField(choices=NAMA_TYPE_CHOICES, default=1)
    tingkat = models.PositiveIntegerField(choices=TINGKAT_TYPE_CHOICES, default=1)
    isi = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.tingkat)+"-"+str(self.Judul)

    class Meta:
        verbose_name_plural = "Visimisi"


class Dosen(models.Model):
    nama = models.CharField(max_length=50)
    email = HTMLField()
    foto = models.FileField(upload_to=_upload_path, validators=[
                              FileExtensionValidator(['jpg','png']), file_size])
    s1 = models.CharField(max_length=50)
    s2 = models.CharField(max_length=50)
    s3 = models.CharField(max_length=50, blank=True, null=True)
    google_scholar = models.CharField(max_length=50)
    schopus = models.CharField(max_length=50)
    sinta = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def get_upload_path(self, filename):
        return "uploads/dosen"+"/"+filename

    def __str__(self):
        return str(self.nama)

    class Meta:
        verbose_name_plural = "Dosen"



class Tendik(models.Model):
    nama = models.CharField(max_length=50)
    foto = models.FileField(upload_to=_upload_path, validators=[
        FileExtensionValidator(['jpg']), file_size])
    NIP = models.CharField(max_length=50)
    Tanggal_Lahir = models.DateField()
    TMT_CPNS = models.DateField(blank=True, null=True)
    TMT_PNS = models.DateField(blank=True, null=True)
    PANGKAT = models.CharField(max_length=50, blank=True, null=True)
    pendidikan = models.CharField(max_length=50)
    instansi = models.CharField(max_length=50)
    unit_kerja = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_upload_path(self, filename):
        return "uploads/tendik"+"/"+filename

    def __str__(self):
        return str(self.nama)

    class Meta:
        verbose_name_plural = "Tendik"


class SOP(models.Model):
    TINGKAT_TYPE_CHOICES = (
        (1, 'S1'),
        (2, 'S2'),
        (3, 'S3'),
    )
    Judul = models.CharField(max_length=50)
    tingkat = models.PositiveIntegerField(choices=TINGKAT_TYPE_CHOICES, default=1)
    file_pdf = models.FileField(upload_to=_upload_path, validators=[
                              FileExtensionValidator(['pdf']), file_size])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_upload_path(self, filename):
        return "uploads/berita"+"/"+filename

    def __str__(self):
        return str(self.Judul)

    class Meta:
        verbose_name_plural = "SOP"


class Persyaratan(models.Model):
    TINGKAT_TYPE_CHOICES = (
        (1, 'S1'),
        (2, 'S2'),
        (3, 'S3'),
    )
    Judul = models.CharField(max_length=50)
    tingkat = models.PositiveIntegerField(choices=TINGKAT_TYPE_CHOICES, default=1)
    file_pdf = models.FileField(upload_to=_upload_path, validators=[
        FileExtensionValidator(['pdf']), file_size])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_upload_path(self, filename):
        return "uploads/berita"+"/"+filename

    def __str__(self):
        return str(self.Judul)

    class Meta:
        verbose_name_plural = "Persyaratan"


class Lembaga_mhs(models.Model):
    Judul = models.CharField(max_length=50)
    gambar = models.FileField(upload_to=_upload_path, validators=[
                              FileExtensionValidator(['jpg', 'png']), file_size])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_upload_path(self, filename):
        return "uploads/Lembaga_mhs"+"/"+filename

    def __str__(self):
        return str(self.Judul)
    
    class Meta:
        verbose_name_plural = "Lembaga Mahasiswa"


class prestasi_mhs(models.Model):
    year_dropdown = []
    for y in range(2011, (datetime.datetime.now().year + 1)):
        year_dropdown.append((y, y))

    tahun = models.IntegerField(
        ('tahun'), choices=year_dropdown, default=datetime.datetime.now().year)
    nama = models.CharField(max_length=50)
    nim = models.CharField(max_length=50)
    lomba = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.lomba)

    class Meta:
        verbose_name_plural = "Prestasi Mahasiswa"


class statistik_mhs(models.Model):
    year_dropdown = []
    for y in range(2005, (datetime.datetime.now().year + 1)):
        year_dropdown.append((y, y))

    tahun = models.IntegerField(
        ('tahun'), choices=year_dropdown, default=datetime.datetime.now().year)
    jumlah = models.IntegerField()
    lulus = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.tahun)

    class Meta:
        verbose_name_plural = "Statistik Mahasiswa"


class Kurikulum(models.Model):
    TINGKAT_TYPE_CHOICES = (
        (1, 'S1'),
        (2, 'S2'),
        (3, 'S3'),
    )
    tingkat = models.PositiveIntegerField(choices=TINGKAT_TYPE_CHOICES, default=1)
    kode = models.CharField(max_length=50)
    nama_mata_kuliah = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    sks = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.kode)+"-"+str(self.nama_mata_kuliah)

    class Meta:
        verbose_name_plural = "Kurikulum"

class Kalender_akademik(models.Model):
    
    Judul = models.CharField(max_length=100)
    upload_file = models.FileField(upload_to=_upload_path,  validators=[
                              FileExtensionValidator(['pdf']), file_size])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_upload_path(self, filename):
        return "uploads/kalender"+"/"+filename

    def __str__(self):
        return str(self.Judul)

    class Meta:
        verbose_name_plural = "Kalender Akademik"

class Akreditasi(models.Model):
    TINGKAT_TYPE_CHOICES = (
        (1, 'akreditasi S1'),
        (2, 'akreditasi S2'),
        (3, 'akreditasi S3'), 
        (4, 'SK AKREDITASI'),
    )
    jenis = models.PositiveIntegerField(choices=TINGKAT_TYPE_CHOICES, default=1)
    Judul = models.CharField(max_length=100)
    upload_file = models.FileField(upload_to=_upload_path,  validators=[
                              FileExtensionValidator(['jpg','png','pdf']), file_size])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_upload_path(self, filename):
        return "uploads/akreditasi"+"/"+filename

    def __str__(self):
        return str(self.Judul)

    class Meta:
        verbose_name_plural = "Akreditasi"

class Jadwal_kuliah(models.Model):
    
    Judul = models.CharField(max_length=100)
    upload_file = models.FileField(upload_to=_upload_path,  validators=[
                              FileExtensionValidator(['pdf']), file_size])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_upload_path(self, filename):
        return "uploads/jadwal"+"/"+filename

    def __str__(self):
        return str(self.Judul)

    class Meta:
        verbose_name_plural = "Jadwal Kuliah"

class Roadmap_Penelitian(models.Model):
    
    file_pdf = models.FileField(upload_to=_upload_path, validators=[
                                FileExtensionValidator(['jpg','png']), file_size])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_upload_path(self, filename):
        return "uploads/Roadmap_Penelitian"+"/"+filename

    def __str__(self):
        return str(self.file_pdf)

    class Meta:
        verbose_name_plural = "Roadmap Penelitian"

class Penelitian(models.Model):
    year_dropdown = []
    for y in range(2011, (datetime.datetime.now().year + 1)):
        year_dropdown.append((y, y))

    dosen = models.ForeignKey(Dosen, on_delete=models.CASCADE)
    tahun = models.IntegerField(('tahun'), choices=year_dropdown, default=datetime.datetime.now().year)
    judul = models.CharField(max_length=500)
    sumber = models.CharField(max_length=200)
    jumlah = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.judul)

    class Meta:
        verbose_name_plural = "Penelitian"
    

class Pengabdian(models.Model):
    year_dropdown = []
    for y in range(2011, (datetime.datetime.now().year + 1)):
        year_dropdown.append((y, y))

    tahun = models.IntegerField(
        ('tahun'), choices=year_dropdown, default=datetime.datetime.now().year)
    judul = models.CharField(max_length=50)
    file_pdf = models.FileField(upload_to=_upload_path, validators=[
                                FileExtensionValidator(['pdf']), file_size])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_upload_path(self, filename):
        return "uploads/Pengabdian"+"/"+filename

    def __str__(self):
        return str(self.judul)

    class Meta:
        verbose_name_plural = "Pengabdian"

class Jurnal(models.Model):
    year_dropdown = []
    for y in range(2011, (datetime.datetime.now().year + 1)):
        year_dropdown.append((y, y))

    tahun = models.IntegerField(
        ('tahun'), choices=year_dropdown, default=datetime.datetime.now().year)
    judul = models.CharField(max_length=50)
    file_pdf = models.FileField(upload_to=_upload_path, validators=[
                                FileExtensionValidator(['pdf']), file_size])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_upload_path(self, filename):
        return "uploads/jurnal"+"/"+filename

    def __str__(self):
        return str(self.judul)

    class Meta:
        verbose_name_plural = "Jurnal"


class Fasilitas(models.Model):
    TINGKAT_TYPE_CHOICES = (
        (1, 'Ruangan'),
        (2, 'Ruang Baca'),
        (3, 'Laboratorium'),
        (3, 'Fasilitas Pendukung'),
    )
    jenis = models.PositiveIntegerField(choices=TINGKAT_TYPE_CHOICES, default=1)
    nama = models.CharField(max_length=50)
    keterangan = HTMLField()
    gambar = models.FileField(upload_to=_upload_path, validators=[FileExtensionValidator(['jpg','png']), file_size])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_upload_path(self, filename):
        return "uploads/Fasilitas"+"/"+filename
    def __str__(self):
        return str(self.jenis)+"-"+str(self.nama)

    class Meta:
        verbose_name_plural = "Fasilitas"


class Beasiswa(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = HTMLField()
    gambar = models.FileField(upload_to=_upload_path, validators=[
                              FileExtensionValidator(['jpg','png','pdf']), file_size])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_upload_path(self, filename):
        return "uploads/beasiswa"+"/"+filename

    def __str__(self):
        return str(self.nama)

    class Meta:
        verbose_name_plural = "Beasiswa"

class Kegiatan(models.Model):

    tgl_kegiatan = models.DateField(('tanggal kegiatan'))
    waktu_kegiatan = models.TimeField(('waktu kegiatan'))
    nama = models.CharField(max_length=50)
    
    gambar = models.FileField(upload_to=_upload_path, validators=[
                              FileExtensionValidator(['jpg', 'png']), file_size])
    keterangan = HTMLField(blank=True, null=True, )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_upload_path(self, filename):
        return "uploads/kegiatan"+"/"+filename

    def __str__(self):
        return str(self.nama)

    class Meta:
        verbose_name_plural = "Kegiatan"

class Berita(models.Model):
    Judul = models.CharField(max_length=100)
    isi_berita = HTMLField()
    gambar = models.FileField(upload_to=_upload_path, validators=[FileExtensionValidator(['jpg']), file_size])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_upload_path(self, filename):
        return "uploads/berita"+"/"+filename

    def __str__(self):
        return str(self.Judul)

    class Meta:
        verbose_name_plural = "Berita"

