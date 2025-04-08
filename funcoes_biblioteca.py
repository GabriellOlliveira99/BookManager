import json

# Definindo o nome do arquivo JSON da biblioteca
biblioteca_arquivo = "biblioteca.json"

# Função para carregar a biblioteca do arquivo JSON
def carregar_biblioteca():
    try:
        with open("biblioteca.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            return dados.get("biblioteca", [])  # Retorna a lista de livros
    except FileNotFoundError:
        print("A biblioteca ainda não foi criada.")
        return []
    except json.JSONDecodeError:
        print("Erro ao ler a biblioteca. O arquivo pode estar corrompido.")
        return []

# Função para salvar a biblioteca no arquivo JSON
def salvar_biblioteca(biblioteca):
    with open(biblioteca_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump({"biblioteca": biblioteca}, arquivo, indent=4, ensure_ascii=False)

# Função para listar livros por status
# Essa função pode ser chamada com ou sem o parâmetro 'status'
# Se 'status' for None, ela lista todos os livros
# Se 'status' for "Disponível" ou "Emprestado", ela lista apenas os livros com esse status
def listar_livros_por_status(status=None):
    biblioteca = carregar_biblioteca()

    if biblioteca:
        if status:
            livros_filtrados = [livro for livro in biblioteca if livro.get('status', '').strip().lower() == status.lower()]
        else:
            livros_filtrados = biblioteca

        if livros_filtrados:
            print(f"\n=== Livros na Biblioteca (Status: {status if status else 'Todos'}) ===")
            for idx, livro in enumerate(livros_filtrados, start=1):
                print(f"{idx}.")
                print(f"   ID: {livro.get('id', 'Desconhecido')}")
                print(f"   Título: {livro.get('titulo', 'Desconhecido')}")
                print(f"   Autor: {livro.get('autor', 'Desconhecido')}")
                print(f"   Gênero: {livro.get('genero', 'Desconhecido')}")
                print(f"   Status: {livro.get('status', 'Desconhecido')}")
                print(f"   Ano de Publicação: {livro.get('ano_publicacao', 'Desconhecido')}")
                print(f"   Páginas: {livro.get('paginas', 'Desconhecido')}")
                print("-" * 40)
        else:
            print(f"Nenhum livro encontrado com o status '{status}'.")
    else:
        print("A biblioteca está vazia.")

# Função para listar todos os livros
def listar_livros():
    listar_livros_por_status() 

# Função para listar livros disponíveis
def listar_livros_disponiveis():
    listar_livros_por_status(status="Disponível")

# Função para listar livros emprestados
def listar_livros_emprestados():
    listar_livros_por_status(status="Emprestado")

# Função para adicionar um livro na biblioteca JSON
def adicionar_livro(livro):
    biblioteca = carregar_biblioteca()  
    biblioteca.append(livro)  
    salvar_biblioteca(biblioteca) 
    print(f"Livro '{livro.get('titulo', 'Desconhecido')}' adicionado com sucesso!")

# Função para deletar um livro da biblioteca JSON
def deletar_livro(id_livro):
    biblioteca = carregar_biblioteca()  
    livro_encontrado = False

    # Filtra os livros para remover o livro com o ID especificado
    biblioteca = [livro for livro in biblioteca if livro.get("id") != id_livro]

    salvar_biblioteca(biblioteca)  # Salva a lista atualizada
    print(f"Livro com ID {id_livro} deletado com sucesso!")

# Função para empréstimo de livro da biblioteca JSON
def emprestar_livro(id_livro):
    biblioteca = carregar_biblioteca()
    livro_encontrado = False

    for livro in biblioteca:
        if livro.get("id") == id_livro:
            livro["status"] = "Emprestado"
            livro_encontrado = True
            break

    if livro_encontrado:
        salvar_biblioteca(biblioteca) 
        print(f"Livro com ID {id_livro} emprestado com sucesso!")
    else:
        print(f"Livro com ID {id_livro} não encontrado na biblioteca.")

#Função para devolução de livro da biblioteca JSON
def devolver_livro(id_livro):
    biblioteca = carregar_biblioteca() 
    livro_encontrado = False

    for livro in biblioteca:
        if livro.get("id") == id_livro:
            livro["status"] = "Disponível"
            livro_encontrado = True
            break

    if livro_encontrado:
        salvar_biblioteca(biblioteca)
        print(f"Livro com ID {id_livro} devolvido com sucesso!")
    else:
        print(f"Livro com ID {id_livro} não encontrado na biblioteca.")


