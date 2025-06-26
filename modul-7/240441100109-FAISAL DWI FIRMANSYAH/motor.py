from booking_interface import Booking

class Motor(Booking):
    def proses_booking(self, nama, usia):
        if usia < 16:
            print(f"{nama} belum cukup umur untuk menyewa motor.")
        else:
            print(f"{nama} berhasil memesan motor.")
