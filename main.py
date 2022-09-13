from src.lib_func import *
import mysql.connector
import pandas as pd
from src.mysql_con import *

def main():
    print("""............LIBRARY MANAGEMENT.............
    1. Pendaftaran User Baru
    2. Pendaftaran Buku Baru
    3. Peminjaman
    4. Tampilkan Daftar Buku
    5. Tampilkan Daftar User
    6. Tampilkan Daftar Peminjaman
    7. Cari Buku
    8. Pengembalian
    9. Exit
    """)
    choice = input("Masukkan Nomor Tugas:")
    print("............................")
    if choice in '12345678':
        if(choice == '1'):
            register_user()
        elif(choice == '2'):
            tambah_buku()
        elif(choice == '3'):
            pinjam_buku()
        elif(choice == '4'):
            tampilkan_informasi("buku")
        elif(choice == '5'):
            tampilkan_informasi("user_lms")
        elif(choice == '6'):
            tampilkan_informasi("peminjaman")
        elif(choice == '7'):
            cari_buku()
        elif(choice == '8'):
            pengembalian()
        main()
    elif(choice=='9'):
        print("Sampai Jumpa")
    else:
        print("wrong choice")
        main()
        
if __name__ == '__main__':
    main()
