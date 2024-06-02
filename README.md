
# Tiktok Autocomplete
##  Analisis Perbandingan Algoritma Brute Force dengan Algoritma Knuth-Morris-Pratt dalam Penentuan Rekomendasi Pencarian Music pada Website Tiktok

Tugas Besar Mata Kuliah Strategi Algoritma

Anggota Kelompok:

- Afif Kurniawan Supriyadi - 1301223161
- Mukhlish Nur Hidhayat - 1301223028
- Reza Ilham Maulana - 1301223365

Pada tugas besar ini, kami membuat tampilan dan sebuah mesin pencari seperti yang ada pada website Tiktok. Website yang kami buat hanya terdiri dari satu page dan berfokus pada penerapan autocomplete pada mesin pencarian. 

Tampilan dan tata letak website dibuat semirip mungkin seperti pada tampilan homepage website Tiktok. Namun, tidak semua fungsionalitas dapat digunakan, hanya fitur kolom pencarian yang dapat berjalan pada website kami.

Fokus utama dalam tugas besar dan website kami adalah menerapkan algoritma KMP dan Brute Force sebagai metode yang digunakan dalam melakukan pencocokan kata dari string input (pattern) yang diketik oleh user pada string text dalam database. 

Karena dataset berupa data music, maka pengguna hanya dapat melakukan pencocokan kata dengan memasukkan nama music atau nama penyanyi tertentu. String input (pattern) yang dimasukkan pengguna pada kolom pencarian akan dicocokan dengan seluruh data dalam database, dan akan ditampilkan hasil autocomplete berupa daftar suggestion word atau rekomendasi pencarian nama music atau nama penyanyi yang dapat dipilih oleh user.

User dapat memilih text dari daftar autocomplete yang keluar untuk melihat konten music yang dipilih dan juga hasil perhitungan perbandingan pencocokan kata dari string input (pattern) dengan string text yang dipilih.  Konten music yang dipilih akan ditampilkan dan user dapat memutar music tersebut.  

Tampilan website:
![Tiktok Clone](https://github.com/afifksupriyadi/tubesSA-tiktok-autocomplete/assets/147795492/4d4ac705-c620-4dac-94b6-62a79f584daa)



##  Cara Menjalankan Website

1. Download semua file dan folder yang ada pada direktory github ini
2. Simpan dan buka direktory ini di vs code atau di teks editor lainnya
3. Menjalankan backend (file ./backend/app.py):
4. Buka terminal cmd baru dan arahkah ke folder backen (tuliskan "cd backend")
5. Tuliskan "python -m venv venv"
6. Tuliskan "venv\Scripts\activate" untuk mengaktifkan environment
7. Install library flask jika belum terunduh dalam komputer (tuliskan "pip install flask")
8. Jalankan app.py dengan menuliskan "python app.py"
9. Buka terminal baru (cmd/powershell) dan jalankan website dengan menuliskan "npm run server"
