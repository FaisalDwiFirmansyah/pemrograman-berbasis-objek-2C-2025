from pembayaran_interface import Pembayaran

class DompetDigital(Pembayaran):
    def __init__(self):
        self.__jumlah = 0
        self.__diskon = 0.05

    def set_jumlah(self, jumlah):
        if jumlah >= 0:
            self.__jumlah = jumlah
        else:
            raise ValueError("Jumlah tidak boleh negatif.")

    def get_jumlah(self):
        return self.__jumlah

    def proses_pembayaran(self, jumlah):
        self.set_jumlah(jumlah)
        potongan = self.__diskon * self.__jumlah
        total = self.__jumlah - potongan
        print(f"[Dompet Digital] Potongan 5%. Total: Rp{total:.2f} (diskon: Rp{potongan:.2f})")

