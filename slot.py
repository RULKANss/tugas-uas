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
