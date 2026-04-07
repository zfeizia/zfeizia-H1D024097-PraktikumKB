import time
import random

# 1. STRUKTUR DATA
# Menggunakan List untuk menyimpan judul drakor
watchlist_drakor = ["Boyfriend On Demand", "No tail To Tell", "My Demon", "Cashero"]

# 2. STRUKTUR KONTROL 
# Menggunakan perulangan While agar menu terus muncul
while True:
    print("\n === Watchlist Drakor ===")
    print("1. Tambah Judul Drakor")
    print("2. Lihat Daftar Tontonan")
    print("3. Pilih Acak Buat Ditonton Sekarang")
    print("4. Keluar")
    
    pilihan = input("Pilih menu (1/2/3/4): ")
    
    # Menggunakan percabangan If-Elif-Else
    if pilihan == '1':
        judul = input("Masukkan judul drakor: ")
        watchlist_drakor.append(judul)
        print(f"'{judul}' Berhasil ditambahkan ke daftar tontonan.")
        
    elif pilihan == '2':
        print("\n--- Daftar Drakor Seru---")
        if len(watchlist_drakor) == 0:
            print("Daftar masih kosong.")
        else:
            # Menggunakan perulangan For
            for i, judul in enumerate(watchlist_drakor):
                print(f"{i+1}. {judul}")
                
    elif pilihan == '3':
        if len(watchlist_drakor) == 0:
            print("Tambahkan judul tontonan terlebih dahulu.")
        else:
            print("Mencari tontonan terbaik untukmu...")
            # 3. LIBRARY (1): time 
            time.sleep(1) 
            
            # --- LIBRARY (2): random 
            acak = random.choice(watchlist_drakor)
            print(f"Saran: Drakkor '{acak}' yang harus km tonton sekarang!")
            
    elif pilihan == '4':
        print("\nSelamat maraton drakor!")
        break 
        
    else:
        print("Menu tidak valid. Pilih angka 1 sampai 4.")