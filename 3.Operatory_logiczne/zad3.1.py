userage = input ("Ile masz lat? Wpisz liczbe :")
czy_A2 = input ("Czy masz prawo jazdy kategorii A2? :")
if czy_A2 == ("tak, Tak, TAK") :
    A2_age = input ("Ile lat masz kategorie A2? :")
    pass


if int(userage) >= 24 or (int(userage) >= 20 and int(A2_age) >= 2) :
    print("użytkownik może zdawać na kategorie A")
if not int(userage) >= 24 or (int(userage) >= 20 and int(A2_age) >= 2) :
    print ("Użytkownik nie może zdawać na kategorie A")
