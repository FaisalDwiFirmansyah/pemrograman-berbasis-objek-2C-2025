from peminjaman_interface import Peminjaman
from reservasi_interface import Reservasi

class BukuFiksi(Peminjaman, Reservasi):
    def pinjam(self, nama):
        print(f"{nama} meminjam buku fiksi.")

    def reservasi(self, nama):
        print(f"{nama} mereservasi buku fiksi.")
