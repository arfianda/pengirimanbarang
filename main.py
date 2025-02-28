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

def main():
    print("=" * 50)
    print("PROGRAM PERHITUNGAN BIAYA PENGIRIMAN PAKET")
    print("=" * 50)
    
    try:
        # Input data dari pengguna
        berat = float(input("Masukkan berat paket (kg): "))
        jarak = float(input("Masukkan jarak pengiriman (km): "))
        
        # Input layanan express
        while True:
            express_input = input("Apakah menggunakan layanan express? (y/n): ").lower()
            if express_input in ['y', 'n']:
                express = express_input == 'y'
                break
            else:
                print("Input tidak valid. Masukkan 'y' untuk ya atau 'n' untuk tidak.")
        
        # Input status member
        while True:
            member_input = input("Apakah pelanggan member? (y/n): ").lower()
            if member_input in ['y', 'n']:
                member = member_input == 'y'
                break
            else:
                print("Input tidak valid. Masukkan 'y' untuk ya atau 'n' untuk tidak.")
        
        # Hitung biaya
        biaya = hitung_biaya_pengiriman(berat, jarak, express, member)
        
        # Tampilkan rincian biaya
        print("\nRINCIAN BIAYA PENGIRIMAN:")
        print("-" * 40)
        print(f"Biaya dasar: Rp 10.000")
        
        # Tampilkan biaya tambahan
        if berat > 5:
            print(f"Tambahan biaya berat > 5kg: Rp 5.000")
        
        if jarak > 10:
            print(f"Tambahan biaya jarak > 10km: Rp 8.000")
        
        if express:
            print(f"Tambahan biaya layanan express: Rp 20.000")
        
        # Subtotal sebelum diskon
        subtotal = biaya
        if member:
            subtotal = biaya / 0.9  # Menghitung subtotal sebelum diskon
            print(f"Subtotal: Rp {int(subtotal)}")
            print(f"Diskon member (10%): Rp {int(subtotal * 0.1)}")
        
        # Total akhir
        print("-" * 40)
        print(f"TOTAL BIAYA: Rp {int(biaya)}")
        
    except ValueError:
        print("Error: Mohon masukkan angka yang valid untuk berat dan jarak.")

if __name__ == "__main__":
    main()