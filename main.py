def somar():
    """Função que pede dois números e mostra o resultado da soma."""
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print(f"A soma de {a} + {b} é = {a + b}")
    except ValueError:
        print("Por favor, digite apenas números válidos.")

if __name__ == "__main__":
    somar()