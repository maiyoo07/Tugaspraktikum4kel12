def cari_kandidat(daftar_anggota, tugas):
    kandidat = []

    for anggota in daftar_anggota:
        if anggota.divisi.lower() == tugas.divisi.lower():
            kandidat.append(anggota)
    return kandidat

def hitung_beban_setelah(anggota, tugas):
    return anggota.beban + tugas.beban

def kategori_beban(beban):
    if beban <= 4:
        return "Ringan"
    elif beban <= 8:
        return "Sedang"
    else:
        return "Tinggi"

def cek_overload(anggota, tugas, batas_beban=10):
    beban_setelah = hitung_beban_setelah(anggota, tugas)
    if beban_setelah > batas_beban:
        return True
    return False

def cari_rekomendasi(kandidat):
    if len(kandidat) == 0:
        return None

    rekomendasi = kandidat[0]
    for anggota in kandidat:
        if anggota.beban < rekomendasi.beban:
            rekomendasi = anggota
    return rekomendasi

def cari_rekomendasi_aman(kandidat, tugas, batas_beban=8):
    kandidat_aman = []
    for anggota in kandidat:
        if not cek_overload(anggota, tugas, batas_beban):
            kandidat_aman.append(anggota)
    return cari_rekomendasi(kandidat_aman)

def analisis_tugas(daftar_anggota, tugas, batas_beban=8):
    kandidat = cari_kandidat(daftar_anggota, tugas)

    if len(kandidat) == 0:
        return {
            "berhasil": False,
            "pesan": "Tidak ada anggota pada divisi yang sesuai.",
            "kandidat": [],
            "rekomendasi": None
        }

    rekomendasi = cari_rekomendasi(kandidat)
    rekomendasi_aman = cari_rekomendasi_aman(
        kandidat,
        tugas,
        batas_beban
    )

    return {
        "berhasil": True,
        "pesan": "Kandidat berhasil ditemukan.",
        "kandidat": kandidat,
        "rekomendasi": rekomendasi,
        "rekomendasi_aman": rekomendasi_aman
    }

def assign_tugas(tugas, anggota):
    if tugas.assigned_to is not None:
        return False

    tugas.assign(anggota.nama)

    anggota.tambah_beban(tugas.beban)
    anggota.tambah_tugas(tugas)

    return True

def batalkan_assignment(tugas, anggota):
    if tugas.assigned_to != anggota.nama:
        return False
    anggota.kurangi_beban(tugas.beban)
    anggota.hapus_tugas(tugas)
    tugas.assigned_to = None
    tugas.status = "Belum"
    return True

def selesaikan_tugas(tugas, anggota, daftar_tugas, riwayat_tugas):
    if tugas.assigned_to != anggota.nama:
        return False

    riwayat_tugas.append({
        "nama": tugas.nama,
        "divisi": tugas.divisi,
        "beban": tugas.beban,
        "prioritas": tugas.prioritas,
        "assigned_to": tugas.assigned_to
    })

    anggota.kurangi_beban(tugas.beban)
    anggota.hapus_tugas(tugas)
    daftar_tugas.remove(tugas)

    return True