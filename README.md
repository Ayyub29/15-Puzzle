# 15 Puzzle


## Latar Belakang
Anda adalah Mr. Khun, saat ini Anda tergabung bersama tim Sweet & Sour untuk mencapai puncak menara. Agar dapat mencapai puncak menara, ada harus melalui serangkaian tes untuk dapat naik ke lantai selanjutnya. Saat ini Anda berada di lantai 18 dan administrator lantai tersebut, yaitu Mr. Le Leo ingin sekali menguji kecerdasan tim Anda dalam membuat strategi. Area permainan pada lantai ini dibagi menjadi 81 area, berbentuk seperti matriks berukuran 9x9. Setiap area ditandai dengan angka, dalam satu kolom maupun satu baris tidak boleh ada angka berulang (seperti pada permainan sudoku). Untuk lolos dari tes ini, tim Anda harus menyelesaikan sebuah puzzle berupa sliding puzzle

## Spesifikasi
Program menerima input 15-puzzle dalam bentuk txt dan menampilkan hasil urutan yang benar dalam terminal

## Requirements
1. Phyton 3.8 https://www.python.org/downloads/

## How to Use
1. Buka CMD dan pergi ke direktori anda menyimpan main.py
2. buka main.py dengan command : "py main.py"

## Strategi dan Kompleksitas Algoritma:

Strategi yang saya gunakan disini adalah algoritma branch and bound dengan pendekatan sederhana. Jadi dibentuk semua variasi yang mungkin dari puzzle (bisa geser ke kanan, kiri, atas dan bawah) dan dicari yang mana yang paling mendekati solusi dengan menghitung nilainya.
