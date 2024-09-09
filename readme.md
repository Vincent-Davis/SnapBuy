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
          -------------------------------------------
          |                                         |
    Root Project (app/urls.py)                 Application (main/urls.py)
    - Bertugas mendistribusikan                - Menangani URL yang spesifik
      request ke aplikasi-aplikasi               untuk aplikasi tertentu.
      yang ada di project.                     - Misalnya: URL utama '' diarahkan
    - Menggunakan include() untuk                ke fungsi show_main di views.py.
      memetakan URL global ke aplikasi.         ---------------------------------
    - Contoh: path('', include('main.urls'))    |
      untuk mengarahkan request                 |
      ke aplikasi 'main'.                       v
          -------------------------------------------
                           |
                           v
             3. View Processing (views.py)
            - Memproses request dan mengambil data
              dari model (jika diperlukan).
            - Menyiapkan data dalam bentuk context untuk
              dikirim ke template.
            - Contoh: Menyiapkan context berisi nama, kelas,
              dan nama aplikasi.
                           |
                           v
         4. Interaction with Model (models.py)
            - Jika view memerlukan data dari database,
              model akan dipanggil untuk mengambil atau
              memodifikasi data.
            - Misalnya: ProductEntry adalah model yang merepresentasikan
              produk dengan kolom nama, price, description, dsb.
                           |
                           v
               5. Rendering Template (HTML)
            - Template HTML akan merender data dari context yang
              dikirim oleh views.
            - Contoh: Menampilkan variabel {{ nama }}, {{ kelas }},
              dan {{ aplikasi }} pada halaman web.
                           |
                           v
          6. Response (HTML) dikirim kembali ke client
            - Setelah template dirender, response dikirimkan
              kembali ke browser client.
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