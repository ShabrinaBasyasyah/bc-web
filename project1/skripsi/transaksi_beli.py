import uuid
from datetime import datetime

class transaksi_beli:
    def __init__(self, id_transaksi_beli, id_periode, kode_transaksi, tanggal_transaksi_beli, id_penjual, id_pembeli, jumlah_karbon_masuk, satuan_karbon_masuk, harga_beli, satuan_harga_beli, token, token_expired, saldo_emisi, satuan_saldo, approval_status, approved_by, approved_at, id_permintaan, id_transaksi_awal):
        self.id_transaksi_beli = id_transaksi_beli
        self.id_periode = id_periode
        self.kode_transaksi = kode_transaksi
        self.tanggal_transaksi_beli = tanggal_transaksi_beli
        self.id_penjual = id_penjual
        self.id_pembeli = id_pembeli
        self.jumlah_karbon_masuk = jumlah_karbon_masuk
        self.satuan_karbon_masuk = satuan_karbon_masuk
        self.harga_beli = harga_beli
        self.satuan_harga_beli = satuan_harga_beli
        self.token = token
        self.token_expired = token_expired
        self.saldo_emisi = saldo_emisi
        self.satuan_saldo = satuan_saldo
        self.approval_status = approval_status
        self.approved_by = approved_by
        self.approved_at = approved_at
        self.id_permintaan = id_permintaan
        self.id_transaksi_awal = id_transaksi_awal
        
    def to_dict(self):
        return vars(self)
    
    @classmethod
    def from_user_input(cls, id_pembeli, token, token_expired, saldo_emisi, satuan_saldo, approval_status, approved_by, approved_at, id_permintaan, id_transaksi_awal):
        try: 
            kode_transaksi = input("Masukkan kode transaksi: ")

            tanggal_transaksi_beli = input("Masukkan Tanggal Transaksi (YYYY-MM-DD): ")
            tanggal_transaksi_beli = datetime.strptime(tanggal_transaksi_beli, "%Y-%m-%d").date()
            
            id_penjual = input("Masukkan id_penjual: ")
            
            jumlah_karbon_masuk = float(input("Masukkan jumlah yang dibeli: "))
            satuan_karbon_masuk = input("Satuan ptbae (hanya dapat memasukkan 'ton co2 e'): ").lower()
            if satuan_karbon_masuk != "ton co2 e":
                raise ValueError("Satuan yang dimasukkan tidak valid. Harap masukkan 'ton co2 e'.")
            harga_beli = float(input("Masukkan harga ptbae yang dibeli: "))
            satuan_harga_beli = input("Masukkan mata uang yang digunakan: ")
            
        except ValueError as e:
            print(f"Input tidak valid: {e}")
            return None  # Tambahkan return None jika terjadi ValueError
                
        return cls(
            id_transaksi_beli = uuid.uuid4(),
            id_periode = uuid.uuid4(),
            kode_transaksi = kode_transaksi,
            tanggal_transaksi_beli = tanggal_transaksi_beli,
            id_penjual = id_penjual,
            id_pembeli = id_pembeli,
            jumlah_karbon_masuk = jumlah_karbon_masuk,
            satuan_karbon_masuk = satuan_karbon_masuk,
            harga_beli = harga_beli,
            satuan_harga_beli = satuan_harga_beli,
            token = uuid.uuid4(),
            token_expired = token_expired,
            saldo_emisi = saldo_emisi,
            satuan_saldo = satuan_saldo,
            approval_status = approval_status,
            approved_by = approved_by,
            approved_at = approved_at,
            id_permintaan = id_permintaan,
            id_transaksi_awal = id_transaksi_awal
        )

if __name__ == "__main__":
    # Tambahkan kode untuk pengujian atau penggunaan kelas transaksi_beli di sini
    pass
