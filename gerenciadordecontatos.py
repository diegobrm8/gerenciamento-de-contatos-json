import json 

class GerenciadorContatos:
    def __init__(self, arquivo_contatos):
        self.arquivo_contatos = arquivo_contatos
        self.contatos = self.carregar_contatos()


    def carregar_contatos(self):
        try:
            with open(self.arquivo_contatos, 'r') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            return []

    def salvar_contatos(self):
        with open(self.arquivo_contatos, 'w') as arquivo:
            json.dump(self.contatos, arquivo, indent=4)

    def adicionar_contato(self, nome, telefone):
        novo_contato = {"nome": nome, "telefone": telefone}
        self.contatos.append(novo_contato)
        self.salvar_contatos()

    def listar_contatos(self):
        for i, contato in enumerate(self.contatos, start=1):
            print(f"{i}. Nome: {contato['nome']}, Telefone: {contato['telefone']}")
    

if __name__ == "__main__":
    gerenciador = GerenciadorContatos("contatos.json")

    while True:
        print("\n=== Gerenciador de Contatos ===")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            gerenciador.adicionar_contato(nome, telefone)
            print("Contato adicionado com sucesso!")
        elif opcao == "2":
            print("\nLista de contatos:")
            gerenciador.listar_contatos()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")