Anapara=int(input("Yatırmak istediginiz toplam tutar(Anapara) :"))
Faiz_suresi=int(input("Faizde kalmasını istediginiz sure(Faiz suresi-yıl) :"))
Faiz_orani=float(input("Kullanmak istediginiz faiz oranını belirtiniz(Faiz oranı) :"))
Faiz_tutari=Anapara*Faiz_suresi*Faiz_orani/100
Faiz_aylik=Faiz_tutari/(Faiz_suresi*12)
Faiz_gunluk=Faiz_tutari/(Faiz_suresi*360)
print(Anapara,"euro için yuzde",Faiz_orani,"(yillik) faiz orani ile",Faiz_suresi,
      "yil sonunda alacaginiz faiz tutarı",Faiz_tutari,"euro'dur.","\n",
      "Toplam miktar ise",Anapara+Faiz_tutari,"euro'dur.")
print("Bu oranla 1 aylik faiz miktari",Faiz_aylik,"euro'dur.","\n",
      "Toplam miktar ise",Anapara+Faiz_aylik,"euro'dur.")
print("Bu oranla 1 gunluk faiz miktari",Faiz_gunluk,"euro'dur.","\n",
      "Toplam miktar ise",Anapara+Faiz_gunluk,"euro'dur.")
