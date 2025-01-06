from data.kendaraan import kendaraan
from data.slot import slot

class Parkiran:
    def __init__(self, kapasitas_motor, kapasitas_mobil):
        self.slot = slot(kapasitas_motor, kapasitas_mobil)
        self.tarif_motor = 3000
        self.tarif_mobil = 6000

    def parkir_masuk(self, jenis, plat, warna):
        kendaraan = kendaraan(jenis, plat, warna)
        self.slot.tambah_kendaraan(kendaraan)
        return f"{jenis.capitalize()} dengan plat {plat} berhasil parkir."

    def parkir_keluar(self, plat, durasi):
        kendaraan = self.slot.hapus_kendaraan(plat)
        tarif = self.tarif_motor if kendaraan.jenis == "motor" else self.tarif_mobil
        biaya = tarif * durasi
        return f"{kendaraan.jenis.capitalize()} dengan plat {plat} keluar. Biaya parkir: Rp{biaya}."

    def tampilkan_status(self):
        return {
            "motor": {
                "terisi": len(self.slot.parkir_motor),
                "kapasitas": self.slot.kapasitas_motor,
                "kendaraan": [
                    {"plat": k.plat, "warna": k.warna} for k in self.slot.parkir_motor
                ],
            },
            "mobil": {
                "terisi": len(self.slot.parkir_mobil),
                "kapasitas": self.slot.kapasitas_mobil,
                "kendaraan": [
                    {"plat": k.plat, "warna": k.warna} for k in self.slot.parkir_mobil
                ],
            },
        }
