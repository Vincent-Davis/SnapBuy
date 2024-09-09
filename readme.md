<h1> 1.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</h1>

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

<h1>2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.</h1>

Berikut adalah bagan yang berisi request client ke web berbasis Django
1. Mengirimkan request ke server
2. URL Routing (urls.py)  
   - Berfungsi untuk memetakan URL yang diminta pengguna ke views.py
3. View Processing (views.py)
   - Memproses request dan menentukan data apa yang akan ditampilkan ke pengguna.
   - Data berupa dictionary context disiapkan untuk dikirim ke template, dalam project ini contohnya adalah nama, kelas, dan nama aplikasi
4. Interaction with Model (models.py)
   - File ini adalah file yang mendefinisikan model dan merepresentasikan tabel dalam database.
   - Dalam contoh ini, Class ProductEntry adalah tabel produknya, dan nama, price, descritpion, produk_terjual, dan rating adalah nama kolom dalam database.
5. Rendering Template (HTML)
   - File ini menampilkan data ke user dalam bentuk halaman web. Data yang ada di views nantinya akan di integrasikan dengan halaman web.
   - Pada kasus ini, nilai - nilai pada dictionary context pada views.py didapatkan dengan menulis {{aplikasi}}, {{nama}}, {{kelas}}
6. Response (HTML) dikirim kembali ke client
   - Client mendapatkan web page yang sesuai


<h1>3. Jelaskan fungsi git dalam pengembangan perangkat lunak!</h1>
Dalam sebuah pengembangan perangkat lunak, git memiliki banyak fungsi 
1. Kolaborasi Tim
Git sangat membantu dalam sebuah proses pengembangan perangkat lunak yang dilakukan oleh lebih 1 orang. Keberadaan git membantu programmer untuk bisa bekerja di cabang yang berbeda tanpa mengganggu proyek satu sama lain. Nantinya, setelah selesai, cabang - cabang tersebut bisa di merge.
2. Backup dan Commit tracking
Dalam sebuah pengembangan, umum terjadi sebuah kesalahan ketika melakukan perubahan. Keberadaan git menjadi sebuah penjamin keamanan, karena kita bisa kembali ke versi yang kita save sebelumnya. Selain itu, keberadaan git juga menjadi jawaban dari kehilangan file, karena keberadan git memastikan kita mempunyai sebuah backup yang dapat digunakan.

<h1>4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?</h1>

Menurut saya, Django sering dijadikan pilihan untuk memulai pembelajaran pengembangan perangkat lunak karena pertama dia berbasis Python, yang mudah dipahami. Django juga  menyediakan banyak fitur - fitur yang bermanfaat seperti autentikasi, ORM, dan admin panel. Framework dari django juga mengikuti pola MTV, dan memiliki dokumentasi yang lengkap. Hal ini tentu akan sangat membantu bagi para mahasiswa dalam memahami konsep pembuatan proyek web. Django juga mempunyai community support yang cukup baik, mengingat besarnya komunitas Django.

<h1>5. Mengapa model pada Django disebut sebagai ORM?</h1>

Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena django memetakan objek - objek di dalam python ke tabel database relational, seperti SQL. Dengan ORM, pengembang dapat bekerja dengan database dengan menggunakan bahasa python tanpa menggunakan bahasa SQL sama sekali. ORM akan mengubah query database menjadi objek python, dan hal sebaliknya juga berlaku.