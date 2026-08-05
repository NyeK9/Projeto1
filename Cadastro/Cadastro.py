class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome} | Idade: {self.idade} | Email: {self.email}"


class SistemaCadastro:
    def __init__(self):
        self.pessoas = []

    def cadastrar(self, pessoa):
        self.pessoas.append(pessoa)
        print("Pessoa cadastrada com sucesso!")

    def listar(self):
        if not self.pessoas:
            print("Nenhuma pessoa cadastrada.")
        else:
            for pessoa in self.pessoas:
                print(pessoa)

    def buscar(self, nome):
        for pessoa in self.pessoas:
            if pessoa.nome.lower() == nome.lower():
                return pessoa
        return None

    def remover(self, nome):
        pessoa = self.buscar(nome)

        if pessoa:
            self.pessoas.remove(pessoa)
            print("Pessoa removida com sucesso!")
        else:
            print("Pessoa não encontrada.")


# Programa principal
sistema = SistemaCadastro()

while True:
    print("\n--- SISTEMA DE CADASTRO ---")
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Buscar pessoa")
    print("4 - Remover pessoa")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        email = input("Email: ")

        pessoa = Pessoa(nome, idade, email)
        sistema.cadastrar(pessoa)

    elif opcao == "2":
        sistema.listar()

    elif opcao == "3":
        nome = input("Digite o nome para buscar: ")
        resultado = sistema.buscar(nome)

        if resultado:
            print(resultado)
        else:
            print("Pessoa não encontrada.")

    elif opcao == "4":
        nome = input("Digite o nome para remover: ")
        sistema.remover(nome)

    elif opcao == "5":
        print("Sistema Encerrado!")
        break

    else:
        print("Opção inválida!")