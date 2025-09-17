1. -data delivery berfungsi sebagai perantara antara backend dan pengguna aplikasi untuk bertukar informasi.
- membuat kegiatan kegiatan realtime seperti autentikasi data, pembayaran dan lain lain dapat terjadi
2. menurut saya pribadi JSON lebih baik dibandingkan dengan XML karena JSON menyajikan data dengan lebih mudah dibaca oleh mata manusia dan lebih mudah diintegrasikan dengan REST API karena itu juga JSON lebih populer dibanding XML
3. tujuan utama dari is_valid() adalah memvalidasi apakah input yang diberikan user sudah sesuai dengan apa yang kita inginkan atau belum. Jika belum sesuai, user tidak akan bisa mensubmit sampai format data sudah sesuai. jika tidak ada is_field(), data yang di input user bisa salah penempatan, contohnya nama : 240183021
4. csrf_token merupakan semacam bantuan dari django itu sendiri untuk melindungi kita dari serangan siber. django akan memberikan token rahasia sehingga penyerang server tidak dapat mengakses request palsu. jika kita tidak menggunakan csrf_token maka penyerang server dapat mengakses request palsu tanpa kita ketahui. request palsu tersebut dapat dimanfaatkan oleh penyerang server untuk keuntungan mereka, seperti meminta transfer atau mengganti password akun.
5. -menambahkan 4 fungsi baru di views.py yang berfungsi untuk melihat data (XML, JSON, XML by ID, dan JSON by ID.)
-membuat path untuk keempat fungsi di atas
-mengimport product dari models
-menambahkan fungsi add_product dan show_product di views.py
-membuat file add_product dan product details di main/templates, dengan template yang sama seperti tutorial namun diubah sesuai dengan keperluan
-mengubah kategori produk menjadi sepatu futsal dan sepatu bola saja
-membuat file forms.py
-membuat product_list
- -Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form dan tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek. 
6. tidak ada, penjelasan di website sudah jelas dan asdos sangat baik

link foto foto
https://drive.google.com/drive/folders/1mqS_vofyV4m3PabJ6P1guv_T6uYWN8Fx?usp=drive_link
  

