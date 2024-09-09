<h2> 1.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</h2>

* Membuat proyek Django baru
    1. Membuat direktori folder baru bernama Snap Buy
    2. Membuat virtual environment python
    3. Menginstall package yang dibutuhkan dari requirements.txt
    4. Buat folder proyek dengan command django-admin startproject snap_buy

* Membuat aplikasi pada proyek
    1. Buat aplikasi bernama main dengan python manage.py startapp main
    2. Tambahkan aplikasi main ke installed_apps pada settings.py
    3. Membuat folder template dan diisi dengan file main.html di dalam folder main

* Edit models.py
    1. Membuat class ProductEntry
    2. Menambahkan field yang sesuai untuk tiap entry

* Migrasi Model
    1. lakukan python manage.py makemigrations
    2. python manage.py migrate

* Edit views.py
    1. Buat fungsi show_main yang mengandung data nama aplikasi, nama siswa, dan kelas
    2. Return render dari fungsi dan context

* Modifikasi main.html
    1. Mengganti kolom yang datanya ada di views.py dengan {{variabel}}

* Routing URL
    1. Ganti urlpatterns pada urls.py (main) dengan path kosong, dan nama fungsi sesuai dengan yang ada di views.py show_main
    2. Ganti urlpatterns pada urls.py (project) dengan path kosong, lalu import function include untuk menambahkan url yang ada pada main.

* PWS
    1. Buat proyek baru dengan nama snapbuy
    2. Melakukan push ke PWS

* Github
    1. Push local git ke github 

<h2>2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.</h2>

                        Client (Browser)
                               |
                               v
               1. Mengirimkan request ke server
                               |
                               v
          2. URL Routing (urls.py)
          -----------------------------------------
          |                                       |
   **Root Project (app/urls.py)**           **Application (main/urls.py)**
   - Berfungsi sebagai pengendali          - Berfungsi untuk menangani URL
     utama untuk project.                    yang spesifik untuk aplikasi.
   - Mendistribusikan request dari         - Mengarah ke views.py untuk aplikasi
     URL global ke aplikasi-aplikasi         tertentu (misalnya aplikasi 'main').
     di dalam project, menggunakan         - Di sinilah route spesifik aplikasi
     fungsi `include()` untuk               diatur, misalnya:
     menyertakan `urls.py` dari aplikasi      - path('', show_main) untuk menampilkan
     tertentu.                                halaman utama aplikasi.
   - Misalnya: `path('', include('main.urls'))` |
   artinya URL `http://domain.com/` akan       |
   diteruskan ke `urls.py` di aplikasi         |
   `main`.                                     |
          -----------------------------------------       
                               |
                               v
                    3. View Processing (views.py)
                   - View berfungsi untuk menangani logika bisnis.
                   - View mengambil data yang dibutuhkan dari model
                     (jika diperlukan), memprosesnya, dan menyiapkan 
                     data dalam bentuk dictionary `context` untuk
                     dikirim ke template.
                   - Misalnya, view `show_main` memproses request
                     untuk halaman utama dan menyiapkan data seperti
                     `nama`, `kelas`, dan `nama aplikasi`.
                               |
                               v
             4. Interaction with Model (models.py)
            - Jika view membutuhkan data dari database, model akan
              dipanggil. Model dalam Django merepresentasikan tabel
              dalam database dan mengatur bagaimana data diambil,
              dimodifikasi, atau disimpan.
            - Dalam project ini, model `ProductEntry` adalah tabel
              yang merepresentasikan produk, dengan kolom seperti
              `nama`, `price`, `description`, `produk_terjual`, dan
              `rating`.
                               |
                               v
                  5. Rendering Template (HTML)
            - Setelah view memproses data, template HTML digunakan
              untuk menampilkan data tersebut dalam halaman web.
            - Template menggunakan Django Template Language (DTL)
              untuk menyisipkan data dari context yang dikirim oleh
              view ke dalam halaman HTML.
            - Misalnya, dalam template, data seperti `{{ aplikasi }}`,
              `{{ nama }}`, dan `{{ kelas }}` ditampilkan di halaman.
                               |
                               v
               6. Response (HTML) dikirim kembali ke client
            - Setelah template dirender, HTML dikirim sebagai response
              ke browser client, yang kemudian menampilkan halaman web
              sesuai dengan data yang diproses.
                               |
                               v
                  Client (Browser menampilkan halaman)



<h2>3. Jelaskan fungsi git dalam pengembangan perangkat lunak!</h2>
Dalam sebuah pengembangan perangkat lunak, git memiliki banyak fungsi 
1. Kolaborasi Tim
Git sangat membantu dalam sebuah proses pengembangan perangkat lunak yang dilakukan oleh lebih 1 orang. Keberadaan git membantu programmer untuk bisa bekerja di cabang yang berbeda tanpa mengganggu proyek satu sama lain. Nantinya, setelah selesai, cabang - cabang tersebut bisa di merge.
2. Backup dan Commit tracking
Dalam sebuah pengembangan, umum terjadi sebuah kesalahan ketika melakukan perubahan. Keberadaan git menjadi sebuah penjamin keamanan, karena kita bisa kembali ke versi yang kita save sebelumnya. Selain itu, keberadaan git juga menjadi jawaban dari kehilangan file, karena keberadan git memastikan kita mempunyai sebuah backup yang dapat digunakan.

<h2>4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?</h2>

Menurut saya, Django sering dijadikan pilihan untuk memulai pembelajaran pengembangan perangkat lunak karena pertama dia berbasis Python, yang mudah dipahami. Django juga  menyediakan banyak fitur - fitur yang bermanfaat seperti autentikasi, ORM, dan admin panel. Framework dari django juga mengikuti pola MTV, dan memiliki dokumentasi yang lengkap. Hal ini tentu akan sangat membantu bagi para mahasiswa dalam memahami konsep pembuatan proyek web. Django juga mempunyai community support yang cukup baik, mengingat besarnya komunitas Django.

<h2>5. Mengapa model pada Django disebut sebagai ORM?</h2>

Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena django memetakan objek - objek di dalam python ke tabel database relational, seperti SQL. Dengan ORM, pengembang dapat bekerja dengan database dengan menggunakan bahasa python tanpa menggunakan bahasa SQL sama sekali. ORM akan mengubah query database menjadi objek python, dan hal sebaliknya juga berlaku.