from proses.parkiran import parkiran
from view.view import Parkiran

if __name__ == "__main__":
    parkiran = parkiran(kapasitas_motor=10, kapasitas_mobil=5)
    view = Parkiran(parkiran)

    while True:
        view.tampilkan_menu()
        try:
            pilihan = int(input("Pilih menu: "))
            if pilihan == 1:
                jenis = input("Jenis kendaraan (motor/mobil): ").strip().lower()
                plat = input("Nomor plat: ").strip().upper()
                warna = input("Warna kendaraan: ").strip()
                print(parkiran.parkir_masuk(jenis, plat, warna))
            elif pilihan == 2:
                plat = input("Nomor plat kendaraan: ").strip().upper()
                durasi = int(input("Durasi parkir (jam): "))
                print(parkiran.parkir_keluar(plat, durasi))
            elif pilihan == 3:
                view.tampilkan_status()
            elif pilihan == 4:
                print("Terima kasih telah menggunakan sistem parkiran.")
                break
            else:
                print("Pilihan tidak valid.")
        except Exception as e:
            print(f"Error: {e}")
