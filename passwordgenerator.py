import string
import random
import time
import sys
import os
from collections import OrderedDict

#passwordgen.txt for created passwords
#randompassgen.txt for deleting bruteforcing list
#TODO karakterı gırınıze ab gırılırse error ver

#TODO istenmeyen harfi passwordable dan cikar bknz: password_generator() DONE!

LETTERS = string.ascii_letters#TODO random buyuk, kucuk harf yap/done.
NUMBERS = string.digits
PUNCTUATION = string.punctuation
lenght= int(input("Sifre uzunlugu ne olsun: "))
istenmeyen_karakterler = []
def istenmeyen_karakter():#istenmeyen karakteri kullanicidan aldik
    karakter_sayisi = int(input("Kac karakter cikarmak istiyorsunuz: "))#TODO sayi girilmesse uyari ver/done.
    i = 0
    print("=====================")
    while i < karakter_sayisi:
            istenmeyen_karakter.karakter = str(input("Karakteri giriniz: "))
            istenmeyen_karakterler.append(istenmeyen_karakter.karakter)
            i =i+1
    print("=====================")
    for i in range(len(istenmeyen_karakterler)):
        for j in range(i + 1, len(istenmeyen_karakterler)):
            if istenmeyen_karakterler[i]==istenmeyen_karakterler[j]:
                print("Ayni şeyleri girmeyin!")
                sys.exit(1)
            else:
                continue
    return
def wordlist_remove():#listimizin degisken adi wordlist_remove.mylist
    wordlist_remove.onay = str(input("Herhangi bir bruteforce wordlistiyle olusan sifreyi\nkarsilastirmak ister misiniz (bu biraz zaman alacaktir!)\n(KULLANACAGINIZ LISTENIN ADI passwordgen.txt OLMALI?: Y/N "))
    print("========================")
    if wordlist_remove.onay.upper() == 'Y':
        with open('passwordgen.txt') as j:
            wordlist_remove.mylist = j.read().splitlines()
            wordlist_remove.mylist = list(wordlist_remove.mylist)
            print("LISTE YUKLENIYOR")
            bar = [
        " [=     ]",
        " [ =    ]",
        " [  =   ]",
        " [   =  ]",
        " [    = ]",
        " [     =]",
        " [    = ]",
        " [   =  ]",
        " [  =   ]",
        " [ =    ]",
        "YUKLEME BASARILI\n",
        "========================\n"]
        i = 0
        while i<15:
            print(bar[i % len(bar)], end="\r")
            time.sleep(0.2)
            i += 1
    
    elif wordlist_remove.onay.upper() =='N':

        with open('passwordgen.txt') as j:
            wordlist_remove.mylist = j.read().splitlines()
            wordlist_remove.mylist = list(wordlist_remove.mylist)

        print("Tamam, devam ediyoruz")
        print("========================")

    else:
        with open('passwordgen.txt') as j:
            wordlist_remove.mylist = j.read().splitlines()
            wordlist_remove.mylist = list(wordlist_remove.mylist)
        print("Gecerli bir harf girmediginiz icin program bu sekmeyi atlayacak")
    
    return wordlist_remove.mylist



def nerede_kullanacaksin():
    nerede_kullanacaksin.site = input("Bu sifre nerenin sifresi: ")
    print("========================")
    nerede_kullanacaksin.site = nerede_kullanacaksin.site.upper()
    return nerede_kullanacaksin.site#global variable

def password_generator(x):
    passwordable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'#tum harfler bastırıldı
    passwordable = list(passwordable)#listeye cevirildi
    istenmeyen_karakterler_int_plus = len(istenmeyen_karakterler)
    i = 0
    while i < istenmeyen_karakterler_int_plus:#TODO aynı karakter girirse error veriyor izin verme/done.
        passwordable.remove(istenmeyen_karakterler[i])
        i = i+1
    print("ISTENMEYEN KARAKTERLER SILINDI")
    print("========================")
    passwordable*random.randint(1,257)#iyice karistirdik
    random.shuffle(passwordable)#hepsi karistirildi

    random_pass= random.choices(passwordable, k=x)#istenen harf kadari alindi
    
    
    random_pass=''.join(map(str, random_pass))#stringe cevilirdi
    if wordlist_remove.onay.upper() == 'Y':
        print("ESLESMELER SILINIYOR")
        bar = [
        " [=     ]",
        " [ =    ]",
        " [  =   ]",
        " [   =  ]",
        " [    = ]",
        " [     =]",
        " [    = ]",
        " [   =  ]",
        " [  =   ]",
        " [ =    ]"]
        
        a = 0

        while a<4:
            print(bar[a % len(bar)], end="\r")
            time.sleep(0.2)
            a += 1

        z = 0
        mylistlength = len(wordlist_remove.mylist)
        random_pass_list = list(random_pass)
        while z < mylistlength:#BRUTE FORCEDE BULUNAN CUMLELER SILINDI
            if wordlist_remove.mylist[z] in random_pass_list:
                random_pass_list.remove(wordlist_remove.mylist[z])
                z = z+1 
            else: 
                z = z+1
        random_pass_str =''.join(map(str,random_pass_list))
        b = 0
        print("ESLESMELER SILINDI")
        print("SIFRENIZ HAZIR")
        print("========================")

        print(nerede_kullanacaksin.site, "Sifresi:", random_pass_str)

        with open("randompassgen.txt", "a") as myfile:
            myfile.write('\n')
            myfile.write(nerede_kullanacaksin.site)
            myfile.write(' Sifresi: ')
            myfile.write(random_pass_str)
    elif wordlist_remove.onay.upper() == 'N':
        
        bar = [
        " [=     ]",
        " [ =    ]",
        " [  =   ]",
        " [   =  ]",
        " [    = ]",
        " [     =]",
        " [    = ]",
        " [   =  ]",
        " [  =   ]",
        " [ =    ]"]
        g = 0
        while g<15:
            print(bar[g % len(bar)], end="\r")
            time.sleep(0.2)
            g += 1

        print(nerede_kullanacaksin.site, "Sifresi:", random_pass_str)

        with open("randompassgen.txt", "a") as myfile:
            myfile.write('\n')
            myfile.write(nerede_kullanacaksin.site)
            myfile.write(' Sifresi: ')
            myfile.write(random_pass_str)
    return

        
    #i = 0

    #while i<15:
    #    print(bar[i % len(bar)], end="\r")
    #    time.sleep(0.2)
    #    i += 1

    #print(nerede_kullanacaksin.site, "Sifresi:", random_pass)

    #with open("randompassgen.txt", "a") as myfile:
    #    myfile.write('\n')
    #    myfile.write(nerede_kullanacaksin.site)
    #    myfile.write(' Sifresi: ')
    #    myfile.write(random_pass)
    #return

istenmeyen_karakter()
nerede_kullanacaksin()
wordlist_remove()
password_generator(lenght)
