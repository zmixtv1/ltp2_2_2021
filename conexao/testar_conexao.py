import mysql.connector


def conectar():
    cnx = mysql.connector.connect(user='root', password='uniceub', host='localhost', database='teste')
    print("conectado", cnx.is_connected())
    print("Conjunto de catacteres=", cnx.charset)

    cnx.close()


if __name__ == '__main__':
    conectar()
