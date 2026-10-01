from src.models.Anggota import Anggota

def tambah_anggota(daftar_anggota, nama, divisi):
    anggota_baru = Anggota(nama, divisi)
    daftar_anggota.append(anggota_baru)
    return anggota_baru

def cari_anggota(daftar_anggota, nama):
    for anggota in daftar_anggota:
        if anggota.nama.lower() == nama.lower():
            return anggota
    return None

def hapus_anggota(daftar_anggota, nama):
    anggota = cari_anggota(daftar_anggota, nama)
    if anggota is None:
        return False
    daftar_anggota.remove(anggota)
    return True