class Aku:
    def __init__(self, nama, nim, umur, kelas, jumlahsks):
        self.nama = nama
        self.nim = nim
        self.umur = umur
        self.kelas = kelas
        self.jumlahsks = jumlahsks
        
    def data_diri(self):
        return f"Nama: {self.nama},\nNIM: {self.nim},\nUmur: {self.umur},\nKelas: {self.kelas}, \nJumlah SKS: {self.jumlahsks}"

Diri = Aku("Mohamad Meazza Aprilianda", "121140216", 21, "RD", 22)
print(Diri.data_diri())