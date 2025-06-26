from pembayaran_interface import Pembayaran

class KartuKredit(Pembayaran):
    def __init__(self):
        self.__jumlah = 0
        self.__biaya_admin = 0.03

    def set_jumlah(self, jumlah):
        if jumlah >= 0:
            self.__jumlah = jumlah
        else:
            raise ValueError("Jumlah tidak boleh negatif.")

    def get_jumlah(self):
        return self.__jumlah

    def proses_pembayaran(self, jumlah):
        self.set_jumlah(jumlah)
        admin = self.__biaya_admin * self.__jumlah
        total = self.__jumlah + admin
        print(f"[Kartu Kredit] Biaya admin 3%. Total: Rp{total:.2f} (admin: Rp{admin:.2f})")
