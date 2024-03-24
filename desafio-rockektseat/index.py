contatos = []


def exibir_menu():
    print("------ Menu ------")
    print("1. Adicionar contato")
    print("2. Visualizar contatos")
    print("3. Editar contato")
    print("4. Marcar/desmarcar contato como favorito")
    print("5. Visualizar contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")


def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o e-mail do contato: ")
    favorito = input("É um contato favorito? (s/n): ").lower() == 's'
    contato = {'nome': nome, 'telefone': telefone,
               'email': email, 'favorito': favorito}
    contatos.append(contato)
    print("Contato adicionado com sucesso!")


def visualizar_contatos():
    print("------ Contatos ------")
    for i, contato in enumerate(contatos, 1):
        print(
            f"{i}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}, Favorito: {'Sim' if contato['favorito'] else 'Não'}")


def editar_contato():
    visualizar_contatos()
    indice = int(input("Digite o número do contato que deseja editar: ")) - 1
    if 0 <= indice < len(contatos):
        contato = contatos[indice]
        nome = input("Digite o novo nome do contato: ")
        telefone = input("Digite o novo telefone do contato: ")
        email = input("Digite o novo e-mail do contato: ")
        favorito = input("É um contato favorito? (s/n): ").lower() == 's'
        contato['nome'] = nome
        contato['telefone'] = telefone
        contato['email'] = email
        contato['favorito'] = favorito
        print("Contato editado com sucesso!")
    else:
        print("Índice inválido!")


def marcar_desmarcar_favorito():
    visualizar_contatos()
    indice = int(input(
        "Digite o número do contato que deseja marcar/desmarcar como favorito: ")) - 1
    if 0 <= indice < len(contatos):
        contato = contatos[indice]
        contato['favorito'] = not contato['favorito']
        print("Contato atualizado como favorito!")
    else:
        print("Índice inválido!")


def visualizar_contatos_favoritos():
    print("------ Contatos Favoritos ------")
    for contato in contatos:
        if contato['favorito']:
            print(
                f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")


def apagar_contato():
    visualizar_contatos()
    indice = int(input("Digite o número do contato que deseja apagar: ")) - 1
    if 0 <= indice < len(contatos):
        del contatos[indice]
        print("Contato apagado com sucesso!")
    else:
        print("Índice inválido!")


while True:
    exibir_menu()
    escolha = input("Digite sua escolha: ")
    if escolha == '1':
        adicionar_contato()
    elif escolha == '2':
        visualizar_contatos()
    elif escolha == '3':
        editar_contato()
    elif escolha == '4':
        marcar_desmarcar_favorito()
    elif escolha == '5':
        visualizar_contatos_favoritos()
    elif escolha == '6':
        apagar_contato()
    elif escolha == '7':
        print("Saindo...")
        break
    else:
        print("Escolha inválida!")
