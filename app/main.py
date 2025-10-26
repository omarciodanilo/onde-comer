from dados.estabelecimentos import estabelecimentos

def main():

    # Testar leitura dos dados
    print("--- Lista de estabelecimentos ---\n")
    for estabelecimento in estabelecimentos:
        print(f"Nome:\t{estabelecimento['nome']}")
        print(f"IG:\t{estabelecimento['instagram']}")
        print("Tipo:\t" + ", ".join(estabelecimento['tipo_culinaria']))
        print()

if __name__ == "__main__":
    main()
