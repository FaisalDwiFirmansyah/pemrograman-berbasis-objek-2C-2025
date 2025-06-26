class Buku:
    def __init__(self, judul, penulis, jumlah_hal):
        self.__judul = judul
        self.__penulis = penulis
        self.__jumlah_hal = jumlah_hal

    @property
    def judul(self):
        return self.__judul

    @judul.setter
    def judul(self, value):
        self.__judul = value

    @property
    def penulis(self):
        return self.__penulis

    @penulis.setter
    def penulis(self, value):
        self.__penulis = value

    @property
    def jumlah_hal(self):
        return self.__jumlah_hal

    @jumlah_hal.setter
    def jumlah_hal(self, value):
        if value > 0:
            self.__jumlah_hal = value

class Perpustakaan:
    def __init__(self): 
        self.daftar_buku = []

    def tambah_buku(self, judul, penulis, jumlah_hal):
        buku_baru = Buku(judul, penulis, jumlah_hal)
        self.daftar_buku.append(buku_baru)
        print(f"Buku '{judul}' berhasil ditambahkan")

    def tampilkan_buku(self):
        print("\nDaftar Buku di Perpustakaan:")
        for i, buku in enumerate(self.daftar_buku, start=1):
            print(f"{i}. Judul           : {buku.judul}")
            print(f"   Penulis         : {buku.penulis}")
            print(f"   Jumlah Halaman  : {buku.jumlah_hal}")
            print("-" * 40)


def main():
    perpustakaan = Perpustakaan()
    perpustakaan.tambah_buku("Kisah Ambaruwo", "Fuad", 333)
    perpustakaan.tambah_buku("Legenda Tung Tung Tung Sahurrr", "Amba", 163)
    perpustakaan.tambah_buku("Solo Leveling", "Sung Jinwoo", 540)

    perpustakaan.tampilkan_buku()
 
main()
