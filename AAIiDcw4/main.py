import os
import string

def oczysc_ze_znakow(slowo):
    return slowo.translate(str.maketrans('', '', string.punctuation))

def wczytaj_slowa_z_pliku(sciezka):
    """
    Wczytuje słowa z pliku i usuwa znaki interpunkcyjne.
    """
    if not os.path.exists(sciezka):
        print(f"Plik '{sciezka}' nie istnieje.")
        return []

    slowa = []
    with open(sciezka, 'r', encoding='utf-8') as plik:
        for linia in plik:
            slowa.extend([oczysc_ze_znakow(s) for s in linia.strip().split()])
    return slowa

def quicksort(slowa):
    """
    QuickSort z liczeniem kroków porównań.
    Zwraca: posortowaną listę, liczba kroków
    """
    def qs(lista):
        nonlocal kroki
        if len(lista) <= 1:
            return lista
        pivot = lista[0]
        lewa = []
        prawa = []
        for x in lista[1:]:
            kroki += 1
            if x.lower() < pivot.lower():
                lewa.append(x)
            else:
                prawa.append(x)
        return qs(lewa) + [pivot] + qs(prawa)

    kroki = 0
    wynik = qs(slowa)
    return wynik, kroki

while True:
    print("\n--- MENU ---")
    print("1. Sortuj słowa z pliku")
    print("2. Wyjście")

    wybor = input("Wybierz opcję (1/2): ")

    if wybor == "1":
        sciezka = input("Podaj ścieżkę do pliku:")
        slowa = wczytaj_slowa_z_pliku(sciezka)

        if slowa:
            posortowane, kroki = quicksort(slowa)
            print("\nPosortowane słowa:")
            print(posortowane)
            print(f"Liczba porównań (kroków): {kroki}")
    elif wybor == "2":
        print("Zamykanie programu...")
        break
    else:
        print("Nieprawidłowa opcja. Wybierz 1 lub 2.")
