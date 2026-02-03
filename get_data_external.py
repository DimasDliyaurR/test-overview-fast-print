import os
import requests
import hashlib
from datetime import datetime
import json
import mysql.connector
import environ 

env = environ.Env(DEBUG=(bool,True))
environ.Env.read_env(".env")

url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
now = datetime.now()

tgl_bln_thn = now.strftime("%d%m%y")
jam = now.strftime("%H")
username = f"tesprogrammer{tgl_bln_thn}C{jam}"

tgl = str(now.day)  # Jadi "1", bukan "01"
bln = str(now.month)  # Jadi "2", bukan "02"
thn = now.strftime("%y")  # "26"

password_raw = f"bisacoding-{now.strftime('%d')}-{now.strftime('%m')}-{thn}"
password_md5 = hashlib.md5(password_raw.encode()).hexdigest()

payload = {"username": username, "password": password_md5}

session = requests.Session()

print(f"DEBUG:")
print(f"Target Username : {username}")
print(f"Target Password : {password_raw} -> {password_md5}")
print("-" * 30)

db_config = {
    "host": os.environ.get("SQL_HOST","localhost"),
    "user":  os.environ.get("SQL_USER","root"),
    "password": os.environ.get("SQL_PASSWORD",""),
    "database":  os.environ.get("SQL_DATABASE",""),
}

# Check the table has the data or not
def check_value_table(sql):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        cursor.execute(sql)

        row = cursor.fetchall()

        return True if len(row) > 0 else False
    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def insert_into_product(product_list):

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        # Query INSERT dengan ON DUPLICATE KEY UPDATE (Upsert)
        query = """
            INSERT INTO produk (nama_produk, harga, kategori_id, status_id)
            VALUES (%s, %s, %s, %s)
       """

        if check_value_table("select * from produk"):
            print("data produk sudah ada")
            return

        data_to_save = [
            tuple([i["nama_produk"], i["harga"], i["kategori"], i["status"]])
            for i in product_list
        ]

        cursor.execute("ALTER TABLE produk AUTO_INCREMENT = 1;")
        cursor.executemany(query, data_to_save)
        conn.commit()
        print(f"Data tersinkronisasi ke MySQL.")

    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def insert_into_kategori(kategori_list):

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:

        if check_value_table("select * from kategori"):
            print("data kategori sudah ada")
            return
        # Query INSERT dengan ON DUPLICATE KEY UPDATE (Upsert)
        query = """
            INSERT INTO kategori (nama_kategori)
            VALUES (%s)
        """

        data_to_save = [tuple([kategori]) for kategori in kategori_list]

        print(type(data_to_save[0]))
        print("kategori_list:", type(data_to_save), data_to_save)
        cursor.execute("ALTER TABLE kategori AUTO_INCREMENT = 1;")
        cursor.executemany(query, data_to_save)
        conn.commit()
        print(f"Data tersinkronisasi ke MySQL.")

    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


try:
    response = session.post(url, data=payload)

    res_data = response.json()
    print("STATUS RESPONSE:", json.dumps(res_data, indent=4, sort_keys=True))

    status = ["tidak bisa dijual", "bisa dijual"]
    data = res_data["data"]
    data_kategori_raw = list(map(lambda x: x["kategori"], data))
    data_kategori = list(dict.fromkeys(data_kategori_raw))
    data_product = []

    print("Jumlah data :", len(data))
    print("data no :", list(data))
    
    # Get Produk Data
    for i in range(len(data)):
        data_inner_product = {}

        product = data[i]
        data_inner_product["id_produk"] = int(product["id_produk"])
        data_inner_product["nama_produk"] = product["nama_produk"]
        data_inner_product["harga"] = product["harga"]
        data_inner_product["kategori"] = data_kategori.index(product["kategori"]) + 1
        data_inner_product["status"] = status.index(product["status"]) + 1

        data_product.append(data_inner_product)

    print("get res...")
    print("insert into kategori with value:", ",".join(data_kategori))
    insert_into_kategori(data_kategori)
    print("insert into produk")
    insert_into_product(data_product)

    # Does the data catch up ?
    if res_data.get("error") == 0:
        print("\n✅ LOGIN BERHASIL!")
    else:
        print("\n❌ GAGAL:", res_data.get("ket"))

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
