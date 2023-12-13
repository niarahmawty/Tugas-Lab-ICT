def luas_persegipanjang(panjang,lebar):
        return panjang * lebar
panjang=int(input("Masukkan panjang :"))
lebar=int(input("Masukkan lebar :"))
print("\t\t\t\t")
print("luas persegi panjang : ",luas_persegipanjang(panjang, lebar))

def keliling_persegipanjang(panjang, lebar):
        return 2 * (panjang + lebar)
print("Keliling Persegi Panjang : ", keliling_persegipanjang(panjang, lebar))