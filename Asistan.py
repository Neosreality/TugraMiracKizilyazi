import sys
import Oyun
import time
import datetime
import os
import google



class Soyle:
    print('''
T:::::::::::::::::::::T        R::::::::::::::::R          U::::::U     U::::::U        X:::::X       X:::::X
T:::::::::::::::::::::T        R::::::RRRRRR:::::R         U::::::U     U::::::U        X:::::X       X:::::X
T:::::TT:::::::TT:::::T        RR:::::R     R:::::R        UU:::::U     U:::::UU        X::::::X     X::::::X
TTTTTT  T:::::T  TTTTTT          R::::R     R:::::R         U:::::U     U:::::U         XXX:::::X   X:::::XXX
        T:::::T                  R::::R     R:::::R         U:::::D     D:::::U            X:::::X X:::::X   
        T:::::T                  R::::RRRRRR:::::R          U:::::D     D:::::U             X:::::X:::::X    
        T:::::T                  R:::::::::::::RR           U:::::D     D:::::U              X:::::::::X     
        T:::::T                  R::::RRRRRR:::::R          U:::::D     D:::::U              X:::::::::X     
        T:::::T                  R::::R     R:::::R         U:::::D     D:::::U             X:::::X:::::X    
        T:::::T                  R::::R     R:::::R         U:::::D     D:::::U            X:::::X X:::::X   
        T:::::T                  R::::R     R:::::R         U::::::U   U::::::U         XXX:::::X   X:::::XXX
      TT:::::::TT              RR:::::R     R:::::R         U:::::::UUU:::::::U         X::::::X     X::::::X
      T:::::::::T       ...... R::::::R     R:::::R ......   UU:::::::::::::UU   ...... X:::::X       X:::::X
      T:::::::::T       .::::. R::::::R     R:::::R .::::.     UU:::::::::UU     .::::. X:::::X       X:::::X
      TTTTTTTTTTT       ...... RRRRRRRR     RRRRRRR ......       UUUUUUUUU       ...... XXXXXXX       XXXXXXX''')
    isim = input("İsminiz Nedir:")
    print("Merhaba", isim, "Bey")
    print(isim ,"Bey Bu Sizin Bilgisayar Bilgileriniz")
    print("Kullanıcı adı:  ", os.environ["USERNAME"])
    print("Bilgisayar adı: ", os.environ["COMPUTERNAME"])
    print("Ev dizini:      ", os.environ["HOMEPATH"])
    print("İşlemci:        ", os.environ["PROCESSOR_IDENTIFIER"])
    print("İşlemci sayısı: ", os.environ["NUMBER_OF_PROCESSORS"])
    while (True):
        secim=input("T.R.U.X >> Ne Yapmak İstersiniz:")
        if secim == "By":
            print("T.R.U.X >>",isim, "Bey Görüşürüz")
            sys.exit()
        elif secim == "Yazı Yazmak":
            a = input("Adı Ne Olsun")
            dosya = open("a", "w")

        elif secim == "Adın Ne":
            print("T.R.U.X")


        elif secim == "Amacın Ne":
            print("T.R.U.X >> Beratı Sikmek")

        elif secim == "Saat Kaç":
            print(time.strftime("T.R.U.X >> Saat:%H Dakika:%M"))

        elif secim=="Oyun Oynamak":
            print("Eğlence Başlasın")
            Oyun.oyun()

        elif secim=="Google":
            google.arama()
            
        elif secim=="Seni Kim Yarattı":
            print("Tuğra Miraç Kızılyazı")
        




        else:
            print("Bir Daha Yazar Mısınız")
        secim = secim.capitalize()           
