print("Aylik Masraf Programi")
print("Aylik gelir ve harcama miktarlarinizi asagida belirtir misiniz?")
gelir=input("Aylik geliriniz kaç euro'dur? :")
mutfak=input("Mutfak harcamalarınız :")
egitim=input("Egitim harcamalarınız :")
giyim=input("Giyim harcamalarınız :")
ulasim=input("Ulasim harcamalarınız :")
masraf=float(int(mutfak)+int(egitim)+int(giyim)+int(ulasim))
oran=float(int(masraf)/int(gelir))
print("Aylik",gelir,"euro gelirinize karşılık aylık toplam masrafiniz",
      masraf,"euro'dur.","\n","Bu masraflarinizin aylik gelirinize orani ise",
      oran,"seklindedir.","\n","Yani gelirinizin yuzde",oran*100,
      "kadarini masraflariniza ayirmalisiniz.")









 
