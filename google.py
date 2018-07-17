def arama():
    while(True):
        import webbrowser


        new = 2

        tabUrl = "http://google.com/?"
        term = input("Ne Aramak İstersiniz:")


        webbrowser.open(tabUrl + term, new=new)
        Cıkıs = input("Çıkış Yapmak İstiyor Musunuz? ")
        if Cıkıs=="Hayır":
            continue
        elif Cıkıs=="Evet":
            break