from participante import Participante


def main():
    # Criando três objetos diferentes da classe Participante
    ana = Participante("Ana Costa", "ana@email.com", "Cosplay")
    bruno = Participante("Bruno Silva", "bruno@email.com", "Campeonato")
    carla = Participante("Carla Souza", "carla@email.com", "Palestra")

    # Chamando o método de cadastro para cada participante
    ana.cadastrar()
    bruno.cadastrar()
    carla.cadastrar()

    # Exibindo os dados dos três participantes
    print("\n=== Lista de Participantes ===")
    ana.exibir_dados()
    bruno.exibir_dados()
    carla.exibir_dados()


if __name__ == "__main__":
    main()
