# class Mobil:
#     def __init__(self, warna, merek, kecepatan):
#         self.warna = warna
#         self.merek = merek
#         self.kecepatan = kecepatan
        
# mobil_1 = Mobil('Biru', 'Ducatti', 300)

# print(mobil_1.warna)
# print(mobil_1.merek)
# print(mobil_1.kecepatan)

# 1. Buatlah class bernama Animal dengan ketentuan:
#     - Memiliki properti:
#       - name: string
#       - age: int
#       - species: string
#     - Memiliki constructor untuk menginisialisasi properti:
#       - name
#       - age
#       - species
# 2. Buatlah class bernama Cat dengan ketentuan:
#     - Merupakan turunan dari class Animal
#     - Memiliki method:
#       - bernama "deskripsi" yang mengembalikan nilai string berikut ini.
#         "{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
#       - bernama "suara" yang akan mengembalikan nilai string "meow!"
#  3. Buatlah instance dari kelas Cat bernama "myCat" dengan ketentuan:
#     - Atribut name bernilai: "Neko"
#     - Atribut age bernilai: 3
#     - Atribut species bernilai: "Persian".

class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        
class Cat(Animal):

    def deskripsi(self):

        self.deskripsi = f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun "
        
        return self.deskripsi
    
    def suara(self):

        self.suara = "meow!"

        return self.suara

myCat = Cat("Neko",3,"Persian")

print(myCat.deskripsi())
print(myCat.suara())
        
        
# x = [1, 2.2, 'Dicoding']
# x[0] = 'Indonesia'
# print(x)

# x = (5, 'program', 1+3j)
# x[1] = 'Dicoding'
# print(x)

# x = True 
# y = False
# print(x or y)

x = { 'name': 'Coding', 'age': 20, 'isMarried': False }
x ['name'] = "Dicoding"
print(x)

print(dict([['name','Dicoding'],['age',17]]))

x = 1960 
y = 901 
print(x % y) 