from funcoes_biblioteca import listar_livros, adicionar_livro, deletar_livro, emprestar_livro, devolver_livro, listar_livros_disponiveis, listar_livros_emprestados


def menu():
    print("\n" + "="*33)
    print("=== BEM-VINDO AO BOOK MANAGER ===")
    print("="*33 + "\n")
    print("1. Lista de livros Completa")
    print("2. Listar livros disponíveis")
    print("3. Listar livros emprestados")
    print("4. Adicionar livro")
    print("5. Deletar livro")
    print("6. Empréstimo de livro")
    print("7. Devolução de livro")
    print("8. Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_livros()
    elif opcao == "2":
        listar_livros_disponiveis()
    elif opcao == "3":
        listar_livros_emprestados()
    elif opcao == "4":
        print("\n=== Adicionar Livro ===")
        livro = {}
        livro["id"] = int(input("ID: "))
        livro["titulo"] = input("Título: ")
        livro["autor"] = input("Autor: ")
        livro["genero"] = input("Gênero: ")
        livro["status"] = "Disponível"
        livro["ano_publicacao"] = int(input("Ano de Publicação: "))
        livro["paginas"] = int(input("Páginas: "))
        adicionar_livro(livro)
    elif opcao == "5":
        print("\n=== Deletar Livro ===")
        id_livro = int(input("ID do livro a ser deletado: "))
        deletar_livro(id_livro)
    elif opcao == "6":
        print("\n=== Solicitar Empréstimo de Livro ===")
        id_livro = int(input("ID do livro a ser emprestado: "))
        emprestar_livro(id_livro)
    elif opcao == "7":
        print("\n=== Solicitar Devolução de Livro ===")
        id_livro = int(input("ID do livro a ser devolvido: "))
        devolver_livro(id_livro)
    elif opcao == "8":
        print("Finalizando programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
