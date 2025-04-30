def verify_pesel(pesel: str) -> int:
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = 0

    for i in range(10):
        suma += int(pesel[i]) * wagi[i]

    kontrolna = (10 - (suma % 10)) % 10

    return 1 if kontrolna == int(pesel[10]) else 0


# Przykładowe wywołanie:
if __name__ == "__main__":
    pesel_input = "97082123152"
    print(verify_pesel(pesel_input))  # Oczekiwane wyjście: 0