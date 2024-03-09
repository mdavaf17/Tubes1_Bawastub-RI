# Tubes 1 Bawastub-RI
## Pemanfaatan Algoritma Greedy Dalam Pembuatan Bot Permainan Diamonds

## Strategi Greedy
1. Strategi ini memiliki prioritas pertama untuk melakukan tackle jika terdapat lawan yang berjarak 1 langkah. Apabila gagal melakukan tackle dalam sekali langkah, bot akan menonaktifkan prioritas ini untuk satu langkah selanjutnya. 
2. Jika poin diamond yang dibawa sama dengan 5, bot akan pulang ke base.
3. Dengan mempertimbangkan gerak jalan bot tiap satu kotak sekitar 1 detik, bot akan kembali ke base ketika waktu yang tersisa adalah jarak bot dengan base (dalam kotak) dikali dengan 1 detik ditambah dengan 1,75 detik sebagai waktu antisipasi berdasarkan beberapa percobaan yang telah dilakukan, jika waktu belum habis, tetapi bot sudah berada pada base maka bot akan melakukan gerakan random 1 langkah ke arah kanan, kiri, atas, ataupun bawah secara terus menerus hingga waktu habis. 
4. Jika jarak antara bot dengan tombol diamond adalah 1 kotak, maka bot akan menuju tombol dan menekan tombol tersebut, hal ini dilakukan karena berdasarkan beberapa percobaan yang dilakukan, dengan menekan tombol tersebut, bot bisa menghasilkan lebih banyak diamond.
5. Algoritma utama pada strategi ini adalah pembobotan poin diamond terhadap jarak diamond dari posisi bot, yaitu dengan mengecek seluruh diamond yang ada di papan pada saat itu dan melakukan pembobotan seluruhnya serta mencari diamond dengan bobot paling besar, lalu bot akan bergerak menuju diamond tersebut.


## Requirements
* [Node.js](https://nodejs.org/en) 
* [Docker desktop](https://www.docker.com/products/docker-desktop/)
* Yarn
* [Python](https://www.python.org/downloads/) 

## How To Setup
1. Buka dan ikuti panduan instalasi yang ada pada tautan [berikut](https://docs.google.com/document/d/1L92Axb89yIkom0b24D350Z1QAr8rujvHof7-kXRAp7c/edit)
2. Lakukan clone pada link repository ini [here](https://github.com/mdavaf17/Tubes1_Bawastub-RI/edit/main/README.md)
3. Pindah src
```
cd src
```
5. Install dependencies dengan
```
pip install -r requirements.txt
```
6. Jalankan program

   a. Single bot ```python main.py --logic Random --email=your_email@example.com --name=your_name --password=your_password --team etimo```

   b. Multiple bot dengan ```./run-bots.bat``` untuk Windows atau ```./run-bots.sh``` untuk Linux/macOS

## Author 

### Group 35 | Bawastub

1. 13522072	Ahmad Mudabbir Arif
2. 13522092	Sa'ad Abdul Hakim
3. 13522114	Muhammad Dava Fathurrahman
