def fibonacci_recursive(n, kroki):
    kroki[0] += 1
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1, kroki) + fibonacci_recursive(n - 2, kroki)

def fibonacci_memo(n, memo, kroki):
    kroki[0] += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibonacci_memo(n - 1, memo, kroki) + fibonacci_memo(n - 2, memo, kroki)
    return memo[n]

def fibonacci_bottom_up(n):
    kroki = 0
    if n <= 1:
        return n, 1
    fib = [0, 1]
    for i in range(2, n + 1):
        kroki += 1
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n], kroki

def main():
    while True:
        print("\n--- MENU ---")
        print("1. Oblicz F(n) rekurencyjnie")
        print("2. Oblicz F(n) z memoizacją")
        print("3. Oblicz F(n) metodą Bottom-Up")
        print("4. Wyjście")

        wybor = input("Wybierz opcję (1-4): ")

        if wybor == '4':
            print("Zamykanie programu.")
            break

        try:
            numer_albumu = int(input("Podaj swój numer albumu: "))
        except ValueError:
            print("Niepoprawny numer albumu!")
            continue

        n = round(numer_albumu / 100)
        print(f"Obliczam F({n})...")

        if wybor == '1':
            if n > 30:
                print("Chcę stąd dzisiaj wyjść, podaj liczbę docelową maksymalnie 30 XD")
            else:
                kroki = [0]
                wynik = fibonacci_recursive(n, kroki)
                print(f"F({n}) = {wynik}, liczba kroków: {kroki[0]}")

        elif wybor == '2':
            kroki = [0]
            wynik = fibonacci_memo(n, {}, kroki)
            print(f"F({n}) = {wynik}, liczba kroków: {kroki[0]}")

        elif wybor == '3':
            wynik, kroki = fibonacci_bottom_up(n)
            print(f"F({n}) = {wynik}, liczba kroków: {kroki}")

        else:
            print("Niepoprawna opcja. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
