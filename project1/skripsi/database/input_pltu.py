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
        cursor.execute(sql, (json.dumps(data['nama_perusahaan']), data['alamat']))
        conn.commit()
        print("Data perusahaan berhasil dimasukkan")
    except psycopg2.Error as e:
        print("Error saat memasukkan data perusahaan:", e)

# Fungsi untuk memasukkan data pltu
def insert_pltu(conn, data):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO pltu (nama_perusahaan, nama_pltu, kategori_pltu) VALUES (%s, %s, %s)"
        cursor.execute(sql, (json.dumps(data['nama']), data['nama_pltu'], data['kategori_pltu']))
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
        cursor.execute(get_perusahaan_id_sql, (data['nama_perusahaan'],))  # Perubahan disini
        result = cursor.fetchone()

        if result is None:
            print("Perusahaan dengan nama '{}' tidak ditemukan.".format(data['nama_perusahaan']))  # Perubahan disini
            return

        id_perusahaan = result[0]

        # SQL untuk memasukkan data emisi dengan id_perusahaan yang telah didapatkan
        sql = "INSERT INTO emisi (nama_pltu, unit_ke, kapasitas, kategori_pltu, produksi_listrik_bruto, izin_ptbae, rencana_emisi, saldo, status, nama_perusahaan) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
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

    # Data pltu
    pltu_data = [
        {"nama": "PT ABC Neosantara Power UPK Sebalang", "nama_pltu": "Sebalang", "kategori_pltu": "non_mulut_tambang", "kapasitas": 100},
        {"nama": "PT ABC Neosantara Power UPK Tarahan B", "nama_pltu": "Tarahan B", "kategori_pltu": "non_mulut_tambang", "kapasitas": 100},
        {"nama": "PT ABC Neosantara POWER UP Kaltim Teluk", "nama_pltu": "Teluk Balikpapan", "kategori_pltu": "non_mulut_tambang", "kapasitas": 110},
        {"nama": "PT ABC Neosantara Power UPK Raya", "nama_pltu": "Raya", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT ABC Neosantara Power UPK Puma", "nama_pltu": "Puma", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT ABC Neosantara Power UPK Tayanan", "nama_pltu": "Tayanan", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT ABC Neosantara Power UPK Teluk Sihir", "nama_pltu": "Teluk Sihir", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT B Electricity", "nama_pltu": "Belectricity", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT Indonesia Energy", "nama_pltu": "Kaltim", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT PT ABC Neosantara Lebuan Sejuk", "nama_pltu": "Lebuan Sejuk", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT Energi Basamo", "nama_pltu": "Jenopato", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT General Energy Bili", "nama_pltu": "Celukan Bawang", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT ABC Neosantara Power PLTU Milkyway", "nama_pltu": "Milkyway", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT Sagara Source Prime", "nama_pltu": "Prime", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT Ten", "nama_pltu": "Ten", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT ABC Neosantara Power UP Peitan", "nama_pltu": "Peitan", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT ABC Neosantara Power UP Rebong", "nama_pltu": "Rebong", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT ABC Neosantara Power Lantar Amu", "nama_pltu": "Lantar Amu", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT Indra", "nama_pltu": "Indra", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT ABC Neosantara Power UP Tajung Awan", "nama_pltu": "Tajung Awan", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT ABC Neosantara Power West Amu", "nama_pltu": "West Amu", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT ABC Neosantara Power UP Python", "nama_pltu": "Python", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT ABC Neosantara Power PLTU Surya UGP", "nama_pltu": "Surya", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT Graha", "nama_pltu": "Eastkal", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT TLC Neo", "nama_pltu": "Westkal", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT Java Power", "nama_pltu": "Piton", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT Tenaga Piton", "nama_pltu": "Pithon", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT ABC Neosantara Power PLTU Laya AMU", "nama_pltu": "Laya", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT ABC UK TJ", "nama_pltu": "TJ B", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT Lestari", "nama_pltu": "LBE", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT Cirebon Power", "nama_pltu": "Cirebon", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT ABC Neosantara Power PLTU Java Adi", "nama_pltu": "middle-java", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT ABC Xhen Ho", "nama_pltu": "Jawa", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT Xena","nama_pltu": "Jateng", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT Bumijati","nama_pltu": "Bumijati", "kategori_pltu": "non_mulut_tambang"},  # Perubahan disini
        {"nama": "PT Tanjung", "nama_pltu": "kalsel", "kategori_pltu": "mulut_tambang"},  # Perubahan disini
        {"nama": "PT Ombi", "nama_pltu": "ombi", "kategori_pltu": "mulut_tambang"},  # Perubahan disini
        {"nama": "PT Priyan", "nama_pltu": "agung", "kategori_pltu": "mulut_tambang"},  # Perubahan disini
        {"nama": "PT Electricity Bukit", "nama_pltu": "Banjarsari", "kategori_pltu": "mulut_tambang"},  # Perubahan disini
        {"nama": "PT FGH", "nama_pltu": "Simpang", "kategori_pltu": "mulut_tambang"},  # Perubahan disini
        {"nama": "PT DSPP Power S", "nama_pltu": "Power S", "kategori_pltu": "mulut_tambang"},  # Perubahan disini
        {"nama": "PT SKS Electricity", "nama_pltu": "kalteng", "kategori_pltu": "mulut_tambang"},  # Perubahan disini
    ]

    
    try:
        # Memasukkan data pltu
        for data in pltu_data:
            insert_pltu(conn, data)

    finally:
        # Menutup koneksi
        conn.close()

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
