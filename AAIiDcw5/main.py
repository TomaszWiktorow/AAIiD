def dodaj_macierze(a, b):
    wynik = []
    kroki = 0
    for i in range(len(a)):
        wiersz = []
        for j in range(len(a[0])):
            wiersz.append(a[i][j] + b[i][j])
            kroki += 1
        wynik.append(wiersz)
    return wynik, kroki

def mnoz_macierze(a, b):
    wiersze_a = len(a)
    kolumny_a = len(a[0])
    kolumny_b = len(b[0])
    wynik = [[0 for _ in range(kolumny_b)] for _ in range(wiersze_a)]
    kroki = 0
    for i in range(wiersze_a):
        for j in range(kolumny_b):
            for k in range(kolumny_a):
                wynik[i][j] += a[i][k] * b[k][j]
                kroki += 2  # mnożenie + dodanie
    return wynik, kroki

def transponuj_macierz(macierz):
    wiersze = len(macierz)
    kolumny = len(macierz[0])
    wynik = [[0 for _ in range(wiersze)] for _ in range(kolumny)]
    kroki = 0
    for i in range(wiersze):
        for j in range(kolumny):
            wynik[j][i] = macierz[i][j]
            kroki += 1
    return wynik, kroki

def wczytaj_macierz(wiersze, kolumny, numer):
    print(f"\nPodaj dane dla macierzy {numer}:")
    macierz = []
    for i in range(wiersze):
        wiersz = []
        for j in range(kolumny):
            val = int(input(f"Element [{i+1}][{j+1}]: "))
            wiersz.append(val)
        macierz.append(wiersz)
    return macierz

def wyswietl_macierz(macierz):
    for wiersz in macierz:
        print(" ".join(str(x) for x in wiersz))

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Dodawanie macierzy")
        print("2. Mnożenie macierzy")
        print("3. Transpozycja macierzy")
        print("4. Wyjście")
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            m = int(input("Podaj liczbę wierszy: "))
            n = int(input("Podaj liczbę kolumn: "))
            a = wczytaj_macierz(m, n, 1)
            b = wczytaj_macierz(m, n, 2)
            wynik, kroki = dodaj_macierze(a, b)
            print("\nWynik dodawania:")
            wyswietl_macierz(wynik)
            print(f"Liczba kroków: {kroki}")

        elif wybor == "2":
            m1 = int(input("Podaj liczbę wierszy pierwszej macierzy: "))
            n1 = int(input("Podaj liczbę kolumn pierwszej macierzy: "))
            m2 = int(input("Podaj liczbę wierszy drugiej macierzy: "))
            n2 = int(input("Podaj liczbę kolumn drugiej macierzy: "))
            if n1 != m2:
                print("Nie można pomnożyć: liczba kolumn pierwszej ≠ liczba wierszy drugiej.")
                continue
            a = wczytaj_macierz(m1, n1, 1)
            b = wczytaj_macierz(m2, n2, 2)
            wynik, kroki = mnoz_macierze(a, b)
            print("\nWynik mnożenia:")
            wyswietl_macierz(wynik)
            print(f"Liczba kroków: {kroki}")

        elif wybor == "3":
            m = int(input("Podaj liczbę wierszy macierzy: "))
            n = int(input("Podaj liczbę kolumn macierzy: "))
            macierz = wczytaj_macierz(m, n, "")
            wynik, kroki = transponuj_macierz(macierz)
            print("\nWynik transpozycji:")
            wyswietl_macierz(wynik)
            print(f"Liczba kroków: {kroki}")

        elif wybor == "4":
            print("Zamykanie programu...")
            break
        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")

menu()
