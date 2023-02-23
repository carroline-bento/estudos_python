import contas


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super(Cliente, self).__init__(nome, idade)
        self.conta: contas.Conta or None 


if __name__ == '__main__':
    cliente = Cliente('carol', 19)
    cliente.conta = contas.ContaCorrente(111, 222, 0, 100)
    print(cliente)    
    print(cliente.conta)    
    cliente2 = Cliente('joana', 50)
    cliente2.conta = contas.ContaPoupanca(548, 221, 0)
    print(cliente2)    
    print(cliente2.conta) 
    

    