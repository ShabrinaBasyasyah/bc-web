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
CREATE TABLE IF NOT EXISTS pengawas (
id_penawaran UUID PRIMARY KEY,
    nama_pltu_penawar VARCHAR(255),
    unit_penawar VARCHAR(255),
    ptbae_ditawarkan FLOAT,
    satuan VARCHAR(20),
    harga FLOAT,
    mata_uang VARCHAR(50),
    sisa_penawaran FLOAT,
    satuan_sisa_penawaran VARCHAR(20),
    status VARCHAR(100),
    available_penawaran FLOAT
);
'''

# Eksekusi perintah untuk membuat tabel
cur.execute(create_table_query)
conn.commit()

# Menutup koneksi
cur.close()
conn.close()
