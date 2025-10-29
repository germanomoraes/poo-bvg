# Projeto 1 - Refatoração de Código Estruturado para POO
### Aluno: Germano de Oliveira Moraes

## Descrição
Este projeto transforma um código estruturado em uma versão orientada a objetos, utilizando uma classe `Cliente` para aplicar conceitos de **POO** como encapsulamento e abstração.

## Estrutura
- `src/cliente.py`: Código principal da classe `Cliente`
- `docs/README.md`: Documentação do projeto
- `tests/test_cliente.py`: Testes básicos

## Exemplo de Uso
```python
cliente1 = Cliente("Germano", 30, 1000.0)
cliente1.mostrar_informacoes()
cliente1.atualizar_saldo(500.0)
cliente1.mostrar_informacoes()

