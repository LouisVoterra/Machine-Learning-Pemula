# # def luas_persegi(p,l):
# #     luas = p * l
# #     return luas

# # def kerucut(a,l,t):
# #     luas = 1/3 * a * l * t
# #     return luas

# # x = int(input("Masukkan nilai panjang : "))
# # y = int(input("Masukkan nilai lebar : "))

# # print(luas_persegi(5,3))

# # 10
# # a = int(input("Masukkan nilai alas : "))
# # l = int(input("Masukkan nilai lebar : "))
# # t = int(input("Masukkan nilai tinggi : "))


# # print("Luas Kerucut dari Alas = " + str(a) + " lebar = " + str(l) + " dan tinggi = " + str(t) + " adalah = " + str(kerucut(a,l,t)))

# import hello

# persegi_panjang = hello.mencari_luas_persegi_panjang(5,10)
# print(persegi_panjang)


class Mobil:
    # Atribut Instance
    def __init__(self):
        self.warna = 'Merah'
        
mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)
print(mobil_2.warna)

# Mengubah atribut instance
mobil_1.warna = "Hitam"

# Menampilkan kembali atribut warna
print(mobil_1.warna)
print(mobil_2.warna)

#ternyata, dikasi constructor dl, supaya Class.Attribute jadi useless wpoakowkokw

