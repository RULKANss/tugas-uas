# Sistem Parkiran Kendaraan dengan Konsep Modular dan OOP

class Kendaraan:
    def __init__(self, jenis, plat, warna):
        self.jenis = jenis
        self.plat = plat
        self.warna = warna

class SlotParkir:
    def __init__(self, kapasitas_motor, kapasitas_mobil):
        self.kapasitas_motor = kapasitas_motor
        self.kapasitas_mobil = kapasitas_mobil
        self.parkir_motor = []
        self.parkir_mobil = []

    def cek_slot(self, jenis):
        if jenis == "motor":
            return len(self.parkir_motor) < self.kapasitas_motor
        elif jenis == "mobil":
            return len(self.parkir_mobil) < self.kapasitas_mobil
        return False

    def tambah_kendaraan(self, kendaraan):
        if kendaraan.jenis == "motor" and self.cek_slot("motor"):
            self.parkir_motor.append(kendaraan)
        elif kendaraan.jenis == "mobil" and self.cek_slot("mobil"):
            self.parkir_mobil.append(kendaraan)
        else:
            raise Exception("Slot parkir penuh untuk jenis ini.")

    def hapus_kendaraan(self, plat):
        for kendaraan in self.parkir_motor:
            if kendaraan.plat == plat:
                self.parkir_motor.remove(kendaraan)
                return kendaraan
        for kendaraan in self.parkir_mobil:
            if kendaraan.plat == plat:
                self.parkir_mobil.remove(kendaraan)
                return kendaraan
        raise Exception("Kendaraan tidak ditemukan.")
class Parkiran:
    def __init__(self, kapasitas_motor, kapasitas_mobil):
        self.slot = SlotParkir(kapasitas_motor, kapasitas_mobil)
        self.tarif_motor = 3000
        self.tarif_mobil = 6000

    def parkir_masuk(self, jenis, plat, warna):
        kendaraan = Kendaraan(jenis, plat, warna)
        self.slot.tambah_kendaraan(kendaraan)
        return f"{jenis.capitalize()} dengan plat {plat} berhasil parkir."

    def parkir_keluar(self, plat, durasi):
        kendaraan = self.slot.hapus_kendaraan(plat)
        tarif = self.tarif_motor if kendaraan.jenis == "motor" else self.tarif_mobil
        biaya = tarif * durasi
        return f"{kendaraan.jenis.capitalize()} dengan plat {plat} keluar. Biaya parkir: Rp{biaya}."

    def tampilkan_status(self):
        print("--- Status Parkiran ---")
        print(f"Motor ({len(self.slot.parkir_motor)}/{self.slot.kapasitas_motor}):")
        for motor in self.slot.parkir_motor:
            print(f"  - {motor.plat} ({motor.warna})")
        print(f"Mobil ({len(self.slot.parkir_mobil)}/{self.slot.kapasitas_mobil}):")
        for mobil in self.slot.parkir_mobil:
            print(f"  - {mobil.plat} ({mobil.warna})")

# Fungsi Utama
if __name__ == "__main__":
    parkiran = Parkiran(kapasitas_motor=10, kapasitas_mobil=5)

    while True:
        print("\n--- Sistem Parkiran ---")
        print("1. Parkir Masuk")
        print("2. Parkir Keluar")
        print("3. Tampilkan Status")
        print("4. Keluar")

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
                parkiran.tampilkan_status()

            elif pilihan == 4:
                print("Terima kasih telah menggunakan sistem parkiran.")
                break

            else:
                print("Pilihan tidak valid.")

        except Exception as e:
            print(f"Error: {e}")
