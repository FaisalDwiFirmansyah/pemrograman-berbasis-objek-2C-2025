from booking_interface import Booking

class Mobil(Booking):
    def proses_booking(self, nama, usia):
        if usia < 17:
            print(f"{nama} belum cukup umur untuk menyewa mobil.")
        else:
            print(f"{nama} berhasil memesan mobil.")
