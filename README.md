# Logika Informatika

## Case

●	Sebuah jasa pengiriman memiliki aturan biaya yang bergantung pada beberapa faktor. Biaya dasar pengiriman ditetapkan sebesar Rp 10.000. Jika berat paket melebihi 5 kg, maka akan dikenakan tambahan biaya sebesar Rp 5.000. Selain itu, jika jarak pengiriman lebih dari 10 km, maka ada tambahan biaya sebesar Rp 8.000. Jika pelanggan memilih layanan pengiriman express, maka akan dikenakan tambahan biaya sebesar Rp 20.000. Namun, jika pelanggan merupakan member, mereka akan mendapatkan diskon 10% dari total biaya pengiriman yang dihitung sebelum diskon


## Requirements

●	Buatlah sebuah fungsi dalam Python yang dapat menghitung total biaya pengiriman berdasarkan aturan tersebut, dengan parameter *berat paket, jarak pengiriman, jenis pengiriman (biasa atau express), serta status keanggotaan pelanggan (member atau non-member).*

## Solutions

Pertama mari buat fungsi python untuk menghitung biaya pengiriman berdasarkan ketentuan yang sudah di tentukan:

```
def hitung_biaya_pengiriman(berat_kg, jarak_km, pengiriman_express=False, member=False):
    """
    Menghitung total biaya pengiriman berdasarkan aturan yang ditetapkan.
    
    Parameters:
    berat_kg (float): Berat paket dalam kilogram
    jarak_km (float): Jarak pengiriman dalam kilometer
    pengiriman_express (bool): True jika menggunakan layanan express, False jika biasa
    member (bool): True jika pelanggan adalah member, False jika bukan
    
    Returns:
    float: Total biaya pengiriman setelah perhitungan
    """
    # Biaya dasar
    biaya_total = 10000
    
    # Tambahan biaya berdasarkan berat
    if berat_kg > 5:
        biaya_total += 5000
    
    # Tambahan biaya berdasarkan jarak
    if jarak_km > 10:
        biaya_total += 8000
    
    # Tambahan biaya untuk pengiriman express
    if pengiriman_express:
        biaya_total += 20000
    
    # Diskon untuk member
    if member:
        biaya_total = biaya_total * 0.9  # Diskon 10%
    
    return biaya_total

```


Fungsi ini menerima empat parameter:

- berat_kg: Berat paket dalam kilogram
- jarak_km: Jarak pengiriman dalam kilometer
- pengiriman_express: Boolean yang menunjukkan apakah layanan express digunakan (default: False)
- member: Boolean yang menunjukkan apakah pelanggan adalah member (default: False)

Cara menggunakan fungsi:

```
# Contoh penggunaan:
# Paket 7 kg, jarak 15 km, pengiriman biasa, bukan member
biaya1 = hitung_biaya_pengiriman(7, 15, False, False)
print(f"Biaya pengiriman: Rp {biaya1}")  # Output: Rp 23000

# Paket 3 kg, jarak 5 km, pengiriman express, member
biaya2 = hitung_biaya_pengiriman(3, 5, True, True)
print(f"Biaya pengiriman: Rp {biaya2}")  # Output: Rp 27000

# Dengan parameter default (pengiriman biasa, bukan member)
biaya3 = hitung_biaya_pengiriman(6, 12)
print(f"Biaya pengiriman: Rp {biaya3}")  # Output: Rp 23000


```

Fungsi akan menghitung biaya berdasarkan aturan yang diberikan:

- Biaya dasar: Rp 10.000
- Tambahan Rp 5.000 jika berat > 5 kg
- Tambahan Rp 8.000 jika jarak > 10 km
- Tambahan Rp 20.000 jika pengiriman express
- Diskon 10% jika pelanggan adalah member

## Implementasi

Program ini memiliki dua bagian utama:

1. Fungsi hitung_biaya_pengiriman() untuk menghitung biaya sesuai dengan aturan yang ditetapkan
2. Fungsi main() yang menangani interaksi dengan pengguna:
- Meminta input data (berat, jarak, jenis pengiriman, status member)
- Memvalidasi input
- Menampilkan rincian biaya secara detail


Pengguna akan diminta untuk memasukkan:

- Berat paket dalam kilogram
-Jarak pengiriman dalam kilometer
- Apakah menggunakan layanan express (y/n)
- Apakah pelanggan member (y/n)

Contoh:

<img src="lib/img/image.png" width="500" alt="Demo Program">
