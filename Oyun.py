def oyun():
    while(True):
        print("Oyundan Cıkmak İcin q Basabilirsiniz:")
        taskagitmakas = ["Taş", "Kağıt", "Makas"]
        import random
        Taş = taskagitmakas[0]
        Kağıt = taskagitmakas[1]
        Makas = taskagitmakas[2]
        gir = input("Taş mı? Kağıt mı? Makas mı? Çıkış Mı ?:")
        a = random.choice(taskagitmakas)

        if gir == Kağıt:
            if Kağıt == a:
                print("Bilgisayar", a, "Seçti")
                print("Berabere")
            elif Taş == a:
                print("Bilgisayar", a, "Seçti")
                print("Kazandınız")
            elif Makas == a:
                print("Bilgisayar", a, "Seçti")
                print("Kaybettiniz")
        elif gir == Taş:
            if Taş == a:
                print("Bilgisayar", a, "Seçti")
                print("Berabere")
            elif Kağıt == a:
                print("Bilgisayar", a, "Seçti")
                print("Kaybettiniz")
            elif Makas == a:
                print("Bilgisayar", a, "Seçti")
                print("Kazandınız")
        elif gir == Makas:

            if gir == Makas:
                print("Bilgisayar", a, "Seçti")
                print("Berabere")
            elif Taş == a:
                print("Bilgisayar", a, "Seçti")
                print("kaybettiniz")
            elif Kağıt == a:
                print("Bilgisayar", a, "Seçti")
                print("Kazandınız")
        elif gir == "q":
            print("Oyundan Çıkıldı")
            break

        else:
            print("Tekrar Yazar Mısın?")
