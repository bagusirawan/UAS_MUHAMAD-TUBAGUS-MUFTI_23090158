class AntrianRestoran:
    def __init__(self):
        self.antrian = []

    def enqueue(self, pesanan):
        self.antrian.append(pesanan)

    def dequeue(self):
        if self.antrian:
            return self.antrian.pop(0)
        else:
            return None

    def tampilkan_antrian(self):
        if self.antrian:
            for idx, pesanan in enumerate(self.antrian, start=1):
                print(f"{idx}. {pesanan}")
        else:
            print("Antrian kosong.")
