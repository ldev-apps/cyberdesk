def afficher_menu():

    ligne="=========================="
    titre="         cyberdesk"
    syst="1. system information"
    ca="2. network analysis"
    s="3. security"
    ai="4. artificial intelligence"
    q="5. quit"
    
    print("cyberdesk works")
    print(ligne)
    print(titre)
    print(ligne)
    print(syst)
    print(ca)
    print(s)
    print(ai)
    print(q)
while True:
    afficher_menu()
    try:
         
        condition=int(input("put nomber"))

        if condition ==1:
            print("launching the system information module")
                    
        elif condition==2:
            print("the connection analysis is in development")

        elif condition==3:
            print("the security check is in development")

        elif condition==4:
            print("local ai is in development")

        elif condition==5:
            print("quitting cyberdesk...")
            print("end")
            break
        else:
            print("error : invalid choice")

    except ValueError:
            print("this is not a number")

