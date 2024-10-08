#O metodo pertence a uma classe
# __init__ é um metodo constru
#exemplo 










def pipoca():
    pass


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"Ola, meu nome é {self.nome} e tenho {self.idade} anos.")
    
    def data_nascimento(self):
        print(2024 - self.idade)
        
    def sobrenome(self):
        sobre_nome = "Henrique"
        print( self.nome +" "+ sobre_nome)
        
        

pessoa1 = Pessoa("Claudio", 40)
pessoa1.apresentar()
pessoa1.data_nascimento()
pessoa2 = Pessoa("Carlos", 31)
pessoa2.data_nascimento()
print(pessoa1.idade - pessoa2.idade)
pessoa1.sobrenome()










