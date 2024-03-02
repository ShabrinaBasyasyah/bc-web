import psycopg2
from psycopg2 import sql

# Koneksi ke database
conn = psycopg2.connect(
    dbname="ptbae",
    user="postgres",
    password="dks120193",
    host="localhost",
    port=5433
)

# Membuat kursor
cur = conn.cursor()

# Perintah untuk membuat tabel permintaan
create_table_query = '''
CREATE TABLE IF NOT EXISTS transaksi_beli (
    id_transaksi_beli UUID PRIMARY KEY,
    id_periode_transaksi_beli UUID,
    kode_transaksi_beli VARCHAR(255),
    tanggal_transaksi_beli DATE,
    id_pelaku_transaksi_beli VARCHAR(255),
    id_penjual VARCHAR(255),
    jumlah_karbon_masuk FLOAT,
    satuan_karbon_masuk VARCHAR(255),
    harga_beli FLOAT,
    satuan_harga_beli VARCHAR(255),
    token UUID,
    token_expired DATE,
    saldo_emisi FLOAT,
    satuan_saldo VARCHAR(255),
    approval_status FLOAT,
    satuan_terbeli VARCHAR(255),
    sisa_permintaan FLOAT,
    satuan_sisa_permintaan VARCHAR(255),
    tanggal_terbeli DATE,
    status VARCHAR(255)
);
'''

# Eksekusi perintah untuk membuat tabel
cur.execute(create_table_query)
conn.commit()

# Menutup koneksi
cur.close()
conn.close()
