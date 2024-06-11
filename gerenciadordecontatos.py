import json

class GerenciadorContatos:
    def __init__(self, arquivo_contatos):
        self.arquivo_contatos = arquivo_contatos
        self.contatos = self.carregar_contatos()

    def carregar_contatos(self):
        try:
            with open(self.arquivo_contatos, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            print(f"Aviso: O arquivo '{self.arquivo_contatos}' não foi encontrado. Criando um novo.")
            return []
        except json.JSONDecodeError:
            print(f"Erro: O arquivo '{self.arquivo_contatos}' está corrompido ou em um formato inválido.")
            return []

    def listar_contatos(self):
        if not self.contatos:
            print("Nenhum contato encontrado.")
            return
        for i, contato in enumerate(self.contatos, start=1):
            print(f"{i}. Nome: {contato['nome']}, Telefone: {contato['telefone']}")

# Teste
nome_arquivo = '#nome do arquivo json'
gerenciador = GerenciadorContatos(nome_arquivo)
gerenciador.listar_contatos()

