from django.shortcuts import render
from . import views
from . import models
from django.db.models import Count
import datetime
# Create your views here.


def index(request):
    beritas = models.Berita.objects.all().latest('updated_at')
    list_beritas = models.Berita.objects.all().order_by('-created_at')[:3] 
    dosens = models.Dosen.objects.all()[:3]
    jml_dosens = models.Dosen.objects.all().count()
    kegiatans = models.Kegiatan.objects.filter(tgl_kegiatan__gte=datetime.datetime.today()).order_by('tgl_kegiatan')[:3]
    context = {
        'rows': beritas,
        'rows1': list_beritas,
        'rows2': dosens,
        'rows3': kegiatans,
        'rows4': jml_dosens,
    }
    return render(request, 'website/index.html', context)


def profiljurusan(request):
    profils = models.Profil.objects.all().latest('created_at')
    context = {
        'rows': profils,
    }
    return render(request, 'website/profil_jurusan.html', context)


def visimisi_jurusan(request):
    visi = models.Visimisi.objects.filter(Judul='1',tingkat='1').latest('created_at')
    misi = models.Visimisi.objects.filter(Judul='2',tingkat='1').latest('created_at')
    tujuan = models.Visimisi.objects.filter(Judul='3',tingkat='1').latest('created_at')
    context = {
        'rows': visi,
        'rows1': misi,
        'rows2': tujuan,
    }
    return render(request, 'website/visimisi_jurusan.html', context)


def sejarah_jurusan(request):
    sejarahs = models.Sejarah.objects.all().latest('created_at')
    context = {
        'rows': sejarahs,
    }
    return render(request, 'website/sejarah_jurusan.html', context)


def list_dosen(request):
    dosens = models.Dosen.objects.all()
    context = {
        'rows': dosens,
    }
    return render(request, 'website/list_dosen.html', context)


def detail_dosen(request, pk):
    dosens = models.Dosen.objects.get(id=pk)
    context = {
        'rows': dosens,
    }
    return render(request, 'website/detail_dosen.html', context)


def list_tendik(request):
    tendiks = models.Tendik.objects.all()
    context = {
        'rows': tendiks,
    }
    return render(request, 'website/list_tendik.html', context)


def detail_tendik(request, pk):
    tendiks = models.Tendik.objects.get(id=pk)
    context = {
        'rows': tendiks,
    }
    return render(request, 'website/detail_tendik.html', context)

def sop_persyaratan(request):
    sops = models.SOP.objects.filter(tingkat='1')
    persyaratans = models.Persyaratan.objects.filter(tingkat='1')
    context = {
        'rows': sops,
        'rows1': persyaratans,
    }
    return render(request, 'website/sop_persyaratan.html', context)


def lembaga_mhs(request):
    try:
        Lembaga_mhss = models.Lembaga_mhs.objects.all().latest('created_at')
    except models.Lembaga_mhs.DoesNotExist:
        Lembaga_mhss = None
    
    context = {
        'rows': Lembaga_mhss,
    }
    return render(request, 'website/lembaga_mhs.html', context)


def prestasi_mhs(request):
    try:
        prestasi_mhss = models.prestasi_mhs.objects.all().order_by('created_at')
    except models.Lembaga_mhs.DoesNotExist:
        prestasi_mhss = None
    
    context = {
        'rows': prestasi_mhss,
    }
    return render(request, 'website/prestasi_mhs.html', context)


def statistik_mhs(request):
    
    try:
        statistik_mhss = models.statistik_mhs.objects.all().order_by('-tahun')
    except models.Lembaga_mhs.DoesNotExist:
        statistik_mhss = None
    context = {
        'rows': statistik_mhss,
    }
    return render(request, 'website/statistik_mhs.html', context)

def kurikulum(request):
    semester1 = models.Kurikulum.objects.filter(semester='1')
    semester2 = models.Kurikulum.objects.filter(semester='2')
    semester3 = models.Kurikulum.objects.filter(semester='3')
    semester4 = models.Kurikulum.objects.filter(semester='4')
    semester5 = models.Kurikulum.objects.filter(semester='5')
    semester6 = models.Kurikulum.objects.filter(semester='6')
    semester7 = models.Kurikulum.objects.filter(semester='7')
    semester8 = models.Kurikulum.objects.filter(semester='8')
    context = {
        'rows1': semester1,
        'rows2': semester2,
        'rows3': semester3,
        'rows4': semester4,
        'rows5': semester5,
        'rows6': semester6,
        'rows7': semester7,
        'rows8': semester8,
    }
    return render(request, 'website/kurikulum.html', context)


