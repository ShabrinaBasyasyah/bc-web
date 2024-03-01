from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from psycopg2 import sql
import random
import string
import uuid

app = Flask(__name__)

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(8))
    return password

def generate_id_penawaran():
    return str(uuid.uuid4())

def generate_id_periode_penawaran():
    return str(uuid.uuid4())

def generate_id_permintaan():
    return str(uuid.uuid4())

def generate_id_periode_permintaan():
    return str(uuid.uuid4())


def get_company_info(nama_perusahaan):
    conn = psycopg2.connect(
        dbname="ptbae",
        user="postgres",
        password="dks120193",
        host="localhost",
        port=5433
    )
    cur = conn.cursor()
    cur.execute("SELECT id_perusahaan, nama_perusahaan FROM perusahaan WHERE nama_perusahaan ILIKE %s", (nama_perusahaan,))
    company_data = cur.fetchone()
    cur.close()
    conn.close()
    return company_data

def authenticate_signup(nama_perusahaan):
    company_data = get_company_info(nama_perusahaan)
    if company_data:
        company_id = company_data[0]
        company_name = company_data[1]
        return company_id, company_name
    return None, None

def save_user_data(id_perusahaan, username, password):
    # Generate hashed password
    
    # Simpan data pengguna ke dalam tabel users
    conn = psycopg2.connect(
        dbname="ptbae",
        user="postgres",
        password="dks120193",
        host="localhost",
        port=5433
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO users (id_perusahaan, username, password) VALUES (%s, %s, %s)", (id_perusahaan, username, password))
    conn.commit()
    cur.close()
    conn.close()



def authenticate_signin(id_perusahaan, username, password):
    conn = psycopg2.connect(
        dbname="ptbae",
        user="postgres",
        password="dks120193",
        host="localhost",
        port=5433
    )
    cur = conn.cursor()
    cur.execute("SELECT id_perusahaan, username, password FROM users WHERE id_perusahaan = %s AND username = %s", (id_perusahaan, username,))
    user_data = cur.fetchone()
    cur.close()
    conn.close()
      
    if user_data:
        stored_id_perusahaan, stored_username, stored_password = user_data
        # Decode the hashed password from the database before comparing
        if id_perusahaan == stored_id_perusahaan and username == stored_username and  password==stored_password:
            return True
    return False

def get_saldo(nama_perusahaan):
    conn = psycopg2.connect(
        dbname="ptbae",
        user="postgres",
        password="dks120193",
        host="localhost",
        port=5433
    )
    cur = conn.cursor()
    cur.execute("SELECT saldo FROM emisi WHERE nama_perusahaan ILIKE %s OR nama_perusahaan = %s", (nama_perusahaan, f'"{nama_perusahaan}"'))
    saldo_data = cur.fetchone()
    cur.close()
    conn.close()
    return saldo_data[0] if saldo_data else None

def save_penawaran(id_penawaran, id_periode_penawaran, id_perusahaan, tanggal_penawaran, tanggal_awal_penawaran,
                   tanggal_akhir_penawaran, nama_pltu_penawar, unit_penawar, ptbae_ditawarkan, satuan, harga, mata_uang,
                   sisa_penawaran, satuan_sisa_penawaran, available_penawaran):
    conn = psycopg2.connect(
        dbname="ptbae",
        user="postgres",
        password="dks120193",
        host="localhost",
        port=5433
    )
    cur = conn.cursor()

    cur.execute("INSERT INTO penawaran (id_penawaran, id_periode_penawaran, id_perusahaan, tanggal_penawaran, "
                "tanggal_awal_penawaran, tanggal_akhir_penawaran, nama_pltu_penawar, unit_penawar, ptbae_ditawarkan, "
                "satuan, harga, mata_uang, sisa_penawaran, satuan_sisa_penawaran, available_penawaran) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (id_penawaran, id_periode_penawaran, id_perusahaan, tanggal_penawaran, tanggal_awal_penawaran,
                 tanggal_akhir_penawaran, nama_pltu_penawar, unit_penawar, ptbae_ditawarkan, satuan, harga, mata_uang,
                 sisa_penawaran, satuan_sisa_penawaran, available_penawaran))

    conn.commit()
    cur.close()
    conn.close()

