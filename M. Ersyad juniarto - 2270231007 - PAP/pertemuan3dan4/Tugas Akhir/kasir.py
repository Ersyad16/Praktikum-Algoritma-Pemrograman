print("---------- Warung Makan Genuk Sadewo ----------")



pembeli = input("nama Pembeli          :")
alamat = input ("Alamat Pembeli        :")
hp= input      ("No.hp pembeli         :")
tanggal= input ("Tanggal beli          :")



def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print("\n----------------- Menu Makanan -----------------")
   print("1. Nasi Goreng - Rp 15000")
   print("2. Rawon - Rp 20000")
   print("3. Mie Ayam - Rp 11000")
   nomor=int(input("Masukan Pilihan: "))
   porsi=int(input("Berapa Porsi  : "))
   
   if nomor==1:
       totalmkn=porsi*15000
       print (porsi," porsi Nasi Goreng = Rp", totalmkn)
       mkn=("Nasi Goreng")
   elif nomor==2:
       totalmkn=porsi*9000
       print (porsi," porsi Rawon = Rp", totalmkn)
       mkn=("Rawon")
   elif nomor==3:
       totalmkn=porsi*11000
       print (porsi, " porsi Mie Ayam = Rp", totalmkn)
       mkn=("Mie Ayam")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Es teh - Rp 2000")
   print("2. Es jeruk - Rp 3500")
   print("3. kopi - Rp 4000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas  : "))

   if nomor==1:
       totalmnm=gelas*2000
       print (gelas," Es Teh = Rp", totalmnm)
       mnm=(" Gelas Es Teh")
   elif nomor==2:
       totalmnm=gelas*3500
       print (gelas, " Gelas Es Jeruk = Rp", totalmnm)
       mnm=("Es Jeruk")
   elif nomor==3:
       totalmnm=gelas*4000
       print (gelas, " Gelas Kopi = Rp", totalmnm)
       mnm=("Kopi")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar      : Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian                  :",kembalian)
print("\nTotal harus Dibayar      : Rp",totalsemua)
print("Kembalian                  :",kembalian)


print("========================================")
print("========== S T R U K   B E L I =========")
print("========================================")

print("Nama pembeli                  :",pembeli)
print("Alamat pembeli                :",alamat)
print("No.hp pembeli                 :",hp)
print("Tanggal beli                  :",tanggal)

print("Beli\t\t              :" ,porsi,mkn,"( Rp", totalmkn,")")
print("\t\t                ",gelas,mnm,"( Rp", totalmnm,")")
print("Tagihan\t\t              : Rp",totalsemua)
print("Dibayar\t\t              : Rp",uang)
print("Kembalian\t              : Rp",kembalian)
print("==================================")
print("==================================")