def akreditasi(request):
    try:
        akreditasis1 = models.Akreditasi.objects.filter(jenis='1').latest('created_at')
    except models.Akreditasi.DoesNotExist:
        akreditasis1 = None

    try:
        akreditasis2 = models.Akreditasi.objects.filter(jenis='2').latest('created_at')
    except models.Akreditasi.DoesNotExist:
        akreditasis2 = None

    try:
        akreditasis3 = models.Akreditasi.objects.filter(jenis='3').latest('created_at')
    except models.Akreditasi.DoesNotExist:
        akreditasis3 = None

    try:
        akreditasisk = models.Akreditasi.objects.filter(jenis='4').latest('created_at')
    except models.Akreditasi.DoesNotExist:
        akreditasisk = None
    context = {
        'rows1': akreditasis1,
        'rows2': akreditasis2,
        'rows3': akreditasis3,
        'rows4': akreditasisk,
    }
    return render(request, 'website/akreditasi.html', context)


def kalender_akademik(request):
    try:
        Kalender_akademiks = models.Kalender_akademik.objects.all().latest('created_at')
    except models.Kalender_akademik.DoesNotExist:
        Kalender_akademiks = None

    
    context = {
        'rows1': Kalender_akademiks,
    }
    return render(request, 'website/kalender_akademik.html', context)


def jadwal_kuliah(request):
    try:
        jadwals = models.Jadwal_kuliah.objects.all().latest('created_at')
    except models.Jadwal_kuliah.DoesNotExist:
        jadwals = None

    context = {
        'rows1': jadwals,
    }
    return render(request, 'website/jadwal.html', context)


def roadmap(request):
    profils = models.Roadmap_Penelitian.objects.all().latest('created_at')
    context = {
        'rows': profils,
    }
    return render(request, 'website/roadmap_penelitian.html', context)


def penelitian_dosen(request):
    penelitians =models.Penelitian.objects.all().values('tahun').annotate(total=Count('tahun')).order_by('tahun')
    context = {
        'rows': penelitians,
    }
    return render(request, 'website/penelitian.html', context)


def detail_penelitian(request, pk):
    penelitians = models.Penelitian.objects.filter(tahun=pk)
    context = {
        'rows': penelitians,
    }
    return render(request, 'website/detail_penelitian.html', context)

def pengabdian_dosen(request):
    pengabdians = models.Pengabdian.objects.all().order_by('tahun')
    context = {
        'rows': pengabdians,
    }
    return render(request, 'website/pengabdian.html', context)


def jurnal(request):
    jurnals = models.Jurnal.objects.all().order_by('tahun')
    context = {
        'rows': jurnals,
    }
    return render(request, 'website/pengabdian.html', context)


def fasilitas_ruangan(request, pk):
    fasilitass = models.Fasilitas.objects.filter(jenis=pk)
    context = {
        'rows': fasilitass,
    }
    return render(request, 'website/fasilitas.html', context)


def kegiatan(request):
    kegiatans = models.Kegiatan.objects.filter(tgl_kegiatan__gte=datetime.datetime.today()).order_by('tgl_kegiatan')
    context = {
        'rows': kegiatans,
    }
    return render(request, 'website/kegiatan.html', context)


def detail_kegiatan(request, pk):
    kegiatans = models.Kegiatan.objects.get(id=pk)
    context = {
        'rows': kegiatans,
    }
    return render(request, 'website/detail_kegiatan.html', context)


def beasiswa(request):
    beasiswas = models.Beasiswa.objects.all().order_by('created_at')
    context = {
        'rows': beasiswas,
    }
    return render(request, 'website/beasiswa.html', context)

def berita(request):
    beritas = models.Berita.objects.all().order_by('created_at')
    context = {
        'rows': beritas,
    }
    return render(request, 'website/berita.html', context)


def detail_berita(request, pk):
    beritas = models.Berita.objects.get(id=pk)
    context = {
        'rows': beritas,
    }
    return render(request, 'website/detail_berita.html', context)