def save_permintaan(id_permintaan, id_periode_permintaan, id_pelaku_permintaan, tanggal_permintaan,
                    tanggal_awal_permintaan, tanggal_akhir_permintaan, nama_pltu_peminta, unit_peminta, ptbae_diminta,
                    satuan, harga, mata_uang, sisa_permintaan, satuan_sisa_permintaan):
    conn = psycopg2.connect(
        dbname = "ptbae",
        user="postgres",
        password="dks120193",
        port="5433"
    )   
    
    cur = conn.cursor()
    
    cur.execute("INSERT INTO permintaan (id_permintaan, id_periode_permintaan, id_pelaku_permintaan, tanggal_permintaan,"
                "tanggal_awal_permintaan, tanggal_akhir_permintaan, nama_pltu_peminta, unit_peminta, ptbae_diminta,"
                "satuan, harga, mata_uang, jumlah_terbeli, satuan_terbeli, sisa_permintaan, satuan_sisa_permintaan) "
                "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (id_permintaan, id_periode_permintaan, id_pelaku_permintaan, tanggal_permintaan,
                tanggal_awal_permintaan, tanggal_akhir_permintaan, nama_pltu_peminta, unit_peminta, ptbae_diminta,
                satuan, harga, mata_uang, sisa_permintaan, satuan_sisa_permintaan)) 
    
    conn.commit()
    cur.close()
    conn.close()
    
# Route untuk halaman utama
@app.route('/')
def landing():
    return render_template('landingpage.html')

# Route untuk halaman sign up
@app.route('/signup')
def signup():
    return render_template('signup.html')

# Route untuk autentikasi sign up
@app.route('/signup/authenticate', methods=['POST'])
def authenticate_signup_route():
    nama_perusahaan = request.form['nama_perusahaan']
    id_perusahaan, nama_perusahaan = authenticate_signup(nama_perusahaan)
    if id_perusahaan and nama_perusahaan:
        # Peroleh username dan password yang diinput oleh pengguna
        username = request.form['username']
        password = generate_password()
        # Simpan data pengguna ke dalam tabel users
        save_user_data(id_perusahaan, username, password)
        # Redirect ke halaman berhasil sign up
        return render_template('signup_berhasil.html', company_id=id_perusahaan, company_name=nama_perusahaan, password=password)
    else:
        return redirect(url_for('signup_failed'))

# Route untuk halaman sign up gagal
@app.route('/signup_failed')
def signup_failed():
    return render_template('signup_failed.html')

# Route untuk mencoba lagi
@app.route('/try_again', methods=['POST'])
def try_again():
    return redirect(url_for('login'))

# Route untuk halaman login
@app.route('/login')
def login():
    return render_template('signin.html')

# Route untuk autentikasi sign in
@app.route('/signin/authenticate', methods=['POST'])
def authenticate_signin_route():
    username = request.form['username']
    password = request.form['password']  # Get the password directly from the form
    id_perusahaan = request.form['id_perusahaan']
    if authenticate_signin(id_perusahaan, username, password):
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login_failed'))
    
# Route untuk halaman login gagal
@app.route('/login_failed')
def login_failed():
    return render_template('signin_failed.html')

# Route untuk dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Route untuk halaman home
@app.route('/home')
def home():
    return render_template('dashboard.html')       
# Route to render the form for creating an offer
@app.route('/create_penawaran')
def buat_penawaran():
    return render_template('create_penawaran.html')

