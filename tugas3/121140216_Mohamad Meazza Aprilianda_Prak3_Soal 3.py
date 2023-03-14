<<<<<<< HEAD
class Karyawan:
    # atribut kelas
    perusahaan = "PT Kocak Gaming"

    def __init__(self, nama, gaji):
        self.__nama = nama  # atribut private
        self._gaji = gaji  # atribut protected
        self.bonus = 0  # atribut public

    # fungsi kelas
    @classmethod
    def perusahaan_info(cls):
        print(f"Perusahaan {cls.perusahaan} adalah sebuah perusahaan internasional yang bergerak di bidang teknologi dan game.")

    # method public
    def tambah_bonus(self, jumlah):
        self.bonus += jumlah

    # method protected
    def _hitung_gaji_bersih(self):
        return self._gaji + self.bonus

    # method private
    def __hitung_pajak(self):
        return self._hitung_gaji_bersih() * 0.1

    # method public
    def cetak_info_karyawan(self):
        print(f"Nama karyawan: {self.__nama}")
        print(f"Gaji pokok: {self._gaji}")
        print(f"Bonus: {self.bonus}")
        print(f"Gaji bersih: {self._hitung_gaji_bersih()}")
        print(f"Pajak: {self.__hitung_pajak()}")

Pekerja = Karyawan("Meazza", 10000000)
Pekerja.perusahaan_info()
Pekerja.tambah_bonus(1000000)
=======
class Karyawan:
    # atribut kelas
    perusahaan = "PT Kocak Gaming"

    def __init__(self, nama, gaji):
        self.__nama = nama  # atribut private
        self._gaji = gaji  # atribut protected
        self.bonus = 0  # atribut public

    # fungsi kelas
    @classmethod
    def perusahaan_info(cls):
        print(f"Perusahaan {cls.perusahaan} adalah sebuah perusahaan internasional yang bergerak di bidang teknologi dan game.")

    # method public
    def tambah_bonus(self, jumlah):
        self.bonus += jumlah

    # method protected
    def _hitung_gaji_bersih(self):
        return self._gaji + self.bonus

    # method private
    def __hitung_pajak(self):
        return self._hitung_gaji_bersih() * 0.1

    # method public
    def cetak_info_karyawan(self):
        print(f"Nama karyawan: {self.__nama}")
        print(f"Gaji pokok: {self._gaji}")
        print(f"Bonus: {self.bonus}")
        print(f"Gaji bersih: {self._hitung_gaji_bersih()}")
        print(f"Pajak: {self.__hitung_pajak()}")

Pekerja = Karyawan("Meazza", 10000000)
Pekerja.perusahaan_info()
Pekerja.tambah_bonus(1000000)
>>>>>>> 859d02f9ad20b3e4290e08d66a5d07e17475e561
Pekerja.cetak_info_karyawan()