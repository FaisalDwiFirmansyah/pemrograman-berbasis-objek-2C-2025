from abc import ABC, abstractmethod
class Manusia():
    @abstractmethod
    def berbicara (self):
        pass
    @abstractmethod
    def bekerja (self):
        pass
    @abstractmethod
    def makan (self):
        pass

class Joko(Manusia):
    def berbicara (self):
        print("Joko sedang berbicara dengan Beni")
    def bekerja (self):
        print("Joko sedang bekerja di Barbershop")
    def makan (self):
        print("Joko sedang makan Pudding coklat buatan pak Hambali")

class Beni(Manusia):
    def berbicara (self):
        print("Beni sedang berbicara dengan Joko")
    def bekerja (self):
        print("Beni sedang bekerja di PLN")
    def makan (self):
        print("Beni sedang makan Ketoprak")

class Fani(Manusia):
    def berbicara (self):
        print("Fani sedang mengobrol bersama Jani")
    def bekerja (self):
        print("Fani sedang bekerja di Depot Bakso")
    def makan (self):
        print("Fani sedang makan Bakso Tetelan")

class Jani(Manusia):
    def berbicara (self):
        print("Jani sedang mengobrol bersama Fani")
    def bekerja (self):
        print("Jani sedang bekerja di Bengkel Motor")
    def makan (self):
        print("Jani sedang makan Kue Sus")

print("========== Data Joko ==========")
joko = Joko()
joko.berbicara()
joko.bekerja()
joko.makan()

print("\n========== Data Beni ==========")
beni = Beni()
beni.berbicara()
beni.bekerja()
beni.makan()

print("\n========== Data Fani ==========")
fani = Fani()
fani.berbicara()
fani.bekerja()
fani.makan()

print("\n========== Data Jani ==========")
jani = Jani()
jani.berbicara()
jani.bekerja()
jani.makan()
