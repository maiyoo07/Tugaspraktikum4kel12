from src.services.anggota_service import tambah_anggota, cari_anggota, hapus_anggota
from src.services.tugas_service import tambah_tugas, cari_tugas, hapus_tugas
from src.services.allocation_service import analisis_tugas, assign_tugas, selesaikan_tugas, kategori_beban, cek_overload, hitung_beban_setelah
from src.utils.storage import load_data, save_data
from src.utils.input_helper import input_teks, input_angka, input_divisi, input_prioritas, konfirmasi
from src.utils.display import tampilkan_header, tampilkan_menu, tampilkan_anggota, tampilkan_tugas, tampilkan_kandidat, tampilkan_rekomendasi, tampilkan_pesan, pause


def menu_tambah_anggota(daftar_anggota):
    while True :
        print("\n=== TAMBAH ANGGOTA ===")
        nama = input_teks("Nama   : ")
        divisi = input_divisi()
        anggota = tambah_anggota(daftar_anggota, nama, divisi)
        tampilkan_pesan(f"Anggota '{anggota.nama}' Berhasil Ditambahkan.")

        lanjut = input("Tambah Anggota Lagi (y/n)").lower()
        if lanjut=="n" : break


def menu_tambah_tugas(daftar_tugas):
    while True : 
        print("\n=== TAMBAH TUGAS ===")
        nama = input_teks("Nama tugas : ")
        divisi = input_divisi()
        beban = input_angka("Beban      : ", minimum=1)
        prioritas = input_prioritas()
        tugas = tambah_tugas( daftar_tugas, nama, divisi, beban, prioritas)
        tampilkan_pesan(f"Tugas '{tugas.nama}' Berhasil Ditambahkan.")

        lanjut = input("Tambah Tugas Lagi (y/n) : ").lower()
        if lanjut=="n" : break


def menu_cari_kandidat(daftar_anggota, daftar_tugas):
    print("\n=== CARI KANDIDAT ===")
    nama_tugas = input_teks("Nama tugas: ")
    tugas = cari_tugas(daftar_tugas, nama_tugas)

    if tugas is None:
        tampilkan_pesan("Tugas Tidak Ditemukan.")
        return

    hasil = analisis_tugas(daftar_anggota, tugas)

    if not hasil["berhasil"]:
        tampilkan_pesan(hasil["pesan"])
        return

    tampilkan_kandidat(hasil["kandidat"])
    tampilkan_rekomendasi(hasil["rekomendasi_aman"], tugas)


def menu_assign_tugas(daftar_anggota, daftar_tugas):
    print("\n=== ASSIGN TUGAS ===")
    nama_tugas = input_teks("Nama Tugas: ")
    tugas = cari_tugas(daftar_tugas, nama_tugas)

    if tugas is None:
        tampilkan_pesan("Tugas Tidak Ditemukan.")
        return

    if tugas.assigned_to is not None:
        tampilkan_pesan("Tugas Sudah Diberikan Kepada Anggota.")
        return

    hasil = analisis_tugas(daftar_anggota, tugas)

    if not hasil["berhasil"]:
        tampilkan_pesan(hasil["pesan"])
        return

    kandidat = hasil["kandidat"]
    rekomendasi = hasil["rekomendasi"]

    print("\nKANDIDAT ANGGOTA")
    print("-" * 40)

    for nomor, anggota in enumerate(kandidat, start=1):
        print(
            f"{nomor}. {anggota.nama} "
            f"| Divisi: {anggota.divisi} "
            f"| Beban: {anggota.beban}"
        )

    print("\nREKOMENDASI SISTEM")
    print("-" * 40)

    print(f"Anggota : {rekomendasi.nama}")
    print(f"Beban   : {rekomendasi.beban}")
    print(
        f"Setelah : "
        f"{hitung_beban_setelah(rekomendasi, tugas)}"
    )

    print("\nOpsi :")
    print("1. Tugaskan Anggota Rekomendasi")
    print("2. Pilih Anggota Lain")
    print("3. Batal")

    pilihan = input_angka(
        "Pilihan: ",
        minimum=1,
        maksimum=3
    )

    if pilihan == 3:
        tampilkan_pesan("Penugasan Dibatalkan.")
        return

    if pilihan == 1:
        anggota = rekomendasi

    else:
        nomor = input_angka(
            "Pilih Nomor Kandidat: ",
            minimum=1,
            maksimum=len(kandidat)
        )
        anggota = kandidat[nomor - 1]

    beban_setelah = hitung_beban_setelah(anggota, tugas)

    print("\nDETAIL ASSIGNMENT")
    print("-" * 40)
    print(f"Anggota       : {anggota.nama}")
    print(f"Beban Sekarang: {anggota.beban}")
    print(f"Beban Tugas   : {tugas.beban}")
    print(f"Beban Setelah : {beban_setelah}")
    print(f"Kategori      : {kategori_beban(beban_setelah)}")

    if cek_overload(anggota, tugas):
        print("\nPERINGATAN: Beban Anggota Akan Melebihi Batas.")
        konfirmasi = input_teks("Tetap Tugaskan? (y/n): ").lower()

        if konfirmasi != "y":
            tampilkan_pesan("Penugasan Dibatalkan.")
            return

    else:
        konfirmasi = input_teks("Tugaskan Kepada Anggota Ini? (y/n): ").lower()

        if konfirmasi != "y":
            tampilkan_pesan("Penugasan Dibatalkan.")
            return

    berhasil = assign_tugas(tugas, anggota)

    if berhasil:
        tampilkan_pesan(
            f"Tugas '{tugas.nama}' Berhasil "
            f"Ditugaskan Kepada {anggota.nama}."
        )
    else:
        tampilkan_pesan("Tugas Gagal Diberikan.")


