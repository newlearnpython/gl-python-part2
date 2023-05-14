#Zaprojektuj klasę Czytelnik, która będzie reprezentowała czytelnika zapisanego do naszej biblioteki. Stwórz parę obiektów tego typu.

#tworzenie obiektu danej klasy - trzeba użyć konstruktora

# to co mamy poniżej w tym akapicie to konstruktor
#czemu id minus 1
class Czytelnik:
    id: int = -1

    def __init__ (self,
                imie: str, nazwisko: str, data_dolaczenia: int,
                tel: str, mail: str, liczba_pozyczonych_ksiazek: int):

        Czytelnik.id = +1


        self.imie =
        self.nazwisko =
        self.data_dolaczenia =
        self.tel =
        self.mail =
        self.liczba_pozyczonych_ksiazek = 



        # potem trzeba stworzyc pare obiektow (czytelnik 1, czyt.2 itd.)