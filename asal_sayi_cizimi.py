import matplotlib.pyplot as plt
import numpy as np
import math

# https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
# Girilen sayının asal olup olmadığını kontrol ediyor.
def isPrime(n) :
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
  
#   Belli bir sayıya kadar ki asal sayıları bir liste halinde döndürüyor.
def asal_sayi_uret(n):
    asal_sayi_listesi = []
    for i in range(0,int(n)):
        if isPrime(i):
            asal_sayi_listesi.append(i)

    return asal_sayi_listesi



# ------- ANA KOD --------

# 5000'e kadar olan asal sayıları alıyor.
sayi_listesi = asal_sayi_uret(5000) 

koordinat_listesi = []

# Her sayı için, koordinatları belirleniyor.
for i, n in enumerate(sayi_listesi):
    x = n * math.cos(math.radians(n))
    y = n * math.sin(math.radians(n))

    koordinat_listesi.append([x,y])

    # Eğer yazılar açılmak isteniyorsa:
    # plt.text(x,y,str(n))


koordinat_listesi = np.asarray(koordinat_listesi)

plt.plot(koordinat_listesi[:,0],koordinat_listesi[:,1])

plt.show()