# Route to handle the form submission and save the offer
@app.route('/save_penawaran', methods=['POST'])
def save_penawaran_route():
    print(request)
    if request.method == 'POST':
        print("Metode permintaan: POST")  # Pernyataan debugging

        # Menghasilkan id_penawaran dan id_periode_penawaran
        id_penawaran = generate_id_penawaran()
        id_periode_penawaran = generate_id_periode_penawaran()
        
        # Mengambil data dari formulir
        id_perusahaan = request.form.get('id_perusahaan')
        tanggal_penawaran = request.form.get('tanggal_penawaran')
        tanggal_awal_penawaran = request.form.get('tanggal_awal_penawaran')
        tanggal_akhir_penawaran = request.form.get('tanggal_akhir_penawaran')
        nama_pltu_penawar = request.form.get('nama_pltu_penawar')
        unit_penawar = request.form.get('unit_penawar')
        ptbae_ditawarkan = request.form.get('ptbae_ditawarkan')
        satuan = request.form.get('satuan')
        harga = request.form.get('harga')
        mata_uang = request.form.get('mata_uang')
        sisa_penawaran = request.form.get('sisa_penawaran')
        satuan_sisa_penawaran = request.form.get('satuan_sisa_penawaran')
        available_penawaran = request.form.get('available_penawaran')

        # Pernyataan debugging untuk mencetak data dari formulir
        print("ID Perusahaan:", id_perusahaan)
        print("Tanggal Penawaran:", tanggal_penawaran)
        print("Tanggal Awal Penawaran:", tanggal_awal_penawaran)
        print("Tanggal Akhir Penawaran:", tanggal_akhir_penawaran)
        print("Nama PLTU Penawar:", nama_pltu_penawar)
        print("Unit Penawar:", unit_penawar)
        print("PTBAE Ditawarkan:", ptbae_ditawarkan)
        print("Satuan:", satuan)
        print("Harga:", harga)
        print("Mata Uang:", mata_uang)
        print("Sisa Penawaran:", sisa_penawaran)
        print("Satuan Sisa Penawaran:", satuan_sisa_penawaran)
        print("Available Penawaran:", available_penawaran)

        # Validasi data sebelum menyimpan ke database
        if not id_perusahaan:
            return "ID Perusahaan tidak boleh kosong."
        elif not tanggal_penawaran:
            return "Tanggal Penawaran tidak boleh kosong."
        elif not tanggal_awal_penawaran:
            return "Tanggal Awal Penawaran tidak boleh kosong."
        elif not tanggal_akhir_penawaran:
            return "Tanggal Akhir Penawaran tidak boleh kosong."
        elif not nama_pltu_penawar:
            return "Nama PLTU Penawar tidak boleh kosong."
        elif not unit_penawar:
            return "Unit Penawar tidak boleh kosong."
        elif not ptbae_ditawarkan:
            return "PTBAE Ditawarkan tidak boleh kosong."
        elif not satuan:
            return "Satuan tidak boleh kosong."
        elif not harga:
            return "Harga tidak boleh kosong."
        elif not mata_uang:
            return "Mata Uang tidak boleh kosong."
        elif not sisa_penawaran:
            return "Sisa Penawaran tidak boleh kosong."
        elif not satuan_sisa_penawaran:
            return "Satuan Sisa Penawaran tidak boleh kosong."
        elif not available_penawaran:
            return "Available Penawaran tidak boleh kosong."
        else:
            try:
                # Menyimpan data penawaran ke dalam database
                save_penawaran(id_penawaran, id_periode_penawaran, id_perusahaan, tanggal_penawaran, 
                               tanggal_awal_penawaran, tanggal_akhir_penawaran, nama_pltu_penawar, 
                               unit_penawar, ptbae_ditawarkan, satuan, harga, mata_uang, sisa_penawaran, 
                               satuan_sisa_penawaran, available_penawaran)
                
                # Redirect ke halaman berhasil penawaran
                return redirect(url_for('penawaran_berhasil'))
            except Exception as e:
                # Tangani kesalahan jika terjadi
                return render_template('penawaran_gagal.html')
    else:
        # Handle the case where the request method is not POST
        return "Method not allowed"


@app.route('/penawaran_berhasil')
def penawaran_berhasil():
    return render_template('penawaran_berhasil.html')

@app.route('/create_permintaan')
def buat_permintaan():
    return render_template('create_permintaan.html')

