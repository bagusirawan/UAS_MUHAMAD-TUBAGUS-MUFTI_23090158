from soalno3modul import AntrianRestoran

def main():
    antrian = AntrianRestoran()

    while True:
        print("\nMenu:")
        print("1. Tambah Pesanan")
        print("2. Hapus Pesanan dari Antrian")
        print("3. Tampilkan Antrian")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            pesanan = input("Masukkan pesanan baru: ")
            antrian.enqueue(pesanan)
            print(f"Pesanan '{pesanan}' ditambahkan ke dalam antrian.")
        elif pilihan == '2':
            pesanan = antrian.dequeue()
            if pesanan:
                print(f"Pesanan '{pesanan}' dihapus dari antrian.")
            else:
                print("Antrian kosong, tidak ada pesanan yang dapat dihapus.")
        elif pilihan == '3':
            print("Antrian saat ini:")
            antrian.tampilkan_antrian()
        elif pilihan == '4':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
