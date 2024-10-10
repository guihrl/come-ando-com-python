# #O metodo pertence a uma classe
# # __init__ é um metodo constru
# #exemplo 


# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#     def apresentar(self):
#         print(f"Ola, meu nome é {self.nome} e tenho {self.idade} anos.")
    
#     def data_nascimento(self):
#         print(2024 - self.idade)
        
#     def sobrenome(self):
#         sobre_nome = "Henrique"
#         print( self.nome +" "+ sobre_nome)
        
        

# pessoa1 = Pessoa("Claudio", 40)
# pessoa1.apresentar()
# pessoa1.data_nascimento()
# pessoa2 = Pessoa("Carlos", 31)
# pessoa2.data_nascimento()
# print(pessoa1.idade - pessoa2.idade)
# pessoa1.sobrenome()

# class Aluno:
#     def __init__(self, nome, nota):
#         self.nome = nome
#         self.nota = nota
    
#     def nota_anual(self):
#         if self.nota > 7:
#             print(f"Seu nome é {self.nome} e sua nota foi {self.nota}. Parabéns você passou!!!!")
#         else:
#             print(f"Seu nome é {self.nome} e sua nota foi {self.nota}. Você reprovou.")

# aluno1 = Aluno("Guilherme", 10)
# aluno1.nota_anual()
# aluno2 = Aluno("Mario", 5)
# aluno2.nota_anual()

# class Animal:
#     def __init__(self, nome):
#         self.nome = nome
#     def emitir_som(self):
#         print(f"{self.nome} diz:barulho")
# class Cachorro(Animal):
#     pass
# class Gato(Animal):
#     pass

# dog = Cachorro("Rex")
# cat = Gato("Tom")

# dog.emitir_som()
# cat.emitir_som()

# class Padaria:
#     def __init__(self, nome):
#         self.nome = nome
    
#     def funcionario(self):
#         print(f"{self.nome} é um bom funcionario")

# class Padeiro(Padaria):
#     pass
# class Seguranca(Padaria):
#     pass

# funcionario1 = Padeiro("Carlos")
# funcionaio2 = Seguranca("João")

# funcionario1.funcionario()
# funcionaio2.funcionario()

# class Animal:
#     def fazer_som(self):
#         pass
# class Cachorro(Animal):
#     def fazer_som(self):
#         print("Au Au!")
# class Gato(Animal):
#         def fazer_som(self):
#             print("Miau!")
            
# animais = [Cachorro(), Gato()]

# for animal in animais:
#     animal.fazer_som()

# class Padaria:
#     def funcionario(self):
#         pass

# class Padeiro(Padaria):
#     def funcionario(self):
#         print("O padeiro é um bom funcionario")

# class Seguranca(Padaria):
#     def funcionario(self):
#         print("O segurança é um bom funcionario")

# funcionarios = [Padeiro(), Seguranca()]

# for funcionario in funcionarios:
#     funcionario.funcionario()


# class Pessoa:
#     def __init__(self, nome):
#         self.__nome = nome
    
#     @property #Converte um  metodo em atributo #getters
#     def nome(self):
#         return self.__nome
    
#     @nome.setter #setters
#     def nome(self, novo_nome):
#         if isinstance(novo_nome, str) and novo_nome.strip():
#             self.__nome = novo_nome
#         else:
#                 print("Nome inválido")
                
# # Uso da classe
# pessoa = Pessoa("João")
# print(pessoa.nome)  # Saída: João
# pessoa.nome = "Maria"
# print(pessoa.nome)  # Saída: Maria

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property 
    def nome_privado(self):
        return self.__nome
    
        
    def exibir_informaçoes(self):
        print(f"Nome: {self.__nome} Idade: {self.__idade}")


pessoa = Pessoa("João", 30)

#Tenntativa de acessar atributos privados __nome
print(pessoa.nome_privado) 

