import psycopg2

class saldo:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        
    def get_saldo(self):
        try:
            connection = psycopg2.connect(
                host=self.host,
                database = self.database,
                user=self.user,
                passwors = self.password
            )
            
            cursor = connection.cursor()
            
            cursor.execute("SELECT saldo FROM emisi")
            
            saldo = cursor.fetchone()[0]
            
            cursor.close()
            connection.close()
            
            return saldo
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
            
host = "localhost"
database = "ptbae"
user = "nama_pengguna"
password = "dks120193"
port = 5433

saldo_manager = saldo(host, database, user, password)
saldo = saldo_manager.get_saldo()
print("Saldo saat ini: ", saldo)