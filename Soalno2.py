data_mahasiswa = [
    ["Mahasiswa 1", 90, 80],
    ["Mahasiswa 2", 50, 60],
    ["Mahasiswa 3", 65, 70]
]
rata_algoritma = sum(mhs[1] for mhs in data_mahasiswa) / len(data_mahasiswa)
rata_matdis = sum(mhs[2] for mhs in data_mahasiswa) / len(data_mahasiswa)

print(f"Rata-rata nilai Algoritma: {rata_algoritma}")
print(f"Rata-rata nilai Matdis: {rata_matdis}")

print("\nRata-rata nilai setiap mahasiswa:")
for mhs in data_mahasiswa:
    rata_mahasiswa = (mhs[1] + mhs[2]) / 2
    print(f"{mhs[0]}: {rata_mahasiswa}")
