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
CREATE TABLE IF NOT EXISTS transaksi_jual (
    id_transaksi_jual UUID PRIMARY KEY,
    id_periode_transaksi_jual UUID,
    kode_transaksi_jual VARCHAR(255),
    tanggal_transaksi_jual DATE,
    id_pelaku_transaksi_jual VARCHAR(255),
    id_pembeli VARCHAR(255),
    jumlah_karbon_keluar FLOAT,
    satuan_karbon_keluar VARCHAR(255),
    harga_jual FLOAT,
    satuan_harga_jual VARCHAR(255),
    token UUID,
    id_permintaan VARCHAR(255),
    id_penawaran VARCHAR(255),
    id_transaksi_awal VARCHAR(255)
);
'''

# Eksekusi perintah untuk membuat tabel
cur.execute(create_table_query)
conn.commit()

# Menutup koneksi
cur.close()
conn.close()
