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
            data['nama_perusahaan']  # Tanpa json.dumps()
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
        {"nama_pltu": "Sebalang", "unit_ke": 1, "kapasitas": 100, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 5000,"produksi_listrik_bruto": 1200000, "nama_perusahaan": "PT ABC Neosantara Power UPK Sebalang"},  # Perubahan disini
        {"nama_pltu": "Sebalang", "unit_ke": 2, "kapasitas": 100, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 6000, "produksi_listrik_bruto": 1300000, "nama_perusahaan": "PT ABC Neosantara Power UPK Sebalang"},  # Perubahan disini
        {"nama_pltu": "Tarahan B", "unit_ke": 1, "kapasitas": 100, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 7500, "produksi_listrik_bruto": 1400000,"nama_perusahaan": "PT ABC Neosantara Power UPK Tarahan B"},  # Perubahan disini
        {"nama_pltu": "Tarahan B", "unit_ke": 2, "kapasitas": 100, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 7000, "produksi_listrik_bruto": 1500000, "nama_perusahaan": "PT ABC Neosantara Power UPK Tarahan B"},  # Perubahan disini
        {"nama_pltu": "Teluk Balikpapan", "unit_ke": 1, "kapasitas": 110, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 8000, "produksi_listrik_bruto": 1600000, "nama_perusahaan": "PT ABC Neosantara Power UPK Tarahan B"},  # Perubahan disini
        {"nama_pltu": "Teluk Balikpapan", "unit_ke": 2, "kapasitas": 110, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 8000, "produksi_listrik_bruto": 1600000, "nama_perusahaan": "PT ABC Neosantara Power UPK Tarahan B"},  # Perubahan disini
        {"nama_pltu": "Raya", "unit_ke": 1, "kapasitas": 110, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 9000, "produksi_listrik_bruto": 1700000, "nama_perusahaan": "PT ABC Neosantara Power UPK Raya"},  # Perubahan disini
        {"nama_pltu": "Raya", "unit_ke": 2, "kapasitas": 110, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 9000, "produksi_listrik_bruto": 1700000, "nama_perusahaan": "PT ABC Neosantara Power UPK Raya"},  # Perubahan disini
        {"nama_pltu": "Puma", "unit_ke": 1, "kapasitas": 110, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 10000, "produksi_listrik_bruto": 1800000, "nama_perusahaan": "PT ABC Neosantara Power UPK Puma"},  # Perubahan disini
        {"nama_pltu": "Puma", "unit_ke": 2, "kapasitas": 110, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 10000, "produksi_listrik_bruto": 1800000, "nama_perusahaan": "PT ABC Neosantara Power UPK Puma"},  # Perubahan disini
        {"nama_pltu": "Tayanan", "unit_ke": 1, "kapasitas": 110, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 11000, "produksi_listrik_bruto": 1900000, "nama_perusahaan": "PT ABC Neosantara Power UPK Tayanan"},  # Perubahan disini
        {"nama_pltu": "Tayanan", "unit_ke": 2, "kapasitas": 110, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 11000, "produksi_listrik_bruto": 1900000, "nama_perusahaan": "PT ABC Neosantara Power UPK Tayanan"},  # Perubahan disini
        {"nama_pltu": "Teluk Sihir", "unit_ke": 1, "kapasitas": 112, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 11000, "produksi_listrik_bruto": 1200000, "nama_perusahaan": "PT ABC Neosantara Power UPK Teluk Sihir"},  # Perubahan disini
        {"nama_pltu": "Teluk Sihir", "unit_ke": 2, "kapasitas": 112, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 11000, "produksi_listrik_bruto": 1200000, "nama_perusahaan": "PT ABC Neosantara Power UPK Teluk Sihir"},  # Perubahan disini
        {"nama_pltu": "Belectricity", "unit_ke": 1, "kapasitas": 115, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 12000, "produksi_listrik_bruto": 1100000, "nama_perusahaan": "PT B Electricity"},  # Perubahan disini
        {"nama_pltu": "Belectricity", "unit_ke": 2, "kapasitas": 115, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 12000, "produksi_listrik_bruto": 1100000, "nama_perusahaan": "PT B Electricity"},  # Perubahan disini
        {"nama_pltu": "Kaltim", "unit_ke": 1, "kapasitas": 115, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 13000, "produksi_listrik_bruto": 1000000, "nama_perusahaan": "PT Indonesia Energy"},  # Perubahan disini
        {"nama_pltu": "Kaltim", "unit_ke": 2, "kapasitas": 115, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 13000, "produksi_listrik_bruto": 1000000, "nama_perusahaan": "PT Indonesia Energy"},  # Perubahan disini
        {"nama_pltu": "Lebuan Sejuk", "unit_ke": 1, "kapasitas": 115, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 14000, "produksi_listrik_bruto": 900000, "nama_perusahaan": "PT ABC Neosantara Lebuan Sejuk"},  # Perubahan disini
        {"nama_pltu": "Lebuan Sejuk", "unit_ke": 2, "kapasitas": 115, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 14000, "produksi_listrik_bruto": 900000, "nama_perusahaan": "PT ABC Neosantara Lebuan Sejuk"},  # Perubahan disini
        {"nama_pltu": "Jenopato", "unit_ke": 1, "kapasitas": 125, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 5000, "produksi_listrik_bruto": 800000, "nama_perusahaan": "PT Energi Basamo"},  # Perubahan disini
        {"nama_pltu": "Jenopato", "unit_ke": 2, "kapasitas": 125, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 5000, "produksi_listrik_bruto": 800000, "nama_perusahaan": "PT Energi Basamo"},  # Perubahan disini
        {"nama_pltu": "Jenopato", "unit_ke": 3, "kapasitas": 135, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 5000, "produksi_listrik_bruto": 800000, "nama_perusahaan": "PT Energi Basamo"},  # Perubahan disini
        {"nama_pltu": "Jenopato", "unit_ke": 4, "kapasitas": 135, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 5000, "produksi_listrik_bruto": 800000, "nama_perusahaan": "PT Energi Basamo"},  # Perubahan disini
        {"nama_pltu": "Celukan Bawang", "unit_ke": 1, "kapasitas": 142, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 6000, "produksi_listrik_bruto": 700000, "nama_perusahaan": "PT General Energy Bili"},  # Perubahan disini
        {"nama_pltu": "Celukan Bawang", "unit_ke": 2, "kapasitas": 142, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 6000, "produksi_listrik_bruto": 700000, "nama_perusahaan": "PT General Energy Bili"},  # Perubahan disini
        {"nama_pltu": "Celukan Bawang", "unit_ke": 3, "kapasitas": 142, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 6000, "produksi_listrik_bruto": 700000, "nama_perusahaan": "PT General Energy Bili"},  # Perubahan disini
        {"nama_pltu": "Milkyway", "unit_ke": 1, "kapasitas": 220, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 5500, "produksi_listrik_bruto": 1200000, "nama_perusahaan": "PT ABC Neosantara Power PLTU Milkyway"},  # Perubahan disini
        {"nama_pltu": "Milkyway", "unit_ke": 2, "kapasitas": 220, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 5500, "produksi_listrik_bruto": 1200000, "nama_perusahaan": "PT ABC Neosantara Power PLTU Milkyway"},  # Perubahan disini
        {"nama_pltu": "Milkyway", "unit_ke": 3, "kapasitas": 200, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 5500, "produksi_listrik_bruto": 1200000, "nama_perusahaan": "PT ABC Neosantara Power PLTU Milkyway"},  # Perubahan disini
        {"nama_pltu": "Milkyway", "unit_ke": 4, "kapasitas": 200, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 5500, "produksi_listrik_bruto": 1200000, "nama_perusahaan": "PT ABC Neosantara Power PLTU Milkyway"},  # Perubahan disini
        {"nama_pltu": "Prime", "unit_ke": 1, "kapasitas": 300, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 6500, "produksi_listrik_bruto": 1100000, "nama_perusahaan": "PT Sagara Source Prime"},  # Perubahan disini
        {"nama_pltu": "Prime", "unit_ke": 2, "kapasitas": 300, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 6500, "produksi_listrik_bruto": 1100000, "nama_perusahaan": "PT Sagara Source Prime"},  # Perubahan disini
        {"nama_pltu": "Ten", "unit_ke": 1, "kapasitas": 300, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 4500, "produksi_listrik_bruto": 1300000, "nama_perusahaan": "PT Ten"},  # Perubahan disini
        {"nama_pltu": "Ten", "unit_ke": 2, "kapasitas": 300, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 4500, "produksi_listrik_bruto": 1300000, "nama_perusahaan": "PT Ten"},  # Perubahan disini
        {"nama_pltu": "Peitan", "unit_ke": 1, "kapasitas": 315, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 3500, "produksi_listrik_bruto": 1200000, "nama_perusahaan": "PT ABC Neosantara Power UP Peitan"},  # Perubahan disini
        {"nama_pltu": "Peitan", "unit_ke": 2, "kapasitas": 315, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 3500, "produksi_listrik_bruto": 1200000, "nama_perusahaan": "PT ABC Neosantara Power UP Peitan"},  # Perubahan disini
        {"nama_pltu": "Rebong", "unit_ke": 1, "kapasitas": 315, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 3500, "produksi_listrik_bruto": 1200000, "nama_perusahaan": "PT ABC Neosantara Power UP Rebong"},  # Perubahan disini
        {"nama_pltu": "Rebong", "unit_ke": 2, "kapasitas": 315, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 3500, "produksi_listrik_bruto": 1200000, "nama_perusahaan": "PT ABC Neosantara Power UP Rebong"},  # Perubahan disini
        {"nama_pltu": "Lantar Amu", "unit_ke": 1, "kapasitas": 315, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 2500, "produksi_listrik_bruto": 1200000, "nama_perusahaan": "PT ABC Neosantara Power Lantar Amu"},  # Perubahan disini
        {"nama_pltu": "Lantar Amu", "unit_ke": 2, "kapasitas": 315, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 2500, "produksi_listrik_bruto": 1200000, "nama_perusahaan": "PT ABC Neosantara Power Lantar Amu"},  # Perubahan disini
        {"nama_pltu": "Lantar Amu", "unit_ke": 3, "kapasitas": 315, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 2500, "produksi_listrik_bruto": 1200000, "nama_perusahaan": "PT ABC Neosantara Power Lantar Amu"},  # Perubahan disini
        {"nama_pltu": "Indra", "unit_ke": 1, "kapasitas": 330, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 5500, "produksi_listrik_bruto": 1400000, "nama_perusahaan": "PT Indra"},  # Perubahan disini
        {"nama_pltu": "Indra", "unit_ke": 2, "kapasitas": 330, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 5500, "produksi_listrik_bruto": 1400000, "nama_perusahaan": "PT Indra"},  # Perubahan disini
        {"nama_pltu": "Indra", "unit_ke": 3, "kapasitas": 330, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 5500, "produksi_listrik_bruto": 1400000, "nama_perusahaan": "PT Indra"},  # Perubahan disini
        {"nama_pltu": "Tajung Awan", "unit_ke": 1, "kapasitas": 350, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 6500, "produksi_listrik_bruto": 1300000, "nama_perusahaan": "PT PT ABC Neosantara Power UP Tajung Awan"},  # Perubahan disini
        {"nama_pltu": "Tajung Awan", "unit_ke": 2, "kapasitas": 350, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 6500, "produksi_listrik_bruto": 1300000, "nama_perusahaan": "PT PT ABC Neosantara Power UP Tajung Awan"},  # Perubahan disini
        {"nama_pltu": "West Amu", "unit_ke": 1, "kapasitas": 350, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 8500, "produksi_listrik_bruto": 1400000, "nama_perusahaan": "PT ABC Neosantara Power West Amu"},  # Perubahan disini
        {"nama_pltu": "West Amu", "unit_ke": 2, "kapasitas": 350, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 8500, "produksi_listrik_bruto": 1400000, "nama_perusahaan": "PT ABC Neosantara Power West Amu"},  # Perubahan disini
        {"nama_pltu": "West Amu", "unit_ke": 3, "kapasitas": 350, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 8500, "produksi_listrik_bruto": 1400000, "nama_perusahaan": "PT ABC Neosantara Power West Amu"},  # Perubahan disini
        {"nama_pltu": "Python", "unit_ke": 1, "kapasitas": 400, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 7500, "produksi_listrik_bruto": 1000000, "nama_perusahaan": "PT ABC Neosantara Power UP Python"},  # Perubahan disini
        {"nama_pltu": "Python", "unit_ke": 2, "kapasitas": 400, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 7500, "produksi_listrik_bruto": 1000000, "nama_perusahaan": "PT ABC Neosantara Power UP Python"},  # Perubahan disini
        {"nama_pltu": "Surya", "unit_ke": 1, "kapasitas": 400, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 6500, "produksi_listrik_bruto": 9000000, "nama_perusahaan": "PT ABC Neosantara Power PLTU Surya UGP"},  # Perubahan disini
        {"nama_pltu": "Surya", "unit_ke": 2, "kapasitas": 400, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 6500, "produksi_listrik_bruto": 9000000, "nama_perusahaan": "PT ABC Neosantara Power PLTU Surya UGP"},  # Perubahan disini
        {"nama_pltu": "Surya", "unit_ke": 3, "kapasitas": 400, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 6500, "produksi_listrik_bruto": 9000000, "nama_perusahaan": "PT ABC Neosantara Power PLTU Surya UGP"},  # Perubahan disini
        {"nama_pltu": "Surya", "unit_ke": 4, "kapasitas": 400, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 6500, "produksi_listrik_bruto": 9000000, "nama_perusahaan": "PT ABC Neosantara Power PLTU Surya UGP"},  # Perubahan disini
        {"nama_pltu": "Eastkal", "unit_ke": 1, "kapasitas": 100, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 2500, "produksi_listrik_bruto": 5000000, "nama_perusahaan": "PT Graha"},  # Perubahan disini
        {"nama_pltu": "Eastkal", "unit_ke": 2, "kapasitas": 100, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 2500, "produksi_listrik_bruto": 5000000, "nama_perusahaan": "PT Graha"},  # Perubahan disini
        {"nama_pltu": "Westkal", "unit_ke": 1, "kapasitas": 100, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 3500, "produksi_listrik_bruto": 4000000, "nama_perusahaan": "PT Graha"},  # Perubahan disini
        {"nama_pltu": "Westkal", "unit_ke": 2, "kapasitas": 100, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "1.011", "rencana_emisi": 3500, "produksi_listrik_bruto": 4000000, "nama_perusahaan": "PT TLC Neo"},  # Perubahan disini
        {"nama_pltu": "Surya", "unit_ke": 5, "kapasitas": 600, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 12500, "produksi_listrik_bruto": 12000000, "nama_perusahaan": "PT ABC Neosantara Power PLTU Surya UGP"},  # Perubahan disini
        {"nama_pltu": "Surya", "unit_ke": 6, "kapasitas": 600, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 12500, "produksi_listrik_bruto": 12000000, "nama_perusahaan": "PT ABC Neosantara Power PLTU Surya UGP"},  # Perubahan disini
        {"nama_pltu": "Surya", "unit_ke": 7, "kapasitas": 600, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 12500, "produksi_listrik_bruto": 12000000, "nama_perusahaan": "PT ABC Neosantara Power PLTU Surya UGP"},  # Perubahan disini
        {"nama_pltu": "Piton", "unit_ke": 5, "kapasitas": 610, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 13500, "produksi_listrik_bruto": 14000000, "nama_perusahaan": "PT Java Power"},  # Perubahan disini
        {"nama_pltu": "Piton", "unit_ke": 6, "kapasitas": 610, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 13500, "produksi_listrik_bruto": 14000000, "nama_perusahaan": "PT Java Power"},  # Perubahan disini
        {"nama_pltu": "Pithon", "unit_ke": 7, "kapasitas": 615, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 14500, "produksi_listrik_bruto": 16000000, "nama_perusahaan": "PT Tenaga Piton"},  # Perubahan disini
        {"nama_pltu": "Pithon", "unit_ke": 8, "kapasitas": 615, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 14500, "produksi_listrik_bruto": 16000000, "nama_perusahaan": "PT Tenaga Piton"},  # Perubahan disini
        {"nama_pltu": "Laya", "unit_ke": 1, "kapasitas": 625, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 15500, "produksi_listrik_bruto": 20000000, "nama_perusahaan": "PT ABC Neosantara Power PLTU Laya AMU"},  # Perubahan disini
        {"nama_pltu": "TJ B", "unit_ke": 1, "kapasitas": 710, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 20000, "produksi_listrik_bruto": 20000000, "nama_perusahaan": "ABC UK TJ"},  # Perubahan disini
        {"nama_pltu": "TJ B", "unit_ke": 2, "kapasitas": 710, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 20000, "produksi_listrik_bruto": 20000000, "nama_perusahaan": "ABC UK TJ"},  # Perubahan disini
        {"nama_pltu": "TJ B", "unit_ke": 3, "kapasitas": 710, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 20000, "produksi_listrik_bruto": 20000000, "nama_perusahaan": "ABC UK TJ"},  # Perubahan disini
        {"nama_pltu": "TJ B", "unit_ke": 4, "kapasitas": 710, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 20000, "produksi_listrik_bruto": 20000000, "nama_perusahaan": "ABC UK TJ"},  # Perubahan disini
        {"nama_pltu": "Prime", "unit_ke": 3, "kapasitas": 660, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 150000, "produksi_listrik_bruto": 1100000, "nama_perusahaan": "PT Sagara Source Prime"},  # Perubahan disini
        {"nama_pltu": "Cirebon", "unit_ke": 1, "kapasitas": 660, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 170000, "produksi_listrik_bruto": 1100000, "nama_perusahaan": "PT Cirebon Power"},  # Perubahan disini
        {"nama_pltu": "LBE", "unit_ke": 1, "kapasitas": 660, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 120000, "produksi_listrik_bruto": 1100000, "nama_perusahaan": "PT Lestari"},  # Perubahan disini
        {"nama_pltu": "Prime", "unit_ke": 3, "kapasitas": 660, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 110000, "produksi_listrik_bruto": 1100000, "nama_perusahaan": "PT Sagara Source Prime"},  # Perubahan disini
        {"nama_pltu": "Cirebon", "unit_ke": 1, "kapasitas": 660, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 210000, "produksi_listrik_bruto": 1150000, "nama_perusahaan": "PT Cirebon Power"},  # Perubahan disini
        {"nama_pltu": "Pithon", "unit_ke": 9, "kapasitas": 660, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 14500, "produksi_listrik_bruto": 16000000, "nama_perusahaan": "PT Tenaga Piton"},  # Perubahan disini
        {"nama_pltu": "middle-java", "unit_ke": 2, "kapasitas": 660, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 200000, "produksi_listrik_bruto": 16000000, "nama_perusahaan": "PT ABC Neosantara Power PLTU Java Adi"},  # Perubahan disini
        {"nama_pltu": "Bumijati", "unit_ke": 1, "kapasitas": 710, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 200000, "produksi_listrik_bruto": 16000000, "nama_perusahaan": "PT Bumijati"},  # Perubahan disini
        {"nama_pltu": "Bumijati", "unit_ke": 2, "kapasitas": 710, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 200000, "produksi_listrik_bruto": 16000000, "nama_perusahaan": "PT Bumijati"},  # Perubahan disini
        {"nama_pltu": "Bumijati", "unit_ke": 3, "kapasitas": 721.8, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 200000, "produksi_listrik_bruto": 16000000, "nama_perusahaan": "PT Bumijati"},  # Perubahan disini
        {"nama_pltu": "Bumijati", "unit_ke": 4, "kapasitas": 721.8, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 200000, "produksi_listrik_bruto": 16000000, "nama_perusahaan": "PT Bumijati"},  # Perubahan disini
        {"nama_pltu": "Python", "unit_ke": 3, "kapasitas": 815, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 150000, "produksi_listrik_bruto": 1000000, "nama_perusahaan": "PT ABC Neosantara Power UP Python"},  # Perubahan disini
        {"nama_pltu": "Jawa", "unit_ke": 1, "kapasitas": 1050, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 160000, "produksi_listrik_bruto": 1100000, "nama_perusahaan": "PT ABC Xhen Ho"},  # Perubahan disini
        {"nama_pltu": "Jawa", "unit_ke": 2, "kapasitas": 1050, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 160000, "produksi_listrik_bruto": 1100000, "nama_perusahaan": "PT ABC Xhen Ho"},  # Perubahan disini
        {"nama_pltu": "Jateng", "unit_ke": 1, "kapasitas": 1000, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 170000, "produksi_listrik_bruto": 1200000, "nama_perusahaan": "PT Xena"},  # Perubahan disini
        {"nama_pltu": "Bumijati", "unit_ke": 5, "kapasitas": 1000, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 180000, "produksi_listrik_bruto": 2200000, "nama_perusahaan": "PT Bumijati"},  # Perubahan disini
        {"nama_pltu": "Bumijati", "unit_ke": 5, "kapasitas": 1000, "kategori_pltu": "non_mulut_tambang", "izin_ptbae": "0.911", "rencana_emisi": 180000, "produksi_listrik_bruto": 2200000, "nama_perusahaan": "PT Bumijati"},  # Perubahan disini
        {"nama_pltu": "Kalsel", "unit_ke": 1, "kapasitas": 100, "kategori_pltu": "mulut_tambang", "izin_ptbae": "1.089", "rencana_emisi": 150000, "produksi_listrik_bruto": 2200000, "nama_perusahaan": "PT Tanjung"},  # Perubahan disini
        {"nama_pltu": "Kalsel", "unit_ke": 2, "kapasitas": 100, "kategori_pltu": "mulut_tambang", "izin_ptbae": "1.089", "rencana_emisi": 150000, "produksi_listrik_bruto": 2200000, "nama_perusahaan": "PT Tanjung"},  # Perubahan disini
        {"nama_pltu": "ombi", "unit_ke": 1, "kapasitas": 100, "kategori_pltu": "mulut_tambang", "izin_ptbae": "1.089", "rencana_emisi": 160000, "produksi_listrik_bruto": 2600000, "nama_perusahaan": "PT Ombi"},  # Perubahan disini
        {"nama_pltu": "ombi", "unit_ke": 2, "kapasitas": 100, "kategori_pltu": "mulut_tambang", "izin_ptbae": "1.089", "rencana_emisi": 10000, "produksi_listrik_bruto": 2600000, "nama_perusahaan": "PT Ombi"},  # Perubahan disini
        {"nama_pltu": "agung", "unit_ke": 1, "kapasitas": 135, "kategori_pltu": "mulut_tambang", "izin_ptbae": "1.089", "rencana_emisi": 90000, "produksi_listrik_bruto": 1500000, "nama_perusahaan": "PT Priyan"},  # Perubahan disini
        {"nama_pltu": "agung", "unit_ke": 2, "kapasitas": 135, "kategori_pltu": "mulut_tambang", "izin_ptbae": "1.089", "rencana_emisi": 90000, "produksi_listrik_bruto": 1500000, "nama_perusahaan": "PT Priyan"},  # Perubahan disini
        {"nama_pltu": "Banjarsari", "unit_ke": 1, "kapasitas": 135, "kategori_pltu": "mulut_tambang", "izin_ptbae": "1.089", "rencana_emisi": 80000, "produksi_listrik_bruto": 1400000, "nama_perusahaan": "PT Electricity Bukit"},  # Perubahan disini
        {"nama_pltu": "Banjarsari", "unit_ke": 2, "kapasitas": 135, "kategori_pltu": "mulut_tambang", "izin_ptbae": "1.089", "rencana_emisi": 80000, "produksi_listrik_bruto": 1400000, "nama_perusahaan": "PT Electricity Bukit"},  # Perubahan disini
        {"nama_pltu": "Simpang", "unit_ke": 1, "kapasitas": 150, "kategori_pltu": "mulut_tambang", "izin_ptbae": "1.089", "rencana_emisi": 70000, "produksi_listrik_bruto": 1300000, "nama_perusahaan": "PT FGH"},  # Perubahan disini
        {"nama_pltu": "Simpang", "unit_ke": 2, "kapasitas": 150, "kategori_pltu": "mulut_tambang", "izin_ptbae": "1.089", "rencana_emisi": 70000, "produksi_listrik_bruto": 1300000, "nama_perusahaan": "PT FGH"},  # Perubahan disini
        {"nama_pltu": "Power S", "unit_ke": 1, "kapasitas": 175, "kategori_pltu": "mulut_tambang", "izin_ptbae": "1.089", "rencana_emisi": 50000, "produksi_listrik_bruto": 1300000, "nama_perusahaan": "PT DSPP Power S"},  # Perubahan disini
        {"nama_pltu": "Power S", "unit_ke": 2, "kapasitas": 175, "kategori_pltu": "mulut_tambang", "izin_ptbae": "1.089", "rencana_emisi": 50000, "produksi_listrik_bruto": 1300000, "nama_perusahaan": "PT DSPP Power S"},  # Perubahan disini
        {"nama_pltu": "kalteng", "unit_ke": 1, "kapasitas": 100, "kategori_pltu": "mulut_tambang", "izin_ptbae": "1.089", "rencana_emisi": 50000, "produksi_listrik_bruto": 1300000, "nama_perusahaan": "PT SKS Electricity"},  # Perubahan disini
        {"nama_pltu": "kalteng", "unit_ke": 2, "kapasitas": 100, "kategori_pltu": "mulut_tambang", "izin_ptbae": "1.089", "rencana_emisi": 40000, "produksi_listrik_bruto": 1300000, "nama_perusahaan": "PT SKS Electricity"},  # Perubahan disini

    ]

    try:
           
        # Memasukkan data emisi setelah semua data perusahaan dan pltu dimasukkan
        for data in emisi_data:
            insert_emisi(conn, data)

    finally:
        # Menutup koneksi
        conn.close()

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
