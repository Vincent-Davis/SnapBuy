<h1>TUGAS 6</h1>
<h2>Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!</h2>
  1. Interaktivitas dan Responsivitas: JavaScript memungkinkan pengembangan aplikasi web yang interaktif dan responsif. Dengan JavaScript, halaman web dapat bereaksi terhadap tindakan pengguna seperti klik, input, atau gerakan mouse tanpa perlu memuat ulang halaman. Ini menciptakan pengalaman yang lebih dinamis dan menarik, misalnya, dropdown menu, carousel, atau validasi formulir real-time.

  2.Framework dan Library yang Mendukung: JavaScript memiliki ekosistem framework dan library yang luas, seperti React, Vue.js, dan Angular, yang sangat membantu dalam pengembangan aplikasi web modern. Dengan framework ini, pengembang dapat membangun antarmuka pengguna yang kompleks, mengelola state aplikasi dengan mudah, dan menciptakan komponen yang dapat digunakan kembali, mempercepat proses pengembangan.

  3.Pemrograman Asinkron: JavaScript mendukung pemrograman asinkron melalui fitur seperti AJAX dan fetch API, yang memungkinkan aplikasi web mengambil data dari server tanpa harus memuat ulang halaman. Ini meningkatkan performa aplikasi, terutama untuk aplikasi yang memerlukan data real-time, seperti media sosial atau aplikasi peta, yang memberikan pengalaman pengguna yang lebih mulus.

<h2>Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?</h2>
Fungsi dari penggunaan await saat menggunakan fetch() adalah untuk menunggu hasil dari operasi asynchronous (dalam hal ini, permintaan HTTP menggunakan fetch()) sebelum melanjutkan eksekusi kode. Saat kita menggunakan await, JavaScript akan menghentikan sementara eksekusi kode di baris tersebut sampai permintaan fetch() selesai dan data respons sudah diterima, lalu mengembalikan hasilnya untuk diproses lebih lanjut.

Jika await tidak digunakan, getProductEntries() akan mengembalikan Promise yang belum selesai, sehingga variabel productEntries berisi Promise alih-alih data produk. Hal ini menyebabkan kegagalan ketika mencoba melakukan iterasi dengan forEach(), karena Promise tidak bisa diiterasi. Akibatnya, UI tidak akan diperbarui dengan benar, dan elemen DOM tidak akan menampilkan data produk seperti yang diharapkan.

<h2>Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?</h2>

Kita perlu menggunakan decorator @csrf_exempt pada view yang akan digunakan untuk AJAX POST request jika kita ingin menonaktifkan perlindungan CSRF (Cross-Site Request Forgery) untuk view tersebut. Secara default, Django menerapkan mekanisme perlindungan CSRF untuk semua permintaan POST yang berasal dari halaman web, yang memastikan bahwa setiap permintaan POST diautentikasi dan dikirim dari sumber yang sah.

Namun, pada kasus AJAX POST request, terutama jika request tidak menyertakan CSRF token yang tepat (yang biasanya dihasilkan dan disisipkan oleh Django dalam formulir HTML), maka request tersebut akan dianggap berbahaya dan diblokir. Dengan menambahkan @csrf_exempt, kita menonaktifkan pemeriksaan CSRF hanya untuk view add_product_entry_ajax, sehingga AJAX POST request dapat diproses tanpa kendala.

<h2>Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?</h2>

1. Keamanan

Pembersihan data di backend sangat penting terutama dari sisi keamanan. Meskipun validasi di frontend dapat membantu memberikan umpan balik cepat kepada pengguna, itu tidak bisa diandalkan sepenuhnya karena mudah dilewati. Pengguna atau penyerang yang mematikan JavaScript atau memanipulasi form HTML di browser bisa mengirim data yang tidak valid atau bahkan berbahaya langsung ke server. Ini bisa membuka celah bagi serangan seperti SQL injection, Cross-Site Scripting (XSS), dan eksploitasi lainnya yang memanfaatkan input tidak aman. Backend, yang mengontrol seluruh komunikasi dan data yang masuk ke server, harus memastikan bahwa semua input sudah dibersihkan dengan benar untuk mencegah serangan semacam ini, menjaga keamanan aplikasi dan data yang disimpannya.

2. Konsistensi

