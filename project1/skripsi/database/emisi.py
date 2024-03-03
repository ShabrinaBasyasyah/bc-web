import psycopg2
import json

# Fungsi untuk membuka koneksi ke database
def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="ptbae",  # Ganti dengan nama database Anda
            user="postgres",        # Ganti dengan nama pengguna Anda
            password="dks120193",     # Ganti dengan kata sandi Anda
            host="localhost",        # Ganti dengan host database Anda
            port="5433"              # Ganti dengan port database Anda
        )
        return conn
    except psycopg2.Error as e:
        print("Error saat terhubung ke database:", e)
        return None

# Fungsi untuk memasukkan data perusahaan
def insert_perusahaan(conn, data):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO perusahaan (nama_perusahaan, alamat) VALUES (%s, %s)"
        cursor.execute(sql, (json.dumps(data['nama']), data['alamat']))
        conn.commit()
        print("Data perusahaan berhasil dimasukkan")
    except psycopg2.Error as e:
        print("Error saat memasukkan data perusahaan:", e)

# Fungsi untuk memasukkan data pltu
def insert_pltu(conn, data):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO pltu (nama_perusahaan, nama_pltu, kategori_pltu, kapasitas) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (json.dumps(data['nama']), data['nama_pltu'], data['kategori_pltu'], data['kapasitas']))
        conn.commit()
        print("Data pltu berhasil dimasukkan")
    except psycopg2.Error as e:
        print("Error saat memasukkan data pltu:", e)

# Fungsi untuk memasukkan data emisi
def insert_emisi(conn, data):
    try:
        cursor = conn.cursor()

        # Subquery untuk mendapatkan id_perusahaan berdasarkan nama_perusahaan
        get_perusahaan_id_sql = "SELECT id_perusahaan FROM perusahaan WHERE lower(nama_perusahaan) = lower(%s)"

        # Eksekusi subquery untuk mendapatkan id_perusahaan
        cursor.execute(get_perusahaan_id_sql, (data['nama'],))
        result = cursor.fetchone()

        if result is None:
            print("Perusahaan dengan nama '{}' tidak ditemukan.".format(data['nama']))
            return

        id_perusahaan = result[0]

        # SQL untuk memasukkan data emisi dengan id_perusahaan yang telah didapatkan
        sql = "INSERT INTO emisi (nama_pltu, unit_ke, kapasitas, kategori_pltu, produksi_listrik_bruto, izin_ptbae, rencana_emisi, saldo, status, id_perusahaan, nama_perusahaan) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (
            data['nama_pltu'], 
            data.get('unit_ke', '1'), 
            data['kapasitas'], 
            data['kategori_pltu'], 
            data.get('produksi_listrik_bruto', '1'), 
            data['izin_ptbae'], 
            data['rencana_emisi'], 
            0, 
            'Surplus' if (data['kapasitas'] >= 100 and data['kategori_pltu'] == 'mulut_tambang' and data['izin_ptbae'] == '0.911') or (data['kapasitas'] > 400 and data['kategori_pltu'] == 'non_mulut_tambang' and data['izin_ptbae'] == '0.911') else 'Defisit',
            id_perusahaan,  # Gunakan id_perusahaan yang telah didapatkan dari subquery
            data['nama_perusahaan']
        ))
        conn.commit()
        print("Data emisi berhasil dimasukkan")
    except psycopg2.Error as e:
        print("Error saat memasukkan data emisi:", e)

# Fungsi utama
def main():
    # Koneksi ke database
    conn = connect_to_db()
    if conn is None:
        return

 # Data emisi
    emisi_data = [
        {"nama_pltu": "Sebalang", "kapasitas": 100, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 50, "nama": "PT ABC Neosantara Power UPK Sebalang"},
        {"nama_pltu": "Tarahan B", "kapasitas": 100, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 100, "nama": "PT ABC Neosantara Power UPK Tarahan B"},
        {"nama_pltu": "Teluk Balikpapan", "kapasitas": 110, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 75, "nama": "PT ABC Neosantara POWER UP Kaltim Teluk"}
    ]

    try:
        for data in emisi_data:
            insert_emisi(conn, data)
    finally:
        # Menutup koneksi
        conn.close()

if __name__ == "__main__":
    main()
