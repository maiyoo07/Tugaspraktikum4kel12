import time

def tampilkan_header():
    print("\n" + "=" * 55)
    print("       SISTEM PENUGASAN DIGITAL UNTUK EVENT")
    print("                    KELOMPOK 12")
    print("=" * 55)

def tampilkan_menu():
    print("\n" + "-" * 55)
    print("MENU UTAMA")
    print("-" * 55)

    print("1. Tambah Anggota")
    print("2. Tambah Tugas")
    print("3. Lihat Daftar Anggota")
    print("4. Lihat Daftar Tugas")
    print("5. Cari Kandidat Tugas")
    print("6. Tugaskan Anggota")
    print("7. Tandai Selesai")
    print("8. Hapus Anggota")
    print("9. Hapus Tugas")
    print("0. Keluar")

def tampilkan_anggota(daftar_anggota):
    print("\n" + "=" * 55)
    print("DAFTAR ANGGOTA")
    print("=" * 55)

    if not daftar_anggota:
        print("Belum Ada Anggota.")
        return

    for num, ang in enumerate(daftar_anggota, start=1):
        print(f"\n[{num}]")
        print(f"Nama   : {ang.nama}")
        print(f"Divisi : {ang.divisi}")
        print(f"Beban  : {ang.beban}")
        print(f"Tugas  : {len(ang.tugas)}")


def tampilkan_tugas(daftar_tugas, riwayat_tugas):
    print("\n" + "=" * 55)
    print("DAFTAR TUGAS AKTIF")
    print("=" * 55)

    if not daftar_tugas:
        print("Tidak ada tugas aktif.")
    else:
        for num, tugas in enumerate(daftar_tugas, start=1):
            print(f"\n[{num}]")
            print(f"Nama      : {tugas.nama}")
            print(f"Divisi    : {tugas.divisi}")
            print(f"Beban     : {tugas.beban}")
            print(f"Prioritas : {tugas.prioritas}")
            print(f"Status    : {tugas.status}")
            print(f"Assigned  : {tugas.assigned_to}")

    print("\n" + "=" * 55)
    print("RIWAYAT TUGAS SELESAI")
    print("=" * 55)

    if not riwayat_tugas:
        print("Belum ada tugas yang selesai.")
    else:
        for num, tugas in enumerate(riwayat_tugas, start=1):
            print(f"\n[{num}]")
            print(f"Nama      : {tugas['nama']}")
            print(f"Divisi    : {tugas['divisi']}")
            print(f"Beban     : {tugas['beban']}")
            print(f"Prioritas : {tugas['prioritas']}")
            print(f"Dikerjakan: {tugas['assigned_to']}")

def tampilkan_kandidat(kandidat):
    print("\n" + "=" * 55)
    print("KANDIDAT TUGAS")
    print("=" * 55)

    if not kandidat:
        print("Tidak Ada Kandidat.")
        return

    for num, anggota in enumerate(kandidat, start=1):
        print(
            f"{num}. "
            f"{anggota.nama} | "
            f"Divisi: {anggota.divisi} | "
            f"Beban: {anggota.beban}"
        )

def tampilkan_rekomendasi(anggota, tugas):
    print("\n" + "=" * 55)
    print("REKOMENDASI")
    print("=" * 55)

    if anggota is None:
        print("Tidak Ada Rekomendasi.")
        return

    beban_setelah = anggota.beban + tugas.beban
    print(f"Tugas                    : {tugas.nama}")
    print(f"Kandidat                 : {anggota.nama}")
    print(f"Beban Saat Ini           : {anggota.beban}")
    print(f"Beban Tugas              : {tugas.beban}")
    print(f"Beban Setelah Ditugaskan : {beban_setelah}")

def tampilkan_pesan(pesan):
    print(f"\n{pesan}")

def pause(durasi=3):
    for i in range(durasi, 0, -1) :
        print(f"\rBeralih Ke Menu Utama Dalam {i}...",end="")
        time.sleep(0.5)
