from src.models.Tugas import Tugas

def tambah_tugas(daftar_tugas, nama, divisi, beban, prioritas):
    tugas_baru = Tugas(
        nama,
        divisi,
        beban,
        prioritas
    )
    daftar_tugas.append(tugas_baru)
    return tugas_baru

def cari_tugas(daftar_tugas, nama):
    for tugas in daftar_tugas:
        if tugas.nama.lower() == nama.lower():
            return tugas
    return None

def hapus_tugas(daftar_tugas, nama):
    tugas = cari_tugas(daftar_tugas, nama)
    if tugas is None:
        return False

    daftar_tugas.remove(tugas)
    return True