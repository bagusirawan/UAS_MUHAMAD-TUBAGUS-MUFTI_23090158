class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def information(self):
        return f"Nama: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}"

class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin

    def information(self):
        buah_info = super().information()
        return f"{buah_info}, Vitamin: {self.vitamin}"
    
mangga1 = Mangga("Mangga Harum Manis", "Hijau", "Manis", "Vitamin C")
print(mangga1.information())

mangga1.nama = "Mangga Gedong"
mangga1.warna = "Kuning"
mangga1.rasa = "Manis dan Sedikit Asam"
mangga1.vitamin = "Vitamin A dan C"
print(mangga1.information())
