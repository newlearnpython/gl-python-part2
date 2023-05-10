#pobrać te rozszerzenia itd.
# link i instrukcje masz na czacie gmaila


def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    return a / b

#przypisanie numerów do działań
działania = {1:dodawanie, 2:odejmowanie, 3:mnozenie, 4:dzielenie}

print ('''Oto prosty kalkulator w Pythonie, pozwalający na 4 podstawowe działania matematyczne:
1. - dodawanie
2. - odejmowanie
3. - mnożenie
4. - dzielenie 
0. - aby zakończyć działanie programu''')

#operacje
def kalkulator():
    while (True):
        print()
    

działanie = input ("Podaj numer operacji aby wykonać działanie lub  '0' aby zakończyć : ")

if działanie == '0' :
    exit

a = float(input("podaj pierwszą liczbę : "))
b = float(input("podaj drugą liczbę : "))

    

if działanie == '1' :
    wynik_dodawania = dodawanie(a,b)
    print (wynik_dodawania)
    
elif działanie == '2' :
    wynik_odejmowania = odejmowanie(a,b)
    print (wynik_odejmowania)
    
elif działanie == '3' :
    wynik_mnożenia = mnozenie(a,b)
    print (wynik_mnożenia)
    
elif działanie == '4' :
    if b == '0':
        print("Błąd - Nasz system matematyki zabrania dzielenia przez zero")
    else:
        wynik_dzielenia = dzielenie(a,b)
        print (wynik_dzielenia)

