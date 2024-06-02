def kena_razia(tanggal, data_kendaraan):
    rute_ganjil_genap = ["Gajah Mada", "Hayam Wuruk", "Sisingamangaraja", "Panglima Polim", "Fatmawati", "Tomang Raya"]
    catatan_pelanggaran = {}
    
    for kendaraan in data_kendaraan:
        if kendaraan["type"] == "Mobil":
            angka_terakhir = kendaraan["plat"].split()[-1][-1]
            if angka_terakhir.isdigit():
                angka_terakhir = int(angka_terakhir)
            else:
                angka_terakhir = 0
            
            if kendaraan["name"] not in catatan_pelanggaran:
                catatan_pelanggaran[kendaraan["name"]] = 0
            
            for rute in kendaraan["rute"]:
                if rute in rute_ganjil_genap and (angka_terakhir % 2 != tanggal % 2):
                    catatan_pelanggaran[kendaraan["name"]] += 1
    
    hasil = [{"name": pengemudi, "tilang": jumlah_pelanggaran} for pengemudi, jumlah_pelanggaran in catatan_pelanggaran.items()]
    
    return hasil

# Contoh penggunaan
data_kendaraan = [
    {
        "name": "Denver",
        "plat": "B 2791 KDS",
        "type": "Mobil",
        "rute": ["TB Simatupang", "Panglima Polim", "Depok", "Senen Raya"]
    },
    {
        "name": "Toni",
        "plat": "B 1212 JBB",
        "type": "Mobil",
        "rute": ["Pintu Besar Selatan", "Panglima Polim", "Depok", "Senen Raya", "Kemang"]
    },
    {
        "name": "Stark",
        "plat": "B 444 XSX",
        "type": "Motor",
        "rute": ["Pondok Indah", "Depok", "Senen Raya", "Kemang"]
    },
    {
        "name": "Anna",
        "plat": "B 678 DD",
        "type": "Mobil",
        "rute": ["Fatmawati", "Panglima Polim", "Depok", "Senen Raya", "Kemang", "Gajah Mada"]
    }
]

tanggal = 27
hasil = kena_razia(tanggal, data_kendaraan)
print(hasil)