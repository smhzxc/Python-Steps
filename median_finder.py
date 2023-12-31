sayilar = [] # Girilen sayıları depolayacak bir liste açıyorum
while True:
    sayi = input("Lütfen bir sayı girin (Çıkmak için 'E' veya 'e' tuşuna basın): ") # Girilen sayıları listeye input ediyorum
    if sayi == "E" or sayi == "e":
        break  # Girilen sayının E ve ya e olduğunu kontrol ediyorum eğer ikisinden biri ise break döngüyü
    # durdurup çıkış yapacak
    else:  # Değilse girilen sayılar sayilar listesine eklenecek
        sayilar.append(float(sayi))

sayilar.sort() # Girilen sayıları küçükten büyüğe sıralıyorum
n = len(sayilar) # n ifadesine len komutuyla listedeki sayı sayısını yüklüyorum
if n % 2 == 0:
    medyan = (sayilar[n // 2 - 1] + sayilar[n // 2]) / 2
    # Çift sayıda eleman varsa medyan ortalama ortadaki iki sayının aritmetik ortalamasıdır. Bu yüzden gerekli işlemi
    # işletiyorum
else:
    medyan = sayilar[n // 2]
    # Tek sayıda eleman varsa medyan ortadaki sayıdır

print("Girilen sayıların medyanı:", medyan)
# Medyanı ekrana yazdırıyorum
