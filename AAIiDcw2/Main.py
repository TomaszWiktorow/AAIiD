import os
import string

def binary_search(lista, szukany_element):
    """
    Wyszukiwanie binarne z liczeniem kroków.
    """
    lewo = 0
    prawo = len(lista) - 1
    kroki = 0

    while lewo <= prawo:
        kroki += 1
        srodek = (lewo + prawo) // 2
        if lista[srodek] == szukany_element:
            return srodek, kroki
        elif lista[srodek] < szukany_element:
            lewo = srodek + 1
        else:
            prawo = srodek - 1
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
    posortowane = sorted(slowa, key=str.lower)

    for litera in litery:
        znalezione = None
        for slowo in posortowane:
            if slowo.lower().startswith(litera):
                znalezione = slowo
                break
        if znalezione:
            indeks, kroki = binary_search(posortowane, znalezione)
            print(
                f"Słowo zaczynające się na '{litera}' to '{znalezione}' (indeks {indeks} w posortowanej liście) - znalezione w {kroki} krokach.")
        else:
            print(f"Nie znaleziono słowa na literę '{litera}'.")


def wyszukaj_ostatnie_slowo(slowa):
    if not slowa:
        print("Brak słów do analizy.")
        return
    ostatnie_slowo = slowa[-1]
    posortowane = sorted(slowa, key=str.lower)
    indeks, kroki = binary_search(posortowane, ostatnie_slowo)
    print(
        f"Ostatnie słowo w oryginalnej liście to '{ostatnie_slowo}' - znalezione w posortowanej liście na indeksie {indeks} w {kroki} krokach.")

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
