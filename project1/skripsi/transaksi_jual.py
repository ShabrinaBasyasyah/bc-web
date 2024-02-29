import uuid
from datetime import datetime

class transaksi_jual:
    def __init__(self, id_transaksi_jual, id_periode, kode_transaksi, tanggal_transaksi_jual, id_penjual, id_pembeli, jumlah_karbon_keluar, satuan_karbon_keluar, harga_jual, satuan_harga_jual, token, token_expired, saldo_emisi, satuan_saldo, approval_status, approved_by, approved_at, id_penawaran, id_transaksi_awal):
        self.id_transaksi_jual = uuid.uuid4()
        self.id_periode = uuid.uuid4
        self.kode_transaksi = kode_transaksi
        self.tanggal_transaksi_jual = tanggal_transaksi_jual
        self.id_penjual = id_penjual
        self.id_pembeli = id_pembeli
        self.jumlah_karbon_keluar = jumlah_karbon_keluar
        self.satuan_karbon_keluar = satuan_karbon_keluar
        self.harga_jual = harga_jual
        self.satuan_harga_jual = satuan_harga_jual
        self.token = uuid.uuid4
        self.token_expired = token_expired
        self.saldo_emisi = saldo_emisi
        self.satuan_saldo = satuan_saldo
        self.approval_status = approval_status
        self.approved_by = approved_by
        self.id_penawaran = id_penawaran
        self.id_transaksi_awal = id_transaksi_awal
        
    def to_dict(self):
        return vars(self)
    
    @classmethod
    def from_user_input(cls, id_penjual, token, token_expired, saldo_emisi, satuan_saldo, approval_status, approved_by, approved_at, id_penawaran, id_transaksi_awal):
        try: 
            kode_transaksi = input("Masukkan kode transaksi: ")

            tanggal_transaksi_jual = input("Masukkan Tanggal Transaksi (YYYY-MM-DD): ")
            tanggal_transaksi_jual = datetime.strptime(tanggal_transaksi_jual, "%Y-%m-%d").date()
            
            id_pembeli = input("Masukkan id_pembeli: ")
            
            jumlah_karbon_keluar = float(input("Masukkan jumlah yang ditawarkan: "))
            satuan_karbon_keluar = input("Satuan ptbae (hanya dapat memasukkan 'ton co2 e'): ").lower()
            if satuan_karbon_keluar != "ton co2 e":
                raise ValueError("Satuan yang dimasukkan tidak valid. Harap masukkan 'ton co2 e'.")
            harga_jual = float(input("Masukkan harga ptbae yang ditawarkan: "))
            satuan_harga_jual = input("Masukkan mata uang yang digunakan: ")
            
        except ValueError as e:
                    print(f"Input tidak valid: {e}")
                    return None  # Tambahkan return None jika terjadi ValueError
                
        return transaksi_jual(
        id_transaksi_jual = uuid.uuid4(),
        id_periode = uuid.uuid4,
        kode_transaksi = kode_transaksi,
        tanggal_transaksi_jual = tanggal_transaksi_jual,
        id_penjual = id_penjual,
        id_pembeli = id_pembeli,
        jumlah_karbon_keluar = jumlah_karbon_keluar,
        satuan_karbon_keluar = satuan_karbon_keluar,
        harga_jual = harga_jual,
        satuan_harga_jual = satuan_harga_jual,
        token = uuid.uuid4,
        token_expired = token_expired,
        saldo_emisi = saldo_emisi,
        satuan_saldo = satuan_saldo,
        approval_status = approval_status,
        approved_by = approved_by,
        id_penawaran = id_penawaran,
        id_transaksi_awal = id_transaksi_awal,
        
        )


if __name__ == "__main__":
    # Add the necessary imports and any other code outside the class here
    pass
                
            