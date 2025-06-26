from abc import ABC, abstractmethod
class PerangkatElektronik(ABC):
    def __init__(self):
        self.energi_tersisa = 100
        self.nama = "Perangkat Elektronik"

    @abstractmethod
    def nyalakan(self):
        pass

    @abstractmethod
    def matikan(self):
        pass

    @abstractmethod
    def gunakan(self, jam: int):
        pass

    def status(self):
        print("=" * 40)
        print("STATUS PERANGKAT ELEKTRONIK")
        print("-" * 40)
        print(f"Nama Perangkat : {self.nama}")
        print(f"Energi Tersisa : {self.energi_tersisa}%")
        print("=" * 40)

class Laptop(PerangkatElektronik):
    def __init__(self):
        super().__init__()
        self.nama = "Laptop"

    def nyalakan(self):
        print("Laptop dinyalakan.")

    def matikan(self):
        print("Laptop dimatikan.")

    def gunakan(self, jam: int):
        print(f"Laptop digunakan selama {jam} jam.")
        self.energi_tersisa -= 10 * jam
        if self.energi_tersisa <= 0:
            self.energi_tersisa = 0
            print("Baterai habis!")

class Kulkas(PerangkatElektronik):
    def __init__(self):
        super().__init__()
        self.nama = "Kulkas"

    def nyalakan(self):
        print("Kulkas dinyalakan.")

    def matikan(self):
        print("Kulkas dimatikan.")

    def gunakan(self, jam: int):
        print(f"Kulkas digunakan selama {jam} jam.")
        self.energi_tersisa -= 5 * jam
        if self.energi_tersisa < 20:
            print("Energi rendah, kulkas butuh daya tambahan!")
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0

laptop1 = Laptop()
laptop1.nyalakan()
laptop1.gunakan(10)
laptop1.status()
laptop1.matikan()

print()

kulkas1 = Kulkas()
kulkas1.nyalakan()
kulkas1.gunakan(17)
kulkas1.status()
kulkas1.matikan()