@app.route('/save_permintaan', methods=['POST'])
def save_permintaan_route():
    print(request)
    if request.method == 'POST':
        print("Metode Permintaan: POST")
        
        id_permintaan = generate_id_permintaan()
        id_periode_permintaan = generate_id_periode_permintaan()
        
        id_pelaku_permintaan = request.form.get('id_pelaku_permintaan')
        tanggal_permintaan = request.form.get('tanggal_permintaan')
        tanggal_awal_permintaan = request.form.get('tanggal_awal_permintaan')
        tanggal_akhir_permintaan = request.form.get('tanggal_akhir_permintaan')
        nama_pltu_peminta = request.form.get('nama_pltu_peminta')
        unit_peminta = request.form.get('unit_peminta')
        ptbae_diminta = request.form.get('ptbae_diminta')
        satuan = request.form.get('satuan')
        harga = request.form.get('harga')
        mata_uang = request.form.get('mata_uang')
        sisa_permintaan = request.form.get('sisa_permintaan')
        satuan_sisa_permintaan = request.form.get('satuan_sisa_permintaan')
        
        print("ID Perusahaan:", id_pelaku_permintaan)
        print ("Tanggal Permintaan:", tanggal_permintaan)
        print("Tanggal Awal Permintaan:", tanggal_awal_permintaan )
        print("Tanggal Akhir Permintaan:", tanggal_akhir_permintaan)
        print("nama pltu peminta:", nama_pltu_peminta)
        print("unit peminta:", unit_peminta)
        print("PTBAE diminta:", ptbae_diminta)
        print("satuan:", satuan)
        print("harga:", harga)
        print("mata_uang:", mata_uang)
        print("sisa permintaan:", sisa_permintaan)
        print("satuan sisa permintaan:", satuan_sisa_permintaan)
        
        if not id_pelaku_permintaan:
            return "ID Perusahaan tidak boleh kosong"
        elif not tanggal_permintaan:
            return "tanggal permintaan tidak boleh kosong"
        elif not tanggal_awal_permintaan:
            return "tanggal awal permintaan tidak boleh kosong"
        elif not tanggal_akhir_permintaan:
            return "tanggal akhir permintaan tidak boleh kosong"
        elif not nama_pltu_peminta:
            return "nama pltu tidak boleh kosong"
        elif not unit_peminta:
            return "unit peminta tidak boleh kosong"
        elif not ptbae_diminta:
            return "ptbae diminta tidak boleh kosong"
        elif not satuan:
            return "satuan tidak boleh kosong"
        elif not harga: 
            return "harga tidak boleh kosong"
        elif not mata_uang:
            return "mata uang tidak boleh kosong"
        elif sisa_permintaan:
            return "sisa permintaan tidak boleh kosong"
        elif satuan_sisa_permintaan:
            return "satuan sisa permintaan tidak boleh kosong"
        else:
            try:
                save_permintaan(id_permintaan, id_periode_permintaan, id_pelaku_permintaan, tanggal_permintaan,
                    tanggal_awal_permintaan, tanggal_akhir_permintaan, nama_pltu_peminta, unit_peminta, ptbae_diminta,
                    satuan, harga, mata_uang, sisa_permintaan, satuan_sisa_permintaan)
                return redirect(url_for('permintaan_berhasil'))
            except Exception as e:
                return render_template('permintaan_gagal.html')
    else:
        return "Method not allowed"

@app.route('/permintaan_berhasil')
def permintaan_berhasil():
    return render_template('permintaan_berhasil.html')
           
# Route untuk transaksi beli
@app.route('/transaksibeli')
def buattransaksibeli():
    return render_template('transaksibeli.html')

# Route untuk transaksi jual
@app.route('/transaksijual')
def buattransaksijual():
    return render_template('transaksijual.html')

# Tambahkan route untuk halaman saldo
@app.route('/saldo')
def saldo():
    nama_perusahaan = request.args.get('nama_perusahaan')  # Ambil nama perusahaan dari query string
    print("Nilai dari parameter nama_perusahaan:", nama_perusahaan)  # Cetak nilai parameter nama_perusahaan
    saldo = get_saldo(nama_perusahaan)
    return render_template('saldo.html', saldo=saldo)

@app.route('/view_blockchain')
def view_blockchain():
    return render_template('view_blockchain.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
