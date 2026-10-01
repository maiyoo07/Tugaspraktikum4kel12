class Anggota:
    def __init__(self, nama, divisi):
        self.nama = nama
        self.divisi = divisi
        self.beban = 0
        self.tugas = []

    def tambah_beban(self, beban):
        self.beban += beban

    def kurangi_beban(self, beban):
        self.beban -= beban

    def tambah_tugas(self, tugas):
        self.tugas.append(tugas)

    def hapus_tugas(self, tugas):
        if tugas in self.tugas:
            self.tugas.remove(tugas)

    def tampilkan_profil(self):
        print(f"Nama   : {self.nama}")
        print(f"Divisi : {self.divisi}")
        print(f"Beban  : {self.beban}")
        print(f"Tugas  : {len(self.tugas)}")