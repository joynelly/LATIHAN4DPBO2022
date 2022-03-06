from Job import Job
from Person import Person
from Vehicle import Vehicle
from Driver import Driver
from Airplane import Airplane
from Ship import Ship

print("\nLATIHAN 4 DPBO - MULTIPLE INHERITANCE")
print("=====================================\n")

# Data 1
print("=========================")
print("| Data 1 - Kelas Person |")
print("=========================")
# Membuat data pertama yang dideklarasikan dengan kelas Person
person1 = Person()
# Mengisi kelas Person
person1.setNIk("P1000000C122")
person1.setName("Spongebob Squarepants")
person1.setGender("Male")
# Menampilkan data pertama
person1.showPerson()
person1.sleep()


# Data 2
print("\n======================")
print("| Data 2 - Kelas Job |")
print("======================")
# Mendeklasrasikan data dengan kelas Job
job2 = Job()
# Mengisi Kelas Job
job2.setNIP("KK0001")
job2.setCompanyName("Krusty Krab")
job2.setPosition("Chef")
# Menampilkan data kedua
job2.showJob()


# Data 3
print("\n=========================")
print("| Data 2 - Kelas Driver |")
print("=========================")
# Mendeklasrasikan data dengan kelas Driver
driver3 = Driver()
# Mengisi kelas Driver
driver3.setName("Ms. Poppy Puff")
driver3.setNIk("P3000000C122")
driver3.setGender("Female")
driver3.setNIP("BD0001")
driver3.setCompanyName("Boating School Corp.")
driver3.setPosition("Driver")
driver3.setlicenseID("LID0001")
driver3.setactiveUntil("21-03-2025")
driver3.setvehicleType("Ship")
# Menampilkan data ketiga
driver3.showPerson()
driver3.showJob()
driver3.showDriver()
driver3.sleep()


# Data 4
print("\n==========================")
print("| Data 4 - Kelas Vehicle |")
print("==========================")
# Deklarasi data dengan kelas vehicle
vehicle4 = Vehicle()
vehicle4.settype("Airplane")
vehicle4.setfuelType("Gasoline")
vehicle4.setmaxPassanger(250)
vehicle4.setModel("AIRBUS A318")
vehicle4.setAge(8)
# Menampilkan data keempat
vehicle4.showVehicle()
vehicle4.move()


# Data 5
print("\n===========================")
print("| Data 5 - Kelas Airplane |")
print("===========================")
# Deklarasi data dengan kelas Airlane
airplane5 = Airplane()
airplane5.settype("Airplane")
airplane5.setfuelType("Biofuel")
airplane5.setmaxPassanger(300)
airplane5.setModel("BOEING 777F")
airplane5.setAge(12)
airplane5.setwingsLength(64.8)
airplane5.settailHeight(18.6)
airplane5.setmaxRange(4970)
airplane5.setairlines("Japan Airlines")
# Menampilkan data kelima
airplane5.showVehicle()
airplane5.showAirplane()
airplane5.move()


# Data 6
print("\n=======================")
print("| Data 6 - Kelas Ship |")
print("=======================")
# Deklarasi data dengan kelas Ship
ship6 = Ship()
ship6.settype("Ship")
ship6.setfuelType("Gas Oil")
ship6.setmaxPassanger(70)
ship6.setModel("NC-9072P")
ship6.setAge(25)
ship6.setcountryOfManufacture("USA")
ship6.setspeed(12)
ship6.setcruisingRange(6000)
ship6.setendurance(25)
# Menampilkan data keenam
ship6.showVehicle()
ship6.showShip()
ship6.move()


# Data 7
# Menampilkan data Lengkap
# Misalkan Driver 'driver3' dapat mengemudikan kendaraan 'ship6'
print("\n=========================")
print("| Data 7 - Data Lengkap |")
print("=========================")
driver3.showPerson()
driver3.showJob()
driver3.showDriver()
driver3.sleep()
print("\nVehicle Used")
ship6.showVehicle()
ship6.showShip()
ship6.move()