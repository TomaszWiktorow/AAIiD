import os
import string

def linear_search(lista, szukany_element):
    kroki = 0
    for indeks in range(len(lista)):
        kroki += 1
        if lista[indeks] == szukany_element:
            return indeks, kroki
    return -1, kroki

def oczysc_ze_znakow(slowo):
    return slowo.translate(str.maketrans('', '', string.punctuation))

def wczytaj_slowa_z_pliku(sciezka):
    """
    Wczytuje wszystkie słowa z pliku i usuwa znaki interpunkcyjne.
    """
    if not os.path.exists(sciezka):
        print(f"Plik '{sciezka}' nie istnieje.")
        return []

    slowa = []
    with open(sciezka, 'r', encoding='utf-8') as plik:
        for linia in plik:
            slowa.extend([oczysc_ze_znakow(s) for s in linia.strip().split()])
    return slowa

def wyszukaj_slowa_na_litery(slowa):
    litery = ['a', 'c', 'd', 'm', 'w', 'z']
    for litera in litery:
        znalezione = None
        for slowo in slowa:
            if slowo.lower().startswith(litera):
                znalezione = slowo
                break
        if znalezione:
            indeks, kroki = linear_search(slowa, znalezione)
            print(
                f"Słowo zaczynające się na '{litera}' to '{znalezione}' (indeks {indeks}) - znalezione w {kroki} krokach.")
        else:
            print(f"Nie znaleziono słowa na literę '{litera}'.")


def wyszukaj_ostatnie_slowo(slowa):
    if not slowa:
        print("Brak słów do analizy.")
        return
    ostatnie_slowo = slowa[-1]
    indeks, kroki = linear_search(slowa, ostatnie_slowo)
    print(f"Ostatnie słowo w pliku to '{ostatnie_slowo}' (indeks {indeks}) - znalezione w {kroki} krokach.")

while True:
    print("\n--- MENU ---")
    print("1. Wyszukiwanie słów na litery 'a', 'c', 'd', 'm', 'w', 'z'")
    print("2. Wyszukiwanie ostatniego słowa z pliku")
    print("3. Wyjście")

    wybor = input("Wybierz opcję (1/2/3): ")

    if wybor == "1":
        sciezka = input("Podaj nazwę pliku (np. C:\\Users\\Wolfi\\Desktop\\plik.txt): ")
        slowa = wczytaj_slowa_z_pliku(sciezka)
        if slowa:
            wyszukaj_slowa_na_litery(slowa)
    elif wybor == "2":
        sciezka = input("Podaj nazwę pliku (np. C:\\Users\\Wolfi\\Desktop\\plik.txt): ")
        slowa = wczytaj_slowa_z_pliku(sciezka)
        if slowa:
            wyszukaj_ostatnie_slowo(slowa)
    elif wybor == "3":
        print("Zamykanie programu...")
        break
    else:
        print("Nieprawidłowa opcja. Wybierz 1, 2 lub 3.")
