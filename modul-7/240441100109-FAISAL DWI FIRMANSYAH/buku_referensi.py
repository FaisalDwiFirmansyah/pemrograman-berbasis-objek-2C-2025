from peminjaman_interface import Peminjaman
from reservasi_interface import Reservasi

class BukuReferensi(Peminjaman, Reservasi):
    def pinjam(self, nama):
        print("Maaf, buku referensi tidak dapat dipinjam.")

    def reservasi(self, nama):
        print(f"{nama} mereservasi buku referensi.")
