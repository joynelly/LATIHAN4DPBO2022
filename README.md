# LATIHAN4DPBO2022

Janji

>Saya Nelly Joy Christi Simanjuntak 2000199 mengerjakan Latihan 4 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin


#### Design Program
![alt text](https://github.com/joynelly/LATIHAN4DPBO2022/blob/main/img/ilustrasi_design.png?raw=true)

#### Penjelasan Desain
Saya membuat kelas Person (manusia) dan kelas Job (pekerjaan) menjadi base dari kelas Driver (Pengemudi) karena secara objek, Driver dan Person **merupakan** objek yang sama (seorang driver merupakan Person/Manusia, jadi memiliki **_is a_** relationship). Begitu juga dengan Driver dan Job yang secara objek **merupakan** objek yang sama (driver merupakan sebuah pekerjaan, jadi memiliki ***is a*** relationship). Person dan Driver tidak memiliki relationship karena secara objek bukan merupakan objek yang sama.

Kelas Driver dan Vehicle (kendaraan) tidak memiliki hubungan. Hal ini saya simpulkan karena walupun kelas Driver memiliki atribut vehicleType yang menandakan dapat memiliki hubungan composition dengan vehicle, tetapi terdapat kemungkinan bahwa sebuah kendaraan tidak hanya dikemudikan satu driver begitu juga dengan driver yang dapat mengemudikan lebih dari satu kendaraan (jenis tetap sama).

Ship dan Airplane menjadi inheritance dari kelas vehicle karena secara objek ship dan airplane **merupakan** sebuah kendaraan (memiliki _**is a**_ relationship). Atribut type dan age yang dimiliki oleh ship dan airplane dipindahkan ke kelas parent mereka yaitu vehicle karena kedua kelas ship dan airplane sama sama memiliki atribut tersebut.



#### Penjelasan Program
Program dibuat tidak dapat menerima inputan, oleh karena itu data yang ditampilkan merupakan data dummy.
Program akan menampilkan bebrapa contoh data, dimana setiap datanya merupakan hasil data yang dideklasrasikan melalui berbagai kelas.
Terdapat 7 jenis data yang ditampilkan, yaitu:
  1. Data yang dideklarasikan dengan kelas Person (hanya memiliki atribut kelasnya)
  2. Data yang dideklarasikan dengan kelas Job (hanya memiliki atribut dari kelasnya)
  3. Data yang dideklarasikan dengan kelas Driver (memiliki atribut dari kelas Person dan Job)
  4. Data yang dideklarasikan dengan kelas Vehicle (hanya memiliki atribut kelasnya)
  5. Data yang dideklasrasikan dengan kelas Ship (memiliki atribut kelas vehicle juga)
  6. Data yang dideklasrasikan dengan kelas Airplane (memiliki atribut kelas vehicle juga)
  7. Data lengkap dimana terdapat kelas driver yang memiliki vehicle (ship/Airplane)



#### Screenshoot Hasil Program
![alt text](https://github.com/joynelly/LATIHAN4DPBO2022/blob/main/img/python1.png?raw=true)
![alt text](https://github.com/joynelly/LATIHAN4DPBO2022/blob/main/img/python2.png?raw=true)
![alt text](https://github.com/joynelly/LATIHAN4DPBO2022/blob/main/img/python3.png?raw=true)


Sekian latihan 4 yang telah saya kerjakan, mohon maaf apabila masih banyak kekurangan.
Terima kasih.
