class Participante:
    """Representa uma pessoa inscrita em uma atividade do evento geek."""

    def __init__(self, nome, email, tipo_participacao):
        # Atributos privados: acesso controlado pelos métodos da classe
        self.__nome = nome
        self.__email = email
        self.__tipo_participacao = tipo_participacao

    def cadastrar(self):
        """Confirma o cadastro do participante."""
        print(f"Participante {self.__nome} cadastrado com sucesso!")

    def exibir_dados(self):
        """Exibe os dados do participante."""
        print("\n=== Dados do Participante ===")
        print(f"Nome: {self.__nome}")
        print(f"E-mail: {self.__email}")
        print(f"Tipo de participação: {self.__tipo_participacao}")

    # Métodos públicos para consultar os atributos privados
    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_tipo_participacao(self):
        return self.__tipo_participacao
