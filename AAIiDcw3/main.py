import os
import string

def selection_sort(slowa):
    """
    Sortowanie przez wybór z liczeniem kroków porównań.
    """
    n = len(slowa)
    kroki = 0

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            kroki += 1
            if slowa[j].lower() < slowa[min_index].lower():
                min_index = j
        # Zamiana miejscami
        slowa[i], slowa[min_index] = slowa[min_index], slowa[i]

    return slowa, kroki

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


while True:
    print("\n--- MENU ---")
    print("1. Sortuj słowa z pliku (algorytm: sortowanie przez wybór)")
    print("2. Wyjście")

    wybor = input("Wybierz opcję (1/2): ")

    if wybor == "1":
        sciezka = input("Podaj ścieżkę do pliku (np. C:\\Users\\Wolfi\\Desktop\\plik.txt): ")
        slowa = wczytaj_slowa_z_pliku(sciezka)

        if slowa:
            posortowane, kroki = selection_sort(slowa)
            print("\nPosortowane słowa:")
            print(posortowane)
            print(f"Liczba kroków porównań: {kroki}")
    elif wybor == "2":
        print("Zamykanie programu...")
        break
    else:
        print("Nieprawidłowa opcja. Wybierz 1 lub 2.")
