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
CREATE TABLE IF NOT EXISTS permintaan (
    id_permintaan UUID PRIMARY KEY,
    id_periode_permintaan UUID,
    id_perusahaan VARCHAR(255),
    tanggal_permintaan DATE,
    tanggal_awal_permintaan DATE,
    tanggal_akhir_permintaan DATE,
    nama_pltu_peminta VARCHAR(255),
    unit_peminta VARCHAR(255),
    ptbae_diminta FLOAT,
    satuan VARCHAR(255),
    harga FLOAT,
    mata_uang VARCHAR(255),
    sisa_permintaan FLOAT,
    satuan_sisa_permintaan VARCHAR(255)
);
'''

# Eksekusi perintah untuk membuat tabel
cur.execute(create_table_query)
conn.commit()

# Menutup koneksi
cur.close()
conn.close()
