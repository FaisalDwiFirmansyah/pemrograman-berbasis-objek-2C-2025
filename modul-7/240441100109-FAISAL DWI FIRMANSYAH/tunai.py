from pembayaran_interface import Pembayaran

class Tunai(Pembayaran):
    def __init__(self):
        self.__jumlah = 0

    def set_jumlah(self, jumlah):
        if jumlah >= 0:
            self.__jumlah = jumlah
        else:
            raise ValueError("Jumlah tidak boleh negatif.")

    def get_jumlah(self):
        return self.__jumlah

    def proses_pembayaran(self, jumlah):
        self.set_jumlah(jumlah)
        print(f"[Tunai] Pembayaran sebesar Rp{self.get_jumlah():.2f} berhasil.")

