from temperature_manager import TemperatureManager

def menu():
    print("\n🌡️ CONTROLE DE TEMPERATURAS DIÁRIAS 🌡️")
    print("1 - Adicionar registro")
    print("2 - Listar registros")
    print("3 - Calcular médias semanais")
    print("4 - Mostrar extremos (quente/frio)")
    print("5 - Sair")

def main():
    manager = TemperatureManager()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            dia = input("Dia (ex: Segunda): ")
            max_t = float(input("Temperatura máxima: "))
            min_t = float(input("Temperatura mínima: "))
            manager.adicionar_registro(dia, max_t, min_t)

        elif opcao == '2':
            manager.listar_registros()

        elif opcao == '3':
            manager.calcular_media()

        elif opcao == '4':
            manager.extremos()

        elif opcao == '5':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
