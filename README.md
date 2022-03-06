# LATIHAN4DPBO2022

Janji

>Saya Nelly Joy Christi Simanjuntak 2000199 mengerjakan Latihan 4 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin


#### Design Program
![alt text](https://github.com/joynelly/LATIHAN4DPBO2022/blob/main/img/ilustrasi.png?raw=true)

#### Penjelasan Desain
Saya membuat kelas Person (manusia) dan kelas Job (pekerjaan) menjadi base dari kelas Driver (Pengemudi) karena secara objek, Driver dan Person **merupakan** objek yang sama (seorang driver merupakan Person/Manusia, jadi memiliki **_is a_** relationship). Begitu juga dengan Driver dan Job yang secara objek **merupakan** objek yang sama (driver merupakan sebuah pekerjaan, jadi memiliki ***is a*** relationship). Person dan Driver tidak memiliki relationship karena secara objek bukan merupakan objek yang sama.

Driver dan Vehicle (kendaraan) memiliki hubungan composition dengan vehicle sebagai component dari driver. Hal ini saya simpulkan karena setiap Driver pasti **memiliki** Vehicle/kendaraan yang dikemudikan, oleh karena itu memiliki _**has a**_ relationship dengan driver sebagai kelas _composite_.

Ship dan Airplane menjadi inheritance dari kelas vehicle karena secara objek ship dan airplane **merupakan** sebuah kendaraan (memiliki _**is a**_ relationship). Atribut type dan age yang dimiliki oleh ship dan airplane dipindahkan ke kelas parent mereka yaitu vehicle karena kedua kelas ship dan airplane sama sama memiliki atribut tersebut.



#### Penjelasan Program
Program dibuat tidak dapat menerima inputan, oleh karena itu data yang ditampilkan merupakan data dummy.


#### Screenshoot Hasil Program
![alt text](https://github.com/joynelly/LATIHAN4DPBO2022/blob/main/python/python.png?raw=true)


Sekian latihan 4 yang telah saya kerjakan, mohon maaf apabila masih banyak kekurangan.
Terima kasih.
