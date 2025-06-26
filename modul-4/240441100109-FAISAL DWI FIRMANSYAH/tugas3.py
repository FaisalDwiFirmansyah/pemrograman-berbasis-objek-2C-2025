class Pasien:
    def __init__(self, nama, umur, keluhan): 
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def umur(self):
        return self.__umur

    @umur.setter
    def umur(self, value):
        if value >= 0:
            self.__umur = value

    @property
    def keluhan(self):
        return self.__keluhan

    @keluhan.setter
    def keluhan(self, value):
        self.__keluhan = value

class Klinik:
    def __init__(self):  
        self.daftar_pasien = []

    def tambah_pasien(self, nama, umur, keluhan):
        pasien_baru = Pasien(nama, umur, keluhan)
        self.daftar_pasien.append(pasien_baru)
        print(f"Pasien dengan nama {nama} berhasil ditambahkan")

    def tampilkan_pasien(self):
        print("\nDaftar Pasien di Klinik Telang:")
        for i, pasien in enumerate(self.daftar_pasien, start=1):
            print(f"{i}. Nama     : {pasien.nama}")
            print(f"   Umur     : {pasien.umur}")
            print(f"   Keluhan  : {pasien.keluhan}")
            print("-" * 40)


def main():
    klinik = Klinik()
    klinik.tambah_pasien("Zaki", 19, "Ambien")
    klinik.tambah_pasien("Yoga", 20, "Bisulan")
    klinik.tambah_pasien("Wahyu", 20, "Epilepsi")

    klinik.tampilkan_pasien()

main()
