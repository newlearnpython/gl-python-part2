
#palindrom

user_input = input("Podaj dowolne slowo: ")
odwrocone_slowo = user_input[::-1] 
if user_input == odwrocone_slowo :
    print("To slowo jest palindromem")
else:
    print("To slowo nie jest palindromem")
