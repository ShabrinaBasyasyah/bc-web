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
        
        # SQL untuk memasukkan data emisi tanpa aturan pada nama_perusahaan
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
            data['nama_perusahaan']  # Tetap memasukkan nama perusahaan dari data
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

    # Data perusahaan
    perusahaan_data = [
        {"nama_perusahaan": "PT ABC Neosantara Power UPK Sebalang", "alamat": "Alamat A"},  # Perubahan disini
        {"nama_perusahaan": "PT ABC Neosantara Power UPK Tarahan B", "alamat": "Alamat B"},  # Perubahan disini
        {"nama_perusahaan": "PT ABC Neosantara POWER UP Kaltim Teluk", "alamat": "Alamat C"} , # Perubahan disini
        {"nama_perusahaan": "PT ABC Neosantara Power UPK Raya", "alamat": "Alamat D"},  # Perubahan disini
        {"nama_perusahaan": "PT ABC Neosantara Power UPK Puma", "alamat": "Alamat F"},  # Perubahan disini
        {"nama_perusahaan": "PT ABC Neosantara Power UPK Tayanan", "alamat": "Alamat G"},  # Perubahan disini
        {"nama_perusahaan": "PT ABC Neosantara Power UPK Teluk Sihir", "alamat": "Alamat H"},  # Perubahan disini
        {"nama_perusahaan": "PT B Electricity", "alamat": "Alamat ..."},  # Perubahan disini
        {"nama_perusahaan": "PT Indonesia Energy", "alamat": "Alamat I"},  # Perubahan disini
        {"nama_perusahaan": "PT PT ABC Neosantara Lebuan Sejuk", "alamat": "Alamat J"},  # Perubahan disini
        {"nama_perusahaan": "PT Energi Basamo", "alamat": "Alamat K"},  # Perubahan disini
        {"nama_perusahaan": "PT General Energy Bili", "alamat": "Alamat K"},  # Perubahan disini
        {"nama_perusahaan": "PT ABC Neosantara Power PLTU Milkyway", "alamat": "Alamat L"},  # Perubahan disini
        {"nama_perusahaan": "PT Sagara Source Prime", "alamat": "Alamat N"},  # Perubahan disini
        {"nama_perusahaan": "PT Ten", "alamat": "Alamat ..."},  # Perubahan disini
        {"nama_perusahaan": "PT ABC Neosantara Power UP Peitan", "alamat": "Alamat M"},  # Perubahan disini
        {"nama_perusahaan": "PT ABC Neosantara Power UP Rebong", "alamat": "Alamat O"},  # Perubahan disini
        {"nama_perusahaan": "PT ABC Neosantara Power Lantar Amu", "alamat": "Alamat P"},  # Perubahan disini
        {"nama_perusahaan": "PT Indra", "alamat": "Alamat ..."},  # Perubahan disini
        {"nama_perusahaan": "PT ABC Neosantara Power UP Tajung Awan", "alamat": "Alamat Q"},  # Perubahan disini
        {"nama_perusahaan": "PT ABC Neosantara Power West Amu", "alamat": "Alamat R"},  # Perubahan disini
        {"nama_perusahaan": "PT ABC Neosantara Power UP Python", "alamat": "Alamat S"},  # Perubahan disini
        {"nama_perusahaan": "PT ABC Neosantara Power PLTU Surya UGP", "alamat": "Alamat T"},  # Perubahan disini
        {"nama_perusahaan": "PT Graha", "alamat": "Alamat U"},  # Perubahan disini
        {"nama_perusahaan": "PT TLC Neo", "alamat": "Alamat V"},  # Perubahan disini
        {"nama_perusahaan": "PT Java Power", "alamat": "Alamat W"},  # Perubahan disini
        {"nama_perusahaan": "PT Tenaga Piton", "alamat": "Alamat X"},  # Perubahan disini
        {"nama_perusahaan": "PT ABC Neosantara Power PLTU Laya AMU", "alamat": "Alamat Y"},  # Perubahan disini
        {"nama_perusahaan": "PT ABC UK TJ", "alamat": "Alamat Z"},  # Perubahan disini
        {"nama_perusahaan": "PT Lestari", "alamat": "Alamat 00"},  # Perubahan disini
        {"nama_perusahaan": "PT Cirebon Power", "alamat": "Alamat ap"},  # Perubahan disini
        {"nama_perusahaan": "PT ABC Neosantara Power PLTU Java Adi", "alamat": "Alamat ..."},  # Perubahan disini
        {"nama_perusahaan": "PT ABC Xhen Ho", "alamat": "Alamat ..."},  # Perubahan disini
        {"nama_perusahaan": "PT Xena", "alamat": "Alamat ..."},  # Perubahan disini
        {"nama_perusahaan": "PT Bumijati", "alamat": "Alamat ..."},  # Perubahan disini
        {"nama_perusahaan": "PT Tanjung", "alamat": "Alamat ..."},  # Perubahan disini
        {"nama_perusahaan": "PT Ombi", "alamat": "Alamat ..."},  # Perubahan disini
        {"nama_perusahaan": "PT Priyan", "alamat": "Alamat ..."},  # Perubahan disini
        {"nama_perusahaan": "PT Electricity Bukit", "alamat": "Alamat ..."},  # Perubahan disini
        {"nama_perusahaan": "PT FGH", "alamat": "Alamat ..."},  # Perubahan disini
        {"nama_perusahaan": "PT DSPP Power S", "alamat": "Alamat ..."},  # Perubahan disini
        {"nama_perusahaan": "PT SKS Electricity", "alamat": "Alamat ..."},  # Perubahan disini
    ]

    
    try:
        # Memasukkan data perusahaan
        # Memasukkan data perusahaan
        for data in perusahaan_data:
            insert_perusahaan(conn, data)

       
    finally:
        # Menutup koneksi
        conn.close()

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
