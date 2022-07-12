from django.contrib import admin

# Register your models here.
from .models import statistik_mhs,Jurnal,Jadwal_kuliah,prestasi_mhs,Lembaga_mhs,Kalender_akademik, Kegiatan, Beasiswa, Akreditasi,Profil, Sejarah, Visimisi, Dosen, Tendik, SOP, Persyaratan, Kurikulum, Penelitian, Roadmap_Penelitian, Penelitian, Pengabdian, Jurnal, Fasilitas, Berita
# Register your models here.

admin.site.register(Profil)
admin.site.register(Sejarah)
admin.site.register(Visimisi)
admin.site.register(Dosen)
admin.site.register(Tendik)
admin.site.register(SOP)
admin.site.register(Persyaratan)
admin.site.register(Kurikulum)
admin.site.register(Akreditasi)
admin.site.register(Roadmap_Penelitian)
admin.site.register(Penelitian)
admin.site.register(Pengabdian)
admin.site.register(Fasilitas)
admin.site.register(Kegiatan)
admin.site.register(Beasiswa)
admin.site.register(Berita)
admin.site.register(Kalender_akademik)
admin.site.register(Lembaga_mhs)
admin.site.register(prestasi_mhs)
admin.site.register(Jadwal_kuliah)
admin.site.register(Jurnal)
admin.site.register(statistik_mhs)
