class ParkiranView:
    def __init__(self, parkiran):
        self.parkiran = parkiran

    def tampilkan_menu(self):
        print("\n--- Sistem Parkiran ---")
        print("1. Parkir Masuk")
        print("2. Parkir Keluar")
        print("3. Tampilkan Status")
        print("4. Keluar")

    def tampilkan_status(self):
        status = self.parkiran.tampilkan_status()
        print("--- Status Parkiran ---")
        print(f"Motor ({status['motor']['terisi']}/{status['motor']['kapasitas']}):")
        for motor in status["motor"]["kendaraan"]:
            print(f"  - {motor['plat']} ({motor['warna']})")
        print(f"Mobil ({status['mobil']['terisi']}/{status['mobil']['kapasitas']}):")
        for mobil in status["mobil"]["kendaraan"]:
            print(f"  - {mobil['plat']} ({mobil['warna']})")