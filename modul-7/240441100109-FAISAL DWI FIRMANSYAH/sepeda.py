from booking_interface import Booking

class Sepeda(Booking):
    def proses_booking(self, nama, usia):
        print(f"{nama} berhasil memesan sepeda.")
