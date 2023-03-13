import os
class AkunBank:
    list_pelanggan = 0
    
    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.no_pelanggan = no_pelanggan
        self.nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        AkunBank.list_pelanggan += 1
        
    def lihat_menu():
        print("Welcome to Bank BingBung")
        print("Halo,", Akun1.nama_pelanggan, "Silahkan pilih menu dibawah ini")
        print("1. Lihat Saldo")
        print("2. Tarik Tunai")
        print("3. Transfer")
        print("4. Keluar")
        masukkan = int(input("Masukkan pilihan anda: "))
        print()
        if masukkan == 1:
            AkunBank.lihat_saldo()
        elif masukkan == 2:
            AkunBank.tarik_tunai()
        elif masukkan == 3:
            AkunBank.transfer()
        elif masukkan == 4:
            print("Thank You!")
        print()
        AkunBank.lihat_menu()
            
    def lihat_saldo():
        print(f"{Akun1.nama_pelanggan} memiliki saldo Rp {Akun1.__jumlah_saldo}")
        
    def tarik_tunai():
        while True:
            jumlah_tarik = int(input("Masukan jumlah nominal yang ingin ditarik : "))

            if jumlah_tarik > Akun1.__jumlah_saldo:
                print("Nominal saldo yang Anda punya tidak cukup!")
            else:
                Akun1.__jumlah_saldo -= jumlah_tarik
                print("Saldo berhasil ditarik!")
                break
        
    def transfer():
        transfer = int(input("Masukkan jumlah nominal yang ingin ditransfer: "))
        tujuan = int(input("Masukkan nomor rekening tujuan: "))
        
        if tujuan == Akun2.no_pelanggan:
            Akun2.__jumlah_saldo += transfer
            Akun1.__jumlah_saldo -= transfer
            print(f"Transfer Rp{transfer} ke {Akun2.nama_pelanggan} sukses!")
        else:
            print("No rekening tujuan tidak dikenal! Kembali ke menu utama")
        if tujuan == Akun3.no_pelanggan:
            Akun3.__jumlah_saldo += transfer
            Akun1.__jumlah_saldo -= transfer
            print(f"Transfer Rp{transfer} ke {Akun3.nama_pelanggan} sukses!")
        

os.system("cls")        
Akun1 = AkunBank(1234, "Mohamad Meazza Aprilianda", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

AkunBank.lihat_menu()