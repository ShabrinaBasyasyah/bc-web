import psycopg2
import bcrypt
import random
import string

# Fungsi untuk membuat password acak dengan panjang 8 karakter
def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(8))
    return password

# Fungsi untuk menambahkan user baru ke database
def add_user(username, company_name):
    conn = psycopg2.connect(
        dbname="ptbae",
        user="postgres",
        password="dks120193",
        host="localhost",
        port=5433
    )
    cur = conn.cursor()

    # Periksa apakah perusahaan sudah terdaftar
    cur.execute("SELECT id_perusahaan FROM perusahaan WHERE nama_perusahaan = %s", (company_name,))
    company_id = cur.fetchone()

    if company_id:
        company_id = company_id[0]  # Mendapatkan nilai id_perusahaan dari tupel
        new_password = generate_password()
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        cur.execute("INSERT INTO users (username, password, id_perusahaan) VALUES (%s, %s, %s) RETURNING id_perusahaan", (username, hashed_password, company_id))
        inserted_id = cur.fetchone()[0]  # Mendapatkan ID perusahaan yang baru ditambahkan
        print(f"User baru telah ditambahkan untuk perusahaan {company_name} dengan username: {username}, Password: {new_password}, dan ID Perusahaan: {inserted_id}")
    else:
        print(f"Perusahaan dengan nama {company_name} tidak ditemukan. Silakan tambahkan perusahaan terlebih dahulu.")

    conn.commit()
    conn.close()
    return inserted_id

# Fungsi untuk autentikasi user
def authenticate(username, password):
    conn = psycopg2.connect(
        dbname="ptbae",
        user="postgres",
        password="dks120193",
        host="localhost",
        port=5433
    )
    cur = conn.cursor()

    cur.execute("SELECT password FROM users WHERE username = %s", (username,))
    stored_password = cur.fetchone()

    conn.close()

    if stored_password:
        if bcrypt.checkpw(password.encode('utf-8'), stored_password[0].encode('utf-8')):
            return True
    return False

# Contoh penggunaan
new_username = input("Masukkan username baru: ")
company_name = input("Masukkan nama perusahaan: ")
new_user_id = add_user(new_username, company_name)  # Memperbarui agar mengambil ID perusahaan yang baru ditambahkan

login_company_id = input("Masukkan id perusahaan Anda: ")
login_username = input("Masukkan username Anda: ")
login_password = input("Masukkan password Anda: ")

if authenticate(login_username, login_password):
    print("Login berhasil!")
else:
    print("Login gagal. Periksa kembali username, id, dan password Anda.")
