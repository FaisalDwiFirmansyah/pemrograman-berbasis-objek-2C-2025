from mobil import Mobil
from motor import Motor
from sepeda import Sepeda

from tunai import Tunai
from kartu_kredit import KartuKredit
from dompet_digital import DompetDigital

from buku_fiksi import BukuFiksi
from buku_referensi import BukuReferensi

def main():
    print("=== Simulasi Pemesanan Kendaraan ===")
    nama = input("Nama penyewa: ")
    usia = int(input("Usia: "))

    jenis = input("Pilih kendaraan (mobil/motor/sepeda): ").lower()
    if jenis == "mobil":
        kendaraan = Mobil()
    elif jenis == "motor":
        kendaraan = Motor()
    elif jenis == "sepeda":
        kendaraan = Sepeda()
    else:
        print("Jenis kendaraan tidak dikenali.")
        return

    kendaraan.proses_booking(nama, usia)

    print("=== Simulasi Pembayaran ===")
    jumlah = float(input("Masukkan jumlah pembayaran: "))
    metode = input("Pilih metode (tunai/kartu/dompet): ").lower()

    if metode == "tunai":
        metode_pembayaran = Tunai()
    elif metode == "kartu":
        metode_pembayaran = KartuKredit()
    elif metode == "dompet":
        metode_pembayaran = DompetDigital()
    else:
        print("Metode tidak dikenali.")
        return

    metode_pembayaran.proses_pembayaran(jumlah)

    print("\n=== Simulasi Peminjaman Buku ===")
    nama_peminjam = input("Nama peminjam: ")
    jenis_buku = input("Jenis buku (fiksi/referensi): ").lower()

    if jenis_buku == "fiksi":
        buku = BukuFiksi()
    elif jenis_buku == "referensi":
        buku = BukuReferensi()
    else:
        print("Jenis buku tidak dikenali.")
        return

    buku.pinjam(nama_peminjam)
    buku.reservasi(nama_peminjam)

main()
