ad=input("Adınız                                :")
soyad=input("Soyadınız                             :")
vize=float(input("Matematik Dersi vize notunuz(0-100)    :"))
final=float(input("Matematik Dersi final notunuz(0-100)  :"))
ders=float(input("Bu derse kaç kez devamsızlık yaptınız(0-20) :"))
ders_puan=100-int(ders*5)
puan=float(vize*30/100)+float(final*50/100)+float(ders_puan*20/100)
print("Tebrikler! Matematik Dersi için yıl sonu itibariyle ortalama",
      puan,"puan aldınız.")

