# Morehub

## [Visit Morehub Right Now!](http://krisna-putra-morehub.pbp.cs.ui.ac.id/)

### Pertanyaan

1. Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).

    **JAWAB**:

    a. Pastikan setup telah selesai disiapkan, termasuk django telah terinstall, dan _virtual environment_ dapat berjalan dengan baik.

    b. Pertama-tama, saya membuat requirements.txt yang berisi dependencies proyek Django yang akan saya buat, berdasarkan dependencies pada sesi tutorial.

    c. Jika sekiranya tidak ada masalah, selanjutnya saya membuat proyek Django dengan perintah `django-admin startproject Morehub .` dimana Morehub adalah nama aplikasi e-dagang saya.

    d. Selanjutnya, saya membuat aplikasi `main` dengan menggunakan perintah `python manage.py startapp main`.

    e. Saat aplikasi `main` sudah dibuat, saya membuat model `Product`  di `models.py` pada folder `main` dengan atribut sebagai berikut: 

    ```python
        from django.db import models

        class Product(models.Model):
            name = models.CharField(max_length=100)
            price = models.DecimalField(max_digits=10, decimal_places=2)
            description = models.TextField()
            quantity = models.IntegerField()
            category = models.CharField(max_length=100)
            featured = models.BooleanField()
    ```
    Namun, saat masa Tugas 1 ini, atribut model diatas masih _subject to change_, karena proyeknya belum dikerjakan. Namun, saya sudah melakukan migrasi model ke dalam basis data lokal.

    f. Setelah itu, buat folder baru di dalam aplikasi `main` bernama `templates` berisi `main.html` yang dapat menampilkan data dari model `Product`.

    g. Kemudian, saya mengintegrasikan komponen MVT dengan membuat fungsi `show_main` di `views.py` yang akan mengembalikan _response_ berupa _template_ HTML yang menampilkan nama aplikasi dan nama serta kelas saya.

    ```python
        from django.shortcuts import render

        def show_main(request):
            context = {
                'name': 'Film kamera analog',
                'price': '120000',
                'description': 'awas terbakar',
                'quantity': '10',
                'category': 'Lifestyle',
                'featured': True
            }

            return render(request, "main.html", context)
    ```

    h. Setelah itu, saya membuat routing URL aplikasi `main` untuk mengatur rute URL spesifik untuk fitur-fitur dalam aplikasi tersebut. 

        ```python
            from django.urls import path
            from main.views import show_main

            app_name = 'main'

            urlpatterns = [
                path('', show_main, name='show_main'),
            ]
        ```

    i. Kemudian, saya membuat routing di tingkat proyek agar proyek saya dapat menjalankan aplikasi `main` dengan menambahkan path `/`ke `urls.py` proyek.

        ```python
            from django.contrib import admin
            from django.urls import path, include

            urlpatterns = [
                path('', include('main.urls')),
                path('admin/', admin.site.urls),
            ]
        ```

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.

    **JAWAB**:

    ![Diagram](diagrams/diagram.png)

    a. Client membuka aplikasi tersebut melalui browser dengan mengirimkan _request_ ke _main_ URL (`/`) yang kemudian diterima oleh URL routing (`urls.py`).

    b. Setelah itu, _request_ tersebut diarahkan ke show_main() di `views.py`. Perhatikan bahwa path `/` ditulis dengan `''` di `urls.py`.

    c. Fungsi show_main() yang sudah memiliki pre-defined model (context), kini bisa mengisi `templates/main.html` dengan konten yang ada pada context tersebut.

    d. `main.html` di-_render_ oleh `views.py` dan dikirimkan sebagai `response` ke client melalui browser. 

3. Jelaskan fungsi `git` dalam pengembangan perangkat lunak!

    **JAWAB**:

    a. **Version Control** 
        Git melacak setiap perubahan kode, sehingga memungkinkan developer riwayat versi pengembangan dan memungkinkan untuk beralih ke versi sebelumnya, contohnya menggunakan command `commit`, `reset`, dan `checkout`.

    b. **Collaboration**
        Git memungkinkan kolaborasi antar developer yang bekerja pada suatu projek yang sama. Dengan `branching` dan `merging`, para developer dapat bekerjasama tanpa mengganggu pekerjaan satu sama lain.

    c. **Deployment**
        Git memungkinkan developer untuk melakukan _deployment_ ke _production server_ secara mudah melalui command `push` untuk mengirim versi terbaru dan `pull` untuk menerima versi terbaru.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

    **JAWAB**:

    a. **Fitur Bawaan**
        Dengan fitur bawaan yang _beginner-friendly_ seperti pengelolaan basis data, autentikasi, dan manajemen admin, pemula diharapkan dapat lebih mudah memahami konsep dasar pengembangan perangkat lunak.

    b. **Struktur**
        Dengan mengikuti pola MVT (Model-View-Template), para pemula diharapkan lebih memahami struktur arsitektur web dan dapat lebih mudah memisahkan logika _back-end_ dan _front-end_.
    
    c. **Keamanan**
        Django dilengkapi fitur keamanan bawaan yang dapat melindungi dari serangan siber, seperti XSS, SQL Injection, MitM, dll.

    d. **Skalabilitas**
        Django dirancang untuk menangani aplikasi web yang besar dan kompleks, sehingga pemula juga dapat belajar cara me-_maintain_ suatu aplikasi kompleks yang terus berkembang.

    e. **ORM Bawaan**
        Django secara otomatis memberikan API abstraksi basis data yang memungkinkan user untuk membuat, menerima, mengupdate, dan menghapus objek. Dengan demikian, pemula tidak perlu berhadapan langsung dengan SQL mentah. 

5. Mengapa model pada Django disebut sebagai _ORM_?

    **JAWAB**:

    Model pada Django disebut ORM karena mereka menghubungkan struktur objek dalam kode python dengan tabel-tabel dalam database relasional, seperti halnya pada SQL.


## Checklist Tugas

-   [x] Membuat sebuah proyek Django baru.
-   [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.
-   [x] Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`.
-   [x] Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib sebagai berikut.
    -   `name`
    -   `price`
    -   `description`
-   [x] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah _template_ HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
-   [x] Membuat sebuah _routing_ pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.
-   [x] Melakukan _deployment_ ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
-   [x] Membuat sebuah `README.md` yang berisi tautan menuju aplikasi PWS yang sudah di- _deploy_ , serta jawaban dari beberapa pertanyaan berikut.
    -   Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).
    -   Buatlah bagan yang berisi _request client_ ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
    -   Jelaskan fungsi `git` dalam pengembangan perangkat lunak!
    -   Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    -   Mengapa model pada Django disebut sebagai _ORM_?






