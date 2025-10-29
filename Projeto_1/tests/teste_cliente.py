from src.cliente import Cliente

def test_atualizar_saldo():
    c = Cliente("Maria", 25, 1000)
    c.atualizar_saldo(200)
    # Aqui não há assert real, apenas execução para validar manualmente
    c.mostrar_informacoes()