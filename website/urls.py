from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('profiljurusan', views.profiljurusan, name='profiljurusan'),
    path('visimisi', views.visimisi_jurusan, name='visimisi'),
    path('sejarah', views.sejarah_jurusan, name='sejarah'),
    path('dosen', views.list_dosen, name='dosen'),
    path('detail_dosen/<int:pk>', views.detail_dosen, name='detail_dosen'),
    path('tendik', views.list_tendik, name='tendik'),
    path('detail_tendik/<int:pk>', views.detail_tendik, name='detail_tendik'),
    path('lembaga_mhs', views.lembaga_mhs, name='lembaga_mhs'),
    path('prestasi_mhs', views.prestasi_mhs, name='prestasi_mhs'),
    path('statistik_mhs', views.statistik_mhs, name='statistik_mhs'),
    path('sop_persyaratan', views.sop_persyaratan, name='sop_persyaratan'),
    path('kurikulum', views.kurikulum, name='kurikulum'),
    path('akreditasi', views.akreditasi, name='akreditasi'),
    path('roadmap', views.roadmap, name='roadmap'),
    path('penelitian_dosen', views.penelitian_dosen, name='penelitian_dosen'),
    path('detail_penelitian/<int:pk>', views.detail_penelitian, name='detail_penelitian'),
    path('pengabdian_dosen', views.pengabdian_dosen, name='pengabdian_dosen'),
    path('jurnal', views.jurnal, name='jurnal'),
    path('fasilitas/<int:pk>', views.fasilitas_ruangan, name='fasilitas'),
    path('kegiatan', views.kegiatan, name='kegiatan'),
    path('detail_kegiatan/<int:pk>', views.detail_kegiatan, name='detail_kegiatan'),
    path('beasiswa', views.beasiswa, name='beasiswa'),
    path('berita', views.berita, name='berita'),
    path('detail_berita/<int:pk>', views.detail_berita, name='detail_berita'),
    path('kalender_akademik', views.kalender_akademik, name='kalender_akademik'),
    path('jadwal_kuliah', views.jadwal_kuliah, name='jadwal_kuliah'),
]