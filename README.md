## ⚙️ Instalasi & Setup

Ikuti langkah-langkah berikut untuk menjalankan project di lokal:

1. **Clone Repository**
    ```shell
    git clone https://github.com/DimasDliyaurR/test-overview-fast-print.git
    cd test-overview-fast-print
    ```
    
2. **Buat Virtual Environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```
    
3. **Install Dependencies**
    ```shell
    pip install -r requirements.txt
    ```
    
4. **Migrasi Database**
    
    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```
    
5. **Jalankan Server**
    
    
    ```shell
    python manage.py runserver
    ```
    

## Scrapping data recruitment api

1. **Siapkan table sebagai berikut**
    
```sql
--
-- Create model Kategori
--
CREATE TABLE `kategori` (
	`id_kategori` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
	`nama_kategori` varchar(50) NOT NULL
);

--
-- Create model Status
--
CREATE TABLE `status` (
	`id_status` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
	`nama_status` varchar(255) NOT NULL
);

--
-- Create model Produk
--
CREATE TABLE `produk` (
	`id_produk` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
	`nama_produk` varchar(255) NOT NULL, `harga` numeric(8, 2) NOT NULL,
	`kategori_id` bigint NOT NULL, `status_id` bigint NOT NULL);

ALTER TABLE `produk` ADD CONSTRAINT `produk_kategori_id_1c4a5c0e_fk_kategori_id_kategori` FOREIGN KEY (`kategori_id`) REFERENCES `kategori` (`id_kategori`);

ALTER TABLE `produk` ADD CONSTRAINT `produk_status_id_b270dde3_fk_status_id_status` FOREIGN KEY (`status_id`) REFERENCES `status` (`id_status`);
```

2. **Scapping data**

```shell
python get_data_external.py
```
