import uuid
from datetime import datetime

class penawaran:
    def __init__(self, id_pelaku_penawaran, tanggal_penawaran, tanggal_awal_penawaran, tanggal_akhir_penawaran, nama_pltu_penawar, unit_penawar, ptbae_ditawarkan, satuan, harga, mata_uang, sisa_penawaran, satuan_sisa_penawaran, status, available_penawaran):
        self.id_penawaran = uuid.uuid4()
        self.id_periode_penawaran = uuid.uuid4()
        self.id_pelaku_penawaran = id_pelaku_penawaran
        self.tanggal_penawaran = tanggal_penawaran
        self.tanggal_awal_penawaran = tanggal_awal_penawaran
        self.tanggal_akhir_penawaran = tanggal_akhir_penawaran
        self.nama_pltu_penawar = nama_pltu_penawar
        self.unit_penawar = unit_penawar
        self.ptbae_ditawarkan = ptbae_ditawarkan
        self.satuan = satuan
        self.harga = harga
        self.mata_uang = mata_uang
        self.sisa_penawaran = sisa_penawaran
        self.satuan_sisa_penawaran = satuan_sisa_penawaran
        self.status = status
        self.available_penawaran = available_penawaran
    
    def to_dict(self):
        return vars(self)
    
    @classmethod
    def from_user_input(cls, id_pelaku_penawaran):
        try: 
            tanggal_penawaran = input("Masukkan Tanggal Penawaran (YYYY-MM-DD): ")
            tanggal_penawaran = datetime.strptime(tanggal_penawaran, "%Y-%m-%d").date()
            
            tanggal_awal_penawaran = input("Masukkan Tanggal Awal Penawaran (YYYY-MM-DD): ")
            tanggal_awal_penawaran = datetime.strptime(tanggal_awal_penawaran, "%Y-%m-%d").date()
            
            tanggal_akhir_penawaran = input("Masukkan Tanggal Akhir Penawaran (YYYY-MM-DD): ")
            tanggal_akhir_penawaran = datetime.strptime(tanggal_akhir_penawaran, "%Y-%m-%d").date()
            
            nama_pltu_penawar = input("Masukkan Nama PLTU: ")
            unit_penawar = input("Masukkan Nomor Unit PLTU: ")
            ptbae_ditawarkan = float(input("Masukkan jumlah yang ditawarkan: "))
            satuan = input("Satuan ptbae (hanya dapat memasukkan 'ton co2 e'): ").lower()
            if satuan != "ton co2 e":
                raise ValueError("Satuan yang dimasukkan tidak valid. Harap masukkan 'ton co2 e'.")
            harga = float(input("Masukkan harga ptbae yang ditawarkan: "))
            mata_uang = input("Masukkan mata uang yang digunakan: ")
            sisa_penawaran = float(input("Sisa penawaran yang ada: "))
            satuan_sisa_penawaran = input("Satuan sisa (hanya dapat memasukkan 'ton co2 e'): ").lower()
            if satuan_sisa_penawaran != "ton co2 e":
                raise ValueError("Satuan yang dimasukkan tidak valid. Harap masukkan 'ton co2 e'.")
            available_penawaran = float(input("Penawaran tersedia: "))
            status = input("Status penawaran: ")
            
        except ValueError as e:
                    print(f"Input tidak valid: {e}")
                    return None  # Tambahkan return None jika terjadi ValueError
                
        return penawaran(
            id_penawaran = uuid.uuid4(),
            id_periode_penawaran = uuid.uuid4(),
            id_pelaku_penawaran = id_pelaku_penawaran,
            tanggal_penawaran = tanggal_penawaran,
            tanggal_awal_penawaran = tanggal_awal_penawaran,
            tanggal_akhir_penawaran = tanggal_akhir_penawaran,
            nama_pltu_penawar = nama_pltu_penawar,
            unit_penawar = unit_penawar,
            ptbae_ditawarkan = ptbae_ditawarkan,
            satuan = satuan,
            harga = harga,
            mata_uang = mata_uang,
            sisa_penawaran = sisa_penawaran,
            satuan_sisa_penawaran = satuan_sisa_penawaran,
            status = status,
            available_penawaran = available_penawaran,
        )


if __name__ == "__main__":
    # Add the necessary imports and any other code outside the class here
    pass
                
            