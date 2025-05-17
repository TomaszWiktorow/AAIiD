def add_matrices(A, B):
    n = len(A)
    steps = 0
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]
            steps += 1
    return result, steps

def multiply_matrices(A, B):
    n = len(A)
    m = len(A[0])
    p = len(B[0])
    steps = 0

    result = [[0] * p for _ in range(n)]

    for i in range(n):
        for j in range(p):
            for k in range(m):
                result[i][j] += A[i][k] * B[k][j]
                steps += 1
    return result, steps

def transpose_matrix(A):
    n = len(A)
    m = len(A[0])
    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][i] = A[i][j]
    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)

# --- MENU ---
while True:
    print("\n--- MENU ---")
    print("1. Dodawanie macierzy")
    print("2. Mnożenie macierzy")
    print("3. Transpozycja macierzy")
    print("4. Wyjście")

    choice = input("Wybierz opcję (1-4): ")

    if choice == "1":
        sizes = [2, 3, 4, 5]
        for n in sizes:
            A = [[1 for _ in range(n)] for _ in range(n)]
            B = [[2 for _ in range(n)] for _ in range(n)]
            result, steps = add_matrices(A, B)
            print(f"\nDodawanie macierzy {n}x{n}: {steps} kroków")
            print_matrix(result)

    elif choice == "2":
        test_cases = [
            (2, 3, 4),
            (3, 4, 5),
            (4, 5, 4),
            (4, 5, 5)
        ]

        for n, m, p in test_cases:
            A = [[1 for _ in range(m)] for _ in range(n)]
            B = [[2 for _ in range(p)] for _ in range(m)]
            result, steps = multiply_matrices(A, B)
            print(f"\nMnożenie macierzy {n}x{m} * {m}x{p}: {steps} kroków")
            print_matrix(result)

    elif choice == "3":
        matrices = [
            [[1, 2, 3], [4, 5, 6]],
            [[7, 8], [9, 10], [11, 12]],
            [[13, 14, 15, 16]],
            [[17], [18], [19]]
        ]

        for idx, A in enumerate(matrices, start=1):
            print(f"\nMacierz {len(A)}x{len(A[0])}:")
            print("Oryginalna:")
            print_matrix(A)

            T = transpose_matrix(A)
            print("Transponowana:")
            print_matrix(T)

    elif choice == "4":
        print("Zamykanie programu...")
        break
    else:
        print("Nieprawidłowa opcja. Wybierz 1-4.")
