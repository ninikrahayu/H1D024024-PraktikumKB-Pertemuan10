# H1D024024-PraktikumKB-Pertemuan10

# Algoritma Genetika - Knapsack Problem

Repository ini berisi implementasi Algoritma Genetika untuk menyelesaikan kasus Knapsack Problem pada Praktikum Kecerdasan Buatan Pertemuan 10.

Tujuan program adalah menentukan kombinasi barang dengan keuntungan maksimal tanpa melebihi kapasitas maksimal gudang.

---

# Data Barang

| Barang | Keuntungan | Ukuran |
|---|---:|---:|
| Barang1 | 10 | 5 |
| Barang2 | 40 | 4 |
| Barang3 | 30 | 6 |
| Barang4 | 50 | 3 |
| Barang5 | 35 | 7 |

Ukuran maksimal gudang:

```text
15
```

---

# Metode Berdasarkan NIM

NIM:

```text
H1D024024
```

Dua digit terakhir:

```text
24
```

Penentuan metode:

| Langkah | Metode |
|---|---|
| Seleksi | Roulette Wheel Selection (RWS) |
| Crossover | Two Point Crossover |
| Mutasi | Swap Mutation |

Penjelasan:
- Digit pertama `2` → RWS
- Digit kedua `4` → Two Point Crossover
- `2 + 4 = 6` → Swap Mutation

---

# Struktur File

```text
H1D024024-PraktikumKB-Pertemuan10/
│
├── inisiasipopulasi.py
├── EvaluasiFitness.py
├── selection.py
├── crossover.py
├── mutation.py
└── main.py
```

---

# Penjelasan Jalannya Program

Program berjalan menggunakan tahapan Algoritma Genetika, yaitu:

1. Inisialisasi Populasi
2. Evaluasi Fitness
3. Seleksi
4. Crossover
5. Mutasi
6. Pembentukan Generasi Baru
7. Menampilkan Solusi Terbaik

---

# 1. Inisialisasi Populasi

Tahap pertama adalah membuat populasi awal secara acak.

Setiap individu direpresentasikan sebagai kromosom biner.

Contoh:

```python
[1, 0, 1, 0, 1]
```

Artinya:
- Barang1 dipilih
- Barang2 tidak dipilih
- Barang3 dipilih
- Barang4 tidak dipilih
- Barang5 dipilih

Kode pada `inisiasipopulasi.py`:

```python
kromosom = [random.randint(0, 1) for _ in range(jumlah_gen)]
```

Program akan membuat banyak kromosom sesuai jumlah populasi.

---

# 2. Evaluasi Fitness

Setelah populasi dibuat, program menghitung nilai fitness setiap individu.

Fitness dihitung dari total keuntungan barang yang dipilih.

Jika total ukuran barang melebihi kapasitas gudang, maka fitness akan bernilai 0 sebagai penalti.

Kode pada `EvaluasiFitness.py`:

```python
if total_ukuran > kapasitas_tas:
    return 0
else:
    return total_keuntungan
```

Contoh:

```python
[0,1,0,1,1]
```

Barang yang dipilih:
- Barang2
- Barang4
- Barang5

Perhitungan:

```text
Keuntungan = 40 + 50 + 35 = 125
Ukuran = 4 + 3 + 7 = 14
```

Karena ukuran 14 tidak melebihi kapasitas 15, maka fitness = 125.

---

# 3. Seleksi

Tahap seleksi digunakan untuk memilih parent terbaik.

Metode yang digunakan:

```text
Roulette Wheel Selection (RWS)
```

Pada metode ini, individu dengan fitness lebih tinggi memiliki peluang lebih besar untuk dipilih.

Kode pada `selection.py`:

```python
parent1, idx1 = roulette_wheel_selection(populasi, fitness_populasi)
```

---

# 4. Crossover

Tahap crossover digunakan untuk menghasilkan keturunan baru dari dua parent.

Metode yang digunakan:

```text
Two Point Crossover
```

Program memilih dua titik potong pada kromosom lalu menukar bagian gen parent.

Contoh:

Parent 1:
```python
[1,0,1,1,0]
```

Parent 2:
```python
[0,1,0,0,1]
```

Hasil crossover:
```python
[1,1,0,1,0]
```

Kode pada `crossover.py`:

```python
anak1, anak2 = two_point_crossover(parent1, parent2)
```

---

# 5. Mutasi

Tahap mutasi digunakan untuk menjaga keragaman populasi.

Metode yang digunakan:

```text
Swap Mutation
```

Mutasi dilakukan dengan menukar posisi dua gen pada kromosom.

Contoh:

Sebelum:
```python
[1,0,1,0,1]
```

Sesudah:
```python
[1,1,1,0,0]
```

Kode pada `mutation.py`:

```python
anak1 = swap_mutation(anak1)
```

---

# 6. Pembentukan Generasi Baru

Anak hasil crossover dan mutasi dimasukkan ke populasi baru.

Proses:
- Seleksi
- Crossover
- Mutasi

akan terus diulang selama beberapa generasi.

Tujuannya agar solusi semakin optimal.

Kode pada `main.py`:

```python
populasi = new_populasi[:jumlah_populasi]
```

---

# 7. Hasil Terbaik

Setelah seluruh generasi selesai, program akan menampilkan solusi terbaik.

Hasil optimal:

```text
Barang2
Barang4
Barang5
```

Dengan:

```text
Total Keuntungan = 125
Total Ukuran = 14
```

Kromosom terbaik:

```python
[0,1,0,1,1]
```

---

# Grafik Fitness

Program menampilkan grafik perkembangan fitness setiap generasi.

Keterangan warna:
- Biru → Fitness tertinggi
- Merah → Fitness rata-rata
- Kuning → Fitness terendah

Grafik menunjukkan perkembangan kualitas solusi selama proses evolusi.

---

# Cara Menjalankan Program

Install library matplotlib:

```bash
pip install matplotlib
```

Jalankan program:

```bash
python main.py
```

---

# Kesimpulan

Algoritma Genetika berhasil menemukan kombinasi barang terbaik tanpa melebihi kapasitas gudang.

Barang yang dipilih:
- Barang2
- Barang4
- Barang5

Keuntungan maksimal:

```text
125
```

Total ukuran:

```text
14
```
