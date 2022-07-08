
def turun (x, xmin, xmax):
    kembali (xmax - x) / (xmax - xmin)

def up(x, xmin, xmax):
    kembali (x - xmin) / (xmax - xmin)

kelas lubang():
    minimal = 2200
    maksimum = 3600

    def turun(sendiri, x):
        jika x >= self.maximum:
            kembali 0
        elif x<= self.minimum:
            kembali 1
        kalau tidak:
            kembali ke bawah(x, self.minimum, self.maximum)

    def naik(sendiri, x):
        jika x >= self.maximum:
            kembali 1
        elif x<= self.minimum:
            kembali 0
        kalau tidak:
            kembali ke atas(x, self.minimum, self.maximum)

kelas Persediaan():
    minimal = 100
    maksimum = 260

    def sedikit(sendiri, x):
        jika x >= self.maximum:
            kembali 0
        elif x<= self.minimum:
            kembali 1
        kalau tidak:
            kembali ke bawah(x, self.minimum, self.maximum)

    def banyak(sendiri, x):
        jika x >= self.maximum:
            kembali 1
        elif x<= self.minimum:
            kembali 0
        kalau tidak:
            kembali ke atas(x, self.minimum, self.maximum)


kelas Produksi():
    minimal = 1000
    maksimum = 6000
    permintaan = 0
    persediaan = 0

    def _berkurang(sendiri, a):
        mengembalikan self.maximum - a*(self.maximum - self.minimum)

    def _bertambah(sendiri, a):
        return a*(self.maximum - self.minimum) + self.minimum

    def _inferensi(sendiri, pmt=Permintaan(), psd=Persediaan()):
        hasil = []
        # [R1] JIKA Buka TURUN, dan Persediaan BANYAK, MAKA
        # Produksi Barang BERKURANG.
        a1 = min(pmt.turun(self.permintaan), psd.banyak(self.persediaan))
        z1 = diri._berkurang(a1)
        hasil.tambahkan((a1, z1))
        # [R2] JIKA Buka TURUN, dan Persediaan SEDIKIT, MAKA
        # Produksi Barang BERKURANG.
        a2 = min(pmt.turun(self.permintaan), psd.sedikit(self.persediaan))
        z2 = self._berkurang(a2)
        hasil.tambahkan((a2, z2))
        # [R3] JIKA Lubang NAIK, dan Persediaan BANYAK, MAKA
        # Produksi Barang BERTAMBAH.
        a3 = min(pmt.naik(self.permintaan), psd.banyak(self.persediaan))
        z3 = self._bertambah(a3)
        hasil.tambahkan((a3, z3))
        # [R4] JIKA Lubang NAIK, dan Persediaan SEDIKIT, MAKA
        # Produksi Barang BERTAMBAH.
        a4 = min(pmt.naik(self.permintaan), psd.sedikit(self.persediaan))
        z4 = self._bertambah(a4)
        hasil.tambahkan((a4, z4))
        hasil kembali
    
    def defuzifikasi(self, data_inferensi=[]):
        # (α1∗z1+α2∗z2+α3∗z3+α4∗z4) / (α1+α2+3+α4)
        data_inferensi = data_inferensi jika data_inferensi lain sendiri._inferensi()
        res_a_z = 0
        res_a = 0
        untuk data di data_inferensi:
            # data[0] = a
            # data[1] = z
            res_a_z += data[0] * data[1]
            res_a += data[0]
        kembali res_a_z/res_a
