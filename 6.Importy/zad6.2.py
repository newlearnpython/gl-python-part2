import functions



while True:

    print ('''Oto prosty kalkulator w Pythonie, pozwalający na 4 podstawowe działania matematyczne:
    1. - dodawanie
    2. - odejmowanie
    3. - mnożenie
    4. - dzielenie 
    0. - aby zakończyć działanie programu''')



    dzialanie = input ("Podaj numer operacji aby wykonać działanie lub  '0' aby zakończyć : ")

    if dzialanie == '0' :
        exit

    a = int(input("podaj pierwszą liczbę : "))
    b = int(input("podaj drugą liczbę : "))

    

    if dzialanie == '1' :
        wynik_dodawania = functions.dodawanie(a,b)
        print (wynik_dodawania)
    
    elif dzialanie == '2' :
        wynik_odejmowania = functions.odejmowanie(a,b)
        print (wynik_odejmowania)
    
    elif dzialanie == '3' :
        wynik_mnozenia = functions.mnozenie(a,b)
        print (wynik_mnozenia)
    
    elif dzialanie == '4' :
        if b == '0':
            print("Błąd - Nasz system matematyki zabrania dzielenia przez zero")
    else:
        wynik_dzielenia = functions.dzielenie(a,b)
        print (wynik_dzielenia)

