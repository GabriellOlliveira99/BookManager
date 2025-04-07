from funcoes_biblioteca import listar_livros, adicionar_livro, deletar_livro

def menu():
    print("\n" + "="*33)
    print("=== BEM-VINDO AO BOOK MANAGER ===")
    print("="*33 + "\n")
    print("1. Listar livros")
    print("2. Adicionar livro")
    print("3. Deletar livro")
    print("3. Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_livros()
    elif opcao == "2":
        print("\n=== Adicionar Livro ===")
        livro = {}
        livro["id"] = int(input("ID: "))
        livro["titulo"] = input("Título: ")
        livro["autor"] = input("Autor: ")
        livro["genero"] = input("Gênero: ")
        livro["status"] = "Disponível"
        livro["ano_publicacao"] = input("Ano de Publicação: ")
        livro["paginas"] = input("Páginas: ")
        adicionar_livro(livro)
    elif opcao == "3":
        print("\n=== Deletar Livro ===")
        id_livro = int(input("ID do livro a ser deletado: "))
        deletar_livro(id_livro)
    elif opcao == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
