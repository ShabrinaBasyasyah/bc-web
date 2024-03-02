import psycopg2

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="ptbae",  # Ganti dengan nama database Anda
            user="postgres",  # Ganti dengan nama pengguna Anda
            password="dks120193",  # Ganti dengan kata sandi Anda
            host="localhost",  # Ganti dengan host database Anda
            port="5433"  # Ganti dengan port database Anda
        )
        return conn
    except psycopg2.Error as e:
        print("Error saat terhubung ke database:", e)
        return None
