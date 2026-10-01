class Tugas: 
    def __init__(self, nama, divisi, beban, prioritas): 
        self.nama = nama 
        self.divisi = divisi 
        self.beban = beban 
        self.prioritas = prioritas 
        self.status = "Belum" 
        self.assigned_to = None 
        
    def assign(self, nama_anggota): 
        self.assigned_to = nama_anggota 
        self.status = "Berjalan" 
    
    def selesai(self): 
        self.status = "Selesai"
        
    def batalkan(self): 
        self.status = "Tugas Telah Dibatalkan" 
    
    def tampilkan_detail(self): 
        print(f"Nama : {self.nama}") 
        print(f"Divisi : {self.divisi}") 
        print(f"Beban : {self.beban}") 
        print(f"Prioritas : {self.prioritas}") 
        print(f"Status : {self.status}") 
        print(f"Assigned : {self.assigned_to}")