Selain itu, pembersihan di backend memastikan konsistensi dalam penanganan data. Aplikasi web bisa menerima data dari berbagai sumber selain browser, seperti aplikasi mobile, API, atau integrasi dengan layanan lain. Jika validasi dan pembersihan hanya dilakukan di frontend, kita tidak bisa menjamin bahwa semua sumber tersebut akan mengimplementasikan logika validasi yang sama. Dengan melakukan pembersihan di backend, kita dapat memastikan bahwa semua data yang masuk diperlakukan dengan standar yang sama terlepas dari sumbernya, sehingga aplikasi lebih andal dan mudah dipelihara. Logika validasi dan pembersihan terpusat di backend juga mencegah duplikasi dan inkonsistensi, menjaga efisiensi dalam pengelolaan data aplikasi.

<h2>Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!</h2>

1. AJAX GET
  * Ubahlah kode cards data product agar dapat mendukung AJAX GET.
      * Menghapus fungsi mendapatkan entri product dari show_main pada views.py
      * Ganti fungsi show_json dan show_xml dengan menambahkan ProductEntry.objects.filter(user=request.user), sehingga data difilter sesuai user yang sesuai (tidak bisa melihat data user lain)   
  * Lakukan pengambilan data mood menggunakan AJAX GET. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in.
      * Membuat fungsi javascript untuk mendapatkan entri produk dengan menggunakan fungsi views json yang sudah dibuat sebelumnya return fetch("{% url 'main:show_json' %}").then((res) => res.json())
      * Membuat fungsi javascript untuk merefresh entri mood.
        * Bila data kosong, maka yang ditampilkan adalah gambar sedih menunjukan kalau belum ada data
        * Bila data sudah ada, maka tampilkan data menggunakan desain kartu pada tugas sebelumnya. Gunakan productEntries.forEach((item) => { html+=' ... untuk melakukan for loop di tiap entri mood.
      * Panggil fungsi untuk merefresh entri produk agar ditampilkan saat user masuk ke web
    
2. AJAX POST
  * Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan mood.
      * Menambah tombol dengan menggunakan tag button dengan atribut onclick yang akan memanggil fungsi showModal (fungsi untuk menampilkan form)
  * Buatlah fungsi view baru untuk menambahkan mood baru ke dalam basis data.
      * Tambahkan kode form untuk form ajax di bawah div dengan id product_entry_cards
      * Form disembunyikan
      * Buat fungsi showModal yang menampilkan form ajax, dengan membuang classlist yang hidden
      * Buat fungsi hideModal yang menyembunyikan form ajax dengan menambahkan classlist yang hiden
  * Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.
      * Menambahkan fungsi add_product_entry_ajax pada views.py. Fungsi tersebut membuat instance ProductEntry yang baru dan menyimpannya
      * Tambahkan dekorator csrf_exempt yang membuat Django tidak perlu mengecek keberadaan csrf_token pada POST request yang dikirimkan ke fungsi ini.
      * Tambahkan juga dekorator require_POST membuat fungsi tersebut hanya bisa diakses ketika pengguna mengirimkan POST
      * Tambahkan ke urls.py
  * Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.
      * Buatlah fungsi javascript addProductEntry yang mengirimkan data form menggunakan metode POST via AJAX ke URL yang ditentukan, lalu setelah berhasil, memanggil fungsi refreshMoodEntries() untuk memperbarui daftar entri mood. Setelah pengiriman, form di-reset dan modal ditutup dengan klik otomatis pada elemen yang terkait dengan modal.
      * Tambahkan event listener pada di modal form untuk menjalankan fungsi addProductEntry()
  * Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar mood terbaru tanpa reload halaman utama secara keseluruhan.
      * Panggil fungsi refreshProductEntries saat page di load dan saat fungsi addProductEntry dilakukan  

<h1>TUGAS 5</h1>

  <h2>Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!</h2>
  
  Ini adalah Jawaban yang terurut dari paling penting :
    
  1. Origin & Importance 
    
  Origin : 
  * Author: CSS yang dibuat oleh pengembang front-end, yaitu stylesheet yang ditulis dalam proyek atau aplikasi.
  * User: Pengguna browser dapat mengatur gaya secara manual di pengaturan browser mereka, seperti mengatur font dan warna.
  * User-Agent: Browser memiliki gaya default yang diterapkan pada elemen HTML. Setiap browser mungkin memiliki gaya default yang berbeda.

  Importance : Deklarasi CSS dapat diprioritaskan dengan menggunakan !important.
    
    contoh : 
          h1 {
      color: blue !important;
    }
  Aturan ini akan mengesampingkan semua aturan lain yang mengatur warna teks elemen h1.
  
  2. Selector Specificity

     1. Inline styles: Gaya yang ditulis langsung di elemen HTML.
  
      Contoh: h1 style="color: red;" akan mengesampingkan semua gaya lain yang ditulis di file CSS.
     
     2. ID selectors: Selector yang menggunakan ID.
  
      Contoh: #title1 { color: aqua; } akan memiliki prioritas lebih tinggi daripada class atau tag selector.
     
     3. Class selectors: Selector yang menggunakan class.
  
      Contoh: .class1 { color: cadetblue; }.
     
     4. Element selectors: Selector berdasarkan tag HTML.

      Contoh: h1 { color: blue; } akan mengatur semua elemen h1.
    
  3. Source Order

Ketika ada beberapa file CSS atau aturan CSS dalam satu file HTML, aturan yang muncul paling akhir akan mengesampingkan aturan yang sebelumnya, jika kedua aturan memiliki spesifisitas yang sama.
  5. Initial & Inherited Properties

Initial Properties: Setiap elemen HTML memiliki nilai default untuk properti tertentu jika tidak ada gaya yang diterapkan. Nilai awal ini bergantung pada properti yang digunakan.

Inherited Properties: Gaya CSS dari elemen parent akan diturunkan ke elemen anak, kecuali jika elemen anak memiliki gaya khusus yang diterapkan padanya.

  <h2>Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!</h2>

  1. Penggunaan Perangkat yang Beragam
     
     * Pengguna saat ini mengakses aplikasi web dari berbagai perangkat, termasuk desktop, laptop, tablet, dan smartphone. Setiap perangkat memiliki ukuran layar yang berbeda, sehingga aplikasi web harus dapat menyesuaikan tampilannya agar tetap mudah digunakan dan terlihat baik di semua perangkat.
    
     * Responsive design memungkinkan aplikasi web untuk menyesuaikan tata letak, ukuran teks, gambar, dan elemen interaktif sesuai dengan ukuran layar perangkat. Hal ini penting untuk memberikan pengalaman pengguna (user experience) yang konsisten dan menyenangkan, baik di layar besar maupun kecil.
  
  3. Efisiensi Pengembangan

     * Dengan menerapkan responsive design, pengembang hanya perlu mengembangkan satu situs web yang dapat bekerja di berbagai perangkat. Hal ini mengurangi biaya dan waktu yang diperlukan untuk membuat versi terpisah untuk desktop dan mobile.

  Yang sudah menerapkan : 
     
  * Twitter
      
Twitter menggunakan responsive design yang sangat baik. Saat diakses dari perangkat mobile, tata letaknya berubah menjadi vertikal dengan navigasi yang lebih mudah dijangkau, dan gambar serta video menyesuaikan ukuran layar tanpa kehilangan kualitas. Menu navigasi berubah menjadi ikon-ikon yang lebih ringkas, dan kolom teks memiliki ukuran yang optimal untuk dibaca tanpa perlu memperbesar layar.
  
  Yang belum menerapkan : 
      
  * Siasisten

Web Siasisten cs ui masih harus melakukan scroll horizontal di handphone. Teks masih terlalu kecil bila dibaca dari handphone. Tidak hanya itu, tombol tombol yang ada juga terlalu kecil, sehingga user harus melakukan zoom dan scrolling horizontal secara berlebihan

  <h2>Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!</h2>
  1. Margin 
    
Margin adalah ruang kosong di luar elemen, yang memisahkan elemen tersebut dari elemen lainnya di sekitarnya. Margin tidak memiliki warna atau isi, hanya berfungsi sebagai jarak antar elemen di halaman web.

  2. Border 
    
Border adalah garis yang mengelilingi elemen, yang berada di antara margin dan padding. Border memberikan batas visual yang jelas untuk elemen dan bisa diberi warna, ketebalan, dan gaya yang berbeda (misalnya solid, dashed, dotted).
  3.Padding 

Padding adalah ruang kosong di dalam elemen, yang memisahkan konten elemen dari border elemen tersebut. Padding menambah ruang di dalam elemen dan sering digunakan untuk memberikan jarak antara teks atau gambar dengan batas elemen.

    Untuk lebih jelasnya, kita dapat mengacu pada sketsa ini : 

            +-----------------------------------------------------+
            |                      Margin                         |
            |  +-----------------------------------------------+  |
            |  |                   Border                      |  |
            |  |  +-----------------------------------------+  |  |
            |  |  |                 Padding                 |  |  |
            |  |  |  +-------------------------------+      |  |  |
            |  |  |  |           Content             |      |  |  |
            |  |  |  +-------------------------------+      |  |  |
            |  |  +-----------------------------------------+  |  |
            |  +-----------------------------------------------+  |
            +-----------------------------------------------------+

  <h2>Jelaskan konsep flex box dan grid layout beserta kegunaannya!</h2>
    1. Flexbox
  
  Flexbox adalah sistem layout satu dimensi yang dirancang untuk mengelola tata letak di satu baris (horizontal) atau satu kolom (vertikal). Flexbox digunakan untuk mengontrol tata letak elemen secara fleksibel dalam satu arah (row atau column).
  Flexbox memudahkan pengaturan elemen-elemen secara responsif, seperti mendistribusikan ruang antara item, mengatur alignment, dan memperbesar atau memperkecil item sesuai dengan ruang yang tersedia.
    
  Properti Utama Flexbox:
  
  * display: flex: Menjadikan kontainer sebagai flex container, sehingga anak-anaknya menjadi flex items yang diatur oleh sistem flexbox.
  * flex-direction: Menentukan arah layout dari item (baris atau kolom).
  Contoh: flex-direction: row; (baris) atau flex-direction: column; (kolom).
  * justify-content: Mengatur bagaimana item-item didistribusikan di sepanjang sumbu utama (main axis).
  Contoh: justify-content: space-between; (mendistribusikan item dengan jarak yang sama).
  * align-items: Mengatur alignment item di sepanjang sumbu sekunder (cross axis).
  Contoh: align-items: center; (menempatkan item-item di tengah secara vertikal).
  * flex-wrap: Memungkinkan elemen untuk membungkus ke baris berikutnya ketika ruang habis (berfungsi untuk layout responsif).

  2. Grid Layout

      Grid Layout adalah sistem layout dua dimensi yang digunakan untuk mengatur elemen-elemen pada baris (row) dan kolom (column). Grid memungkinkan kamu untuk membuat tata letak yang lebih kompleks dibandingkan Flexbox, karena ia dapat mengatur elemen secara dua dimensi (baik dalam baris maupun kolom secara bersamaan).

      Properti Utama Grid Layout:
     
      * display: grid: Menjadikan kontainer sebagai grid container.
      * grid-template-columns dan grid-template-rows: Mengatur jumlah dan ukuran kolom serta baris.
      Contoh: grid-template-columns: 1fr 2fr; (kolom pertama menggunakan 1 bagian, kolom kedua 2 bagian).
      * grid-gap atau gap: Menentukan jarak antara baris dan kolom.
      Contoh: gap: 20px; (jarak antar elemen dalam grid).
      * grid-column dan grid-row: Menentukan seberapa banyak elemen membentang ke kolom atau baris.
      Contoh: grid-column: span 2; (membentang ke dua kolom).


  <h2>Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!</h2>
  
  1. Menambahkan tailwind

      * Menambahkan tag meta name = viewport agar dapat menyesuaikan dengan perilaku perangkat mobile
      * Tambahkan script CDN tailwind di bagian head base.html
    
  2. Menambahkan Fitur Edit Product
     
      * Buat fungsi edit_product di views.py yang mempunyai form yang sudah di pre-fill dengan menggunakan line form = ProductEntryForm(request.POST or None, instance=product), dengan product adalah product yg difilter berdasarkan id nya.
      * Buat template edit_product.html yang berisi form
      * Tambahkan ke urls.py
      * Tambahkan button edit product di main.html
  3. Menambahkan fitur Hapus Product
     
      * Buat fungsi delete_product di views.py yang menghapus product dengan product.delete() dan redirect ke halaman main
      * Tambahkan ke urls.py
      * Tambahkan button delete product di main.html
  4. Menambahkan Navigation Bar
       
      * Membuat file template navigation bar 
      * Pada file template tersebut, tambahkan menu - menu untuk navbar yaitu "Home", "Products", "Categories", dan "Cart".
      * Bila pengguna sudah login, tambahkan tombol logout
      * Membuat 2 design, yaitu design untuk desktop dan mobile
      * Tambahkan navbar ke semua halaman web (kecuali login)
      
  6. Mengkustomisasi halaman login, register, tambah product, dan halaman lainnya
     
      * Menggunakan template dari tailwind untuk membuat website yang baik
      * Membuat card baru dengan desain yang beda
      * Menambahkan atribut produk yang sesuai ke card pada main.html
      * Menambah button untuk edit dan menghapus card

  
<h1>TUGAS 4</h1>
 <h2>1. Apa perbedaan antara HttpResponseRedirect() dan redirect()</h2>
  
  * HttpResponseRedirect
  Merupakan kelas bawaan Django yang membuat respon redirect ke url yang diberikan di parameter. Keunggulan menggunakan HttpResponseRedirect adalah kita dapat memanipulasi object response yang dibuat. Misalnya, dalam hal cookie, menggunakan HttpResponseRedirect bisa lebih menguntungkan, karena kita bisa menggunakan response.set_cookie atau response.delete_cookie untuk memanipulasi cookie. Hal ini tidak bisa dilakukan bila kita menggunakan redirect
  * Redirect
  Merupakan fungsi shortcut django yang sebenarnya juga menggunakan HttpResponseRedirect tapi lebih mudah ditunakan karena dapat menerima input URL, nama view, atau objek model. Fungsi ini bisa secara otomatis menangani konversi ke url yang tepat. Namun kekurangannya adalah objek response tidak bisa dimanipulasi

 <h2>2. Jelaskan cara kerja penghubungan model Product dengan User!</h2>
  
  pada model product, user dihubungkan dengan menggunakan foreign key. Hal ini terlihat dari user = models.ForeignKey(User, on_delete=models.CASCADE). Parameter on_delete yang diset ke cascade memastikan agar datanya dihapus juga saat user dihapus. 
  
  User disimpan pada saat request post dilakukan. Terlihat dari kode ini : 

            if form.is_valid() and request.method == "POST":
              product_entry = form.save(commit=False)
              product_entry.user = request.user
              product_entry.save()
              
  Terlihat kalau data user didapatkan bukan dari input form, melainkan melalui atribut user dari parameter request.

  Setelah itu, dilakukan juga filter data berdasarkan user. 
  product_entries = ProductEntry.objects.filter(user=request.user)
  Oleh karena itu, data forms yang nantinya terlihat seharusnya hanya mengandung data yang dibuat user.


 <h2>3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.</h2>
 
  * Authentication
  Autentikasi adalah proses verifikasi identitas pengguna, di mana sistem memeriksa apakah pengguna yang mencoba masuk adalah pengguna yang sah dengan memvalidasi kredensial seperti username dan password. Proses ini memastikan bahwa hanya pengguna yang terdaftar dan memiliki izin yang tepat dapat mengakses sistem.
  * Authorization
  Authorisasi adalah proses yang menentukan hak atau izin pengguna yang telah diautentikasi untuk mengakses sumber daya atau melakukan tindakan tertentu dalam sistem. Setelah pengguna berhasil diautentikasi, otorisasi menentukan apa yang boleh dan tidak boleh dilakukan oleh pengguna tersebut, berdasarkan peran atau izin yang diberikan kepada mereka.

  Saat pengguna login, umumnya proses autentikasi dilakukan dengan memeriksa apakah username dan passowrdnya sesuai. Bila user terautentikasi, maka django akan mengirim cookie session ke browser pengguna. Cookie ini memungkinkan server untuk mengenali user pada request request berikutnya. Proses autenthication berada pada bagian - bagian platform yang tidak dapat diakses apabila pengguna belum login. Hal ini dilakukan dengan menggunakan decorator @login_required(login_url='/login').

 <h2>4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?</h2>

 Django mengingat pengguna yang telah login dengan menggunakan cookies yang disimpan di browser pengguna. Ketika pengguna berhasil login, Django membuat sesi khusus untuk mereka dan menyimpan session ID di cookie. Setiap kali pengguna mengirimkan permintaan HTTP (misalnya, membuka halaman lain di situs), browser mengirimkan cookie ini bersama dengan permintaan tersebut, sehingga server Django dapat mencocokkan session ID dari cookie dengan sesi pengguna yang tersimpan di server.
 
 Selain itu, beberapa kegunaan cookie adalah :
  1. Menyimpan Otentikasi
  Dengan cookies, situs dapat mempertahankan sesi login pengguna bahkan setelah mereka menutup browser 
  2. Analitik dan Pelacakan
  Cookies sering digunakan oleh layanan analitik untuk melacak perilaku pengguna di situs web
  3. Pengiklanan dan preferensi
  Cookies dapat menyimpan pengaturan preferensi pengguna seperti bahasa, tema, atau item dalam keranjang belanja, sehingga pengalaman pengguna dapat dipersonalisasi. Cookies juga digunakan oleh platform iklan untuk melacak kebiasaan browsing pengguna, sehingga dapat menampilkan iklan yang relevan dengan minat pengguna.

  Namun, tidak semua cookies aman digunakan : 
  1. Situs tanpa HTTPS
  Cookies yang dikirim melalui koneksi HTTP yang tidak terenkripsi dapat diambil oleh pihak ketiga yang mengintercept data.
  2. Cross-Site Request Forgery (CSRF)
  Penyerang dapat mengirim permintaan berbahaya yang tampak sah dengan memanfaatkan cookies sesi pengguna yang sudah login. 
  3. Session Hijacking
  Jika cookies yang menyimpan session ID tidak dilindungi dengan benar (misalnya, tanpa enkripsi), penyerang dapat mencuri cookie tersebut melalui serangan man-in-the-middle atau melalui cross-site scripting (XSS).
 
 <h2>5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</h2>
 
  1. Membuat form registrasi

    * Import UsercreationForm di views.py
    * Tambahkan fungsi di views.py(register) yang menampilkan form. Kali ini, form merupakan instance dari UsercreationForm. 
    * Buat penanganan request POST (request pembuatan akun) dengan menyimpan data dan me redirect ke main page.
    * Buat template untuk form registrasi yang berisikan form dengan csrf token.
    * Render template dengan context berisikan form tersebut.
    * Tambahkan fungsi register ke urls.py
  2. Membuat Fungsi Login

    * Buat fungsi baru di views.py (login_user) yang berfungsi untuk melakukan autentikasi kepada user yang login
    * Buatlah instance dari AuthenticationForm
    * Bila tidak ada request POST maka kembalikan render template dengan context berisikan authentication form tersebut
    * Bila ada request POST, maka ambil data dan dapatkan user. Bila berhasil di autentikasi, maka panggil method login (bawaan django) dan redirect ke main page.
    * Buat template login yang menampilkan form dengan csrf token. Tambahkan juga link yang mengalihkan ke register page.
    * Tambahkan fungsi ke urls.py
  3. Membuat Fungsi Logout

    * Import fungsi logout dari django di views.py
    * Buat function (logout) yang memanggil method tersebut, lalu me re-direct ke login page.
    * Tambahkan link yang memanggil function ini di bagian bawah main.html
    * Tambahkan ke urls.py
  4. Merestriksi halaman lain bila belum login

    * Import login_required ke views.py
    * Tambahkan decorator login_required ke fungsi show_main
  5. Menggunakan data Cookie

    * Import datetime, HttpResponseRedirect, dan Reverse
    * Pada fungsi login_user tambahkan cookie last_login. Hal ini dilakukan dengan memanfaatkan HttpResponseRedirect dan fungsi set_cookie.
    * Tambahkan context last_login pada context show_main yang isinya merupakan request.COOKIES['last_login']
    * Menggunakan HttpResponseRedirectdan fungsi delete_cookie, hapus cookie di logout_user.
    * Tambahkan keterangan kapan terakhir login di main.html
  6. Menghubungkan ProductEntry degnan User

    * Tambahkan User ke product entry dengan menggunakan models.ForeinKey
    * Buka views.py dan pada function create_product_entry, simpan data user dengan mendapatkan data user menggunakan request.user
          product_entry = form.save(commit=False)
          product_entry.user = request.user
    * Menampilkan nama username (diganti dari nama pembuat ke nama username) pada fungsi show_main dengan mengganti context dengan request.user.username
    * lakukan model migration


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