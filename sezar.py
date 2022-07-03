def sezarolustur(metin):
    sifre = ""
    alfabe=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in metin:
        sifre+=alfabe[(alfabe.index(i)+21)%26]
    print("Sezar şifresi :",sifre)
    return metin

def sezarkir(metin):
    sifre = ""
    alfabe=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in metin:
        sifre+=alfabe[(alfabe.index(i)-21)%26]
    print("Kırılan şifre :",sifre)
    return metin

yesil = "\033[92m"
alti_cizili = '\033[4m'
kalin = '\033[1m'
normal = '\033[0m'

print(alti_cizili+yesil+"""---- #Coded By wolkan ----""")
print(normal+kalin+"""1- Sezar Şifresi Oluştur
2- Sezar Şifresi Kır""")

soru = input(normal+"Seçenek: ")

if (soru == "1"):
    isim = input("Metini giriniz (küçük harfler ile) : ")
    sezarolustur(isim)

elif (soru == "2"):
    isim = input("Sezar şifrenizi giriniz (küçük harfler ile) : ")
    sezarkir(isim)

else:
    print("Hatalı tuşlama yaptınız..!")
