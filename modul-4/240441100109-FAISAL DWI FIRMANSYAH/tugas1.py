class RekeningBank:
    def __init__(self, NoRek, n_pemilik, saldo=0):
        self.__NoRek = NoRek
        self.__n_pemilik = n_pemilik
        self.__saldo = saldo

    @property
    def no_rek(self):
        return self.__NoRek

    @no_rek.setter
    def no_rek(self, value):
        self.__NoRek = value

    @property
    def nama_pemilik(self):
        return self.__n_pemilik

    @nama_pemilik.setter
    def nama_pemilik(self, value):
        self.__n_pemilik = value

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if value >= 0:
            self.__saldo = value

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            return True
        return False

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            return True
        return False

    def get_info(self):
        return {
            "No Rekening": self.__NoRek,
            "Nama Pemilik": self.__n_pemilik,
            "Saldo": self.__saldo
        }

    def get_no_rek(self):
        return self.__NoRek

class Bank:
    def __init__(self):
        self.daftar_rekening = []

    def tambah_rekening(self, rekening):
        self.daftar_rekening.append(rekening)

    def setor_uang(self, NoRek, jumlah):
        for rekening in self.daftar_rekening:
            if rekening.get_no_rek() == NoRek:
                return rekening.setor(jumlah)
        return False

    def tarik_uang(self, NoRek, jumlah):
        for rekening in self.daftar_rekening:
            if rekening.get_no_rek() == NoRek:
                return rekening.tarik(jumlah)
        return False 

    def tampilkan_semua_rekening(self):
        for rekening in self.daftar_rekening:
            info = rekening.get_info()  
            print(f"No Rekening: {info['No Rekening']}, Nama: {info['Nama Pemilik']}, Saldo: Rp{info['Saldo']}")


def main():
    bank = Bank()

    data1 = RekeningBank("2087", "Zaki", 700000)
    data2 = RekeningBank("2088", "Yoga", 500000)

    bank.tambah_rekening(data1)
    bank.tambah_rekening(data2)

    bank.setor_uang("2087", 300000)
    bank.tarik_uang("2088", 50000)

    print("Daftar Rekening di Bank:")
    bank.tampilkan_semua_rekening()

main()
