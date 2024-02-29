import uuid
from datetime import datetime

class permintaan:
    def __init__(self, id_pelaku_permintaan, tanggal_permintaan, tanggal_awal_permintaan, tanggal_akhir_permintaan, nama_pltu_peminta, unit_peminta, ptbae_diminta, satuan, harga, mata_uang, jumlah_terbeli, satuan_terbeli, sisa_permintaan, satuan_sisa_permintaan, tanggal_terbeli, status):
        self.id_permintaan = uuid.uuid4()
        self.id_periode_permintaan = uuid.uuid4()
        self.id_pelaku_permintaan = id_pelaku_permintaan
        self.tanggal_permintaan = tanggal_permintaan
        self.tanggal_awal_permintaan = tanggal_awal_permintaan
        self.tanggal_akhir_permintaan = tanggal_akhir_permintaan
        self.nama_pltu_peminta = nama_pltu_peminta
        self.unit_peminta = unit_peminta
        self.ptbae_diminta = ptbae_diminta
        self.satuan = satuan
        self.harga = harga
        self.mata_uang = mata_uang
        self.jumlah_terbeli = jumlah_terbeli
        self.satuan_terbeli = satuan_terbeli
        self.sisa_permintaan = sisa_permintaan
        self.satuan_sisa_permintaan = satuan_sisa_permintaan
        self.tanggal_terbeli = tanggal_terbeli
        self.status = status
    
    def to_dict(self):
        return vars(self)
    
    @classmethod
    def from_user_input(cls, id_pelaku_permintaan):
        try: 
            tanggal_permintaan = input("Masukkan Tanggal Permintaan (YYYY-MM-DD): ")
            tanggal_permintaan = datetime.strptime(tanggal_permintaan, "%Y-%m-%d").date()
            
            tanggal_awal_permintaan = input("Masukkan Tanggal Awal Permintaan (YYYY-MM-DD): ")
            tanggal_awal_permintaan = datetime.strptime(tanggal_awal_permintaan, "%Y-%m-%d").date()
            
            tanggal_akhir_permintaan = input("Masukkan Tanggal Akhir Permintaan (YYYY-MM-DD): ")
            tanggal_akhir_permintaan = datetime.strptime(tanggal_akhir_permintaan, "%Y-%m-%d").date()
            
            nama_pltu_peminta = input("Masukkan Nama PLTU: ")
            unit_peminta = input("Masukkan Nomor Unit PLTU: ")
            ptbae_diminta = float(input("Masukkan jumlah yang ditawarkan: "))
            satuan = input("Satuan ptbae (hanya dapat memasukkan 'ton co2 e'): ").lower()
            if satuan != "ton co2 e":
                raise ValueError("Satuan yang dimasukkan tidak valid. Harap masukkan 'ton co2 e'.")
            harga = float(input("Masukkan harga ptbae yang ditawarkan: "))
            mata_uang = input("Masukkan mata uang yang digunakan: ")
            jumlah_terbeli = float(input("Jumlah ptbae yang telah terbeli: "))
            satuan_terbeli = input("Satuan terbeli (hanya dapat memasukkan 'ton co2 e'): ").lower()
            if satuan_terbeli != "ton co2 e":
                raise ValueError("Satuan yang dimasukkan tidak valid. Harap masukkan 'ton co2 e'.")
            sisa_permintaan = float(input("Sisa permintaan yang ada: "))
            satuan_sisa_permintaan = input("Satuan sisa (hanya dapat memasukkan 'ton co2 e'): ").lower()
            if satuan_sisa_permintaan != "ton co2 e":
                raise ValueError("Satuan yang dimasukkan tidak valid. Harap masukkan 'ton co2 e'.")
            tanggal_terbeli = input("Masukkan Tanggal Terbeli (YYYY-MM-DD): ")
            tanggal_terbeli = datetime.strptime(tanggal_terbeli, "%Y-%m-%d").date()
            status = input("Status penawaran: ")
            
        except ValueError as e:
                    print(f"Input tidak valid: {e}")
                    return None  # Tambahkan return None jika terjadi ValueError
                
        return permintaan(
        id_permintaan = uuid.uuid4(),
        id_periode_permintaan = uuid.uuid4(),
        id_pelaku_permintaan = id_pelaku_permintaan,
        tanggal_permintaan = tanggal_permintaan,
        tanggal_awal_permintaan = tanggal_awal_permintaan,
        tanggal_akhir_permintaan = tanggal_akhir_permintaan,
        nama_pltu_peminta = nama_pltu_peminta,
        unit_peminta = unit_peminta,
        ptbae_diminta = ptbae_diminta,
        satuan = satuan,
        harga = harga,
        mata_uang = mata_uang,
        jumlah_terbeli = jumlah_terbeli,
        satuan_terbeli = satuan_terbeli,
        sisa_permintaan = sisa_permintaan,
        satuan_sisa_permintaan = satuan_sisa_permintaan,
        tanggal_terbeli = tanggal_terbeli,
        status = status,
        )


if __name__ == "__main__":
    # Add the necessary imports and any other code outside the class here
    pass
                
            