def menu_selesaikan_tugas(daftar_anggota, daftar_tugas, riwayat_tugas):
    print("\n=== SELESAIKAN TUGAS ===")
    nama_tugas = input_teks("Nama Tugas: ")
    tugas = cari_tugas(daftar_tugas, nama_tugas)

    if tugas is None:
        tampilkan_pesan("Tugas Tidak Ditemukan.")
        return

    if tugas.assigned_to is None:
        tampilkan_pesan("Tugas Belum Diberikan Kepada Anggota.")
        return

    anggota = cari_anggota(daftar_anggota, tugas.assigned_to)

    if anggota is None:
        tampilkan_pesan("Anggota Yang Mengerjakan Tugas Tidak Ditemukan.")
        return

    berhasil = selesaikan_tugas(tugas, anggota, daftar_tugas, riwayat_tugas)

    if berhasil:
        tampilkan_pesan(f"Tugas '{tugas.nama}' Telah Diselesaikan. '{tugas.nama}' Akan Dihapus Dari Daftar Tugas")
    else:
        tampilkan_pesan("Tugas Gagal Diselesaikan.")


def menu_hapus_anggota(daftar_anggota):
    print("\n=== HAPUS ANGGOTA ===")
    nama = input_teks("Nama Anggota: ")
    anggota = cari_anggota(daftar_anggota, nama)

    if anggota is None:
        tampilkan_pesan("Anggota Tidak Ditemukan.")
        return

    if anggota.tugas:
        tampilkan_pesan(
            "Anggota Masih Memiliki Tugas. "
            "Selesaikan Atau Batalkan Tugas Terlebih Dahulu."
        )
        return

    if not konfirmasi(f"Hapus Anggota '{anggota.nama}'?"):
        tampilkan_pesan("Penghapusan Dibatalkan.")
        return

    berhasil = hapus_anggota(daftar_anggota, nama)

    if berhasil:
        tampilkan_pesan("Anggota Berhasil Dihapus.")
    else:
        tampilkan_pesan("Anggota Gagal Dihapus.")


def menu_hapus_tugas(daftar_tugas):
    print("\n=== HAPUS TUGAS ===")
    nama = input_teks("Nama tugas: ")
    tugas = cari_tugas(daftar_tugas, nama)

    if tugas is None:
        tampilkan_pesan("Tugas Tidak Ditemukan.")
        return

    if tugas.assigned_to is not None:
        tampilkan_pesan(
            "Tugas Yang Sedang Dikerjakan Tidak Dapat Dihapus"
        )
        return

    if not konfirmasi(f"Hapus Tugas '{tugas.nama}'?"):
        tampilkan_pesan("Penghapusan Dibatalkan.")
        return

    berhasil = hapus_tugas(daftar_tugas, nama)

    if berhasil:
        tampilkan_pesan("Tugas Berhasil Dihapus.")
    else:
        tampilkan_pesan("Tugas Gagal Dihapus.")


def main():
    data = load_data()

    daftar_anggota = data["anggota"]
    daftar_tugas = data["tugas"]
    riwayat_tugas = data["riwayat_tugas"]

    while True:

        tampilkan_header()
        tampilkan_menu()

        pilihan = input_angka(
            "\nPilih Menu: ",
            minimum=0,
            maksimum=9
        )

        if pilihan == 1:
            menu_tambah_anggota(daftar_anggota)

        elif pilihan == 2:
            menu_tambah_tugas(daftar_tugas)

        elif pilihan == 3:
            tampilkan_anggota(daftar_anggota)

        elif pilihan == 4:
            tampilkan_tugas(daftar_tugas, riwayat_tugas)

        elif pilihan == 5:
            menu_cari_kandidat(daftar_anggota, daftar_tugas)

        elif pilihan == 6:
            menu_assign_tugas(daftar_anggota, daftar_tugas)

        elif pilihan == 7:
            menu_selesaikan_tugas(daftar_anggota, daftar_tugas, riwayat_tugas)

        elif pilihan == 8:
            menu_hapus_anggota(daftar_anggota)

        elif pilihan == 9:
            menu_hapus_tugas(daftar_tugas)

        elif pilihan == 0:
            save_data(daftar_anggota, daftar_tugas, riwayat_tugas)
            print("\nData berhasil disimpan.")
            print("Program selesai.")
            break

        save_data(daftar_anggota, daftar_tugas, riwayat_tugas)
        pause()

if __name__ == "__main__":
    main()