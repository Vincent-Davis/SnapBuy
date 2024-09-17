<h1>TUGAS 3 </h1>
<h2>1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?</h2>
1. Komunikasi antar komponen 
Dalam sebuah platform, tidak jarang kalau berbagai komponen dari platform, seperti layanan dan modul, harus saling berinteraksi agar fungsinya bisa berjalan normal. Data delivery memastikan setiap komponen mendapatkan informasi yang tepat di waktu yang tepat, sekalipun komponen - komponen tersebut berada di lokasi dan server yang berbeda. Misalnya, pada sebuah aplikasi e-commerce, modul pembayaran dan pengiriman harus bertukar data agar transaksi berjalan dengan lancar.

2. Konsistensi Data
Semakin besar sebuah platform, maka semakin banyak celah untuk terjadinya inkonsistensi data. Perubahan yang dilakukan oleh pengguna/admin pada sebuah bagian platform harus tercerminkan juga di bagian lain platform. Misalnya, di dalam sebuah e-commerce, ketika sebuah toko mengubah jumlah stock barang menjadi 0 (habis), perubahan tersebut harus secara real-time tercerminkan di komponen platform user. Sehingga, user tidak bisa memesan barang yang sudah habis. Data delivery memastikan perubahan yang dilakukan di suatu bagian bisa tersinkronisasi ke seluruh platform.

<h2>2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?</h2>
Secara umum, menurut saya JSON lebih baik dibandingkan XML, berikut alasannya : 

1. Format yang Ringkas
JSON Memiliki format yang lebih ringkas, karena dibandingkan dengan XML yang menggunakan tag pembuka dan tag penutup, json hanya menggunakan tanda kurung dan tanda kutip. Hal ini membuat JSON lebih ringkas dibanding XML
2. Kinerja yang lebih baik
Dikarenakan format JSON yang lebih ringkas dibanding dengan XML, JSON jadi lebih cepat diproses oleh browser dan aplikasi backend dibandingkan XML.
3. Kompatibel dengan JavaScript
Javascript secara langsung mendukung JSON, hal ini menyebabkan JSON jadi opsi yang lebih populer. Karena Javascript memiliki JSON sebagai sintaks, JSON dapat diurai atau dihasilkan dengan mudah.

<h2>3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?</h2>
Method is_valid() berfungsi untuk memeriksa validitas data yang dikirim melalui form. Validitas data ini dilihat dari semua aturan validasi yang ditentukan sebelumnya. Ketentuan ini bisa berasal dari kesesuaian tipe data field, apakah field wajib sudah terisi, dan juga aturan - aturan khusus yang sebelumnya disiapkan oleh pengembang. 

Tentu saja method ini sangat bermanfaat untuk memastikan kualitas data yang masuk ke database. Kita bisa mengembalikan kesalahan ke pengguna apabila ada kriteria input yang tidak dipenuhi. Hal ini dapat dicapai dengan mengirimkan pesan kesalahan ke pengguna. 

<h2>Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?</h2>
CSRF adalah singkatan dari (Cross-Site Request Forgery). CSRF adalah serangan yang mengeksploitasi kepercayaan yang dimiliki platform terhadap sebuah pengguna yang terautentikasi. Serangan ini umumnya memaksa pengguna secara diam - diam untuk mengirimkan HTPP request setelah mendapatkan cookies dari user. Sehingga, seolah - olah user lah yang melakukan HTTP request tersebut ketika pada kenyataannya, hal tersebut dilakukan oleh penyerang. Misalnya, kita sudah berhasil login ke sebuah situs, maka session cookie akan disimpan oleh browser. Misalnya kita menekan link dengan form tersembunyi, form tersebut bisa mendapatkan session cookie kita, walaupun di situs yang berbeda, dan akhirnya melakukan http requests yang tidak diinginkan, seperti mendelete account.

Fungsi dari csrf_token adalah untuk memastikan kalau http request yang dilakukan oleh user yang terautentikasi memang berasal dari si user, dan bukan penyerang. Dengan menggenerate token random pada form yang selalu dikirim bersamaan dalam permintaan post, django dapat memverifikasi apakah permintaan post tersebut valid atau tidak. Hal ini memastikan permintaan yang didapatkan valid dan memang dibuat oleh user.

<h2>Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</h2>

* Mengedit models.py.
  1. Menambahkan ID Ke ProductEntry di models.py dengan id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
  2. Lakukan Migrasi pada model
* Membuat input form untuk menambahkan objek model pada app sebelumnya
  1. Buat forms.py dan buat class turunan ModelForm yang memiliki fields yang sesuai dengan ProductEntry
  2. Buat fungsi create_product_entry di views.py. Fungsi tersebut akan menghandle request POST dari form. Nantinya data pada form akan disimpan. Fungsi ini juga dibuat untuk merender html form.
* Tambahkan data form ke main.html
  1. Tambahkan product entries dari models.py. Dapatkan semua object ProductEntry dan tambahkan ke context
* Tambahkan link form (fungsi create_product_entry) ke urls.py
* Buat template html entry form create product.
  1. Form menggunakan method post
  2. Tambahkan csrf_token
  3. Tambahkan button submit untuk menambahkan product entry
* Tampilkan data dan link form ke main.html
  1. Cek apakah sudah ada data, kalau belum ada, jangan tampilkan apa apa, kalau sudah ada, tampilkan seluruh field pada data untuk tiap objek (nama, price, description, produk_terjual, rating).
  2. Tambahkan link ke form penambahan entri produk
* Tambahkan fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON
  1. Buat fungsi show_xml untuk semua data. Gunakan serializers.serialize dengan format xml untuk mengubah jadi format xml
  2. Buat fungsi show_json untuk semua data. Gunakan serializers.serialize dengan format json untuk mengubah jadi format json
  3. Tambahkan path ke urls.py
* Tambahkan fungsi views baru untuk melihat objek dalam formatXML by ID, dan JSON by ID.
  1. Buat fungsi show_xml_by_id dengan parameter tambahan, yaitu id. Dapatkan data dengan method filter dan input id dari parameter. Gunakan serializers.serialize dengan format xml untuk mengubah jadi format xml
  2. Buat fungsi show_json_by_id dengan parameter tambahan, yaitu id. Dapatkan data dengan method filter dan input id dari parameter. Gunakan serializers.serialize dengan format json untuk mengubah jadi format xml
  3. Tambahkan path ke urls.py dengan path "xml/<str:id>/" atau "json/<str:id>/" untuk mendapatkan id dari link.










<h1>TUGAS 2</h1>
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