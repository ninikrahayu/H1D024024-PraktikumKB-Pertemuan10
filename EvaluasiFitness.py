def hitung_fitness(kromosom, barang, kapasitas_tas):
    total_keuntungan = 0
    total_ukuran = 0

    for i in range(len(kromosom)):
        if kromosom[i] == 1:
            total_keuntungan += barang[i][1]
            total_ukuran += barang[i][2]

    if total_ukuran > kapasitas_tas:
        return 0
    else:
        return total_keuntungan