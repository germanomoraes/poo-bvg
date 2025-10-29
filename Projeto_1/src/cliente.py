class Cliente:
    """Classe que representa um cliente de uma loja."""

    def __init__(self, nome, idade, saldo):
        # Atributos privados (Encapsulamento)
        self.__nome = nome
        self.__idade = idade
        self.__saldo = saldo

    def mostrar_informacoes(self):
        """Exibe as informações do cliente."""
        print(f"Cliente: {self.__nome}, Idade: {self.__idade}, Saldo: R${self.__saldo:.2f}")

    def atualizar_saldo(self, valor):
        """Atualiza o saldo do cliente."""
        self.__saldo += valor
        print(f"Saldo atualizado! Novo saldo: R${self.__saldo:.2f}")


if __name__ == "__main__":
    cliente1 = Cliente("Germano", 30, 1000.0)
    cliente1.mostrar_informacoes()
    cliente1.atualizar_saldo(500.0)
    cliente1.mostrar_informacoes()