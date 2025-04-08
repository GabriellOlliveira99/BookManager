# Book Manager 📚

Este é um projeto prático desenvolvido por **Gabriel Oliveira** para consolidar conhecimentos em Python. O objetivo do projeto é criar um sistema de gerenciamento de livros que permite listar, adicionar, deletar, emprestar e devolver livros, utilizando um arquivo JSON como banco de dados.

## 📋 Funcionalidades

- **Listar livros completos**: Exibe todos os livros cadastrados na biblioteca.
- **Listar livros disponíveis**: Mostra apenas os livros que estão disponíveis para empréstimo.
- **Listar livros emprestados**: Mostra os livros que estão atualmente emprestados.
- **Adicionar livro**: Permite adicionar um novo livro à biblioteca.
- **Deletar livro**: Remove um livro da biblioteca com base no ID.
- **Empréstimo de livro**: Marca um livro como emprestado.
- **Devolução de livro**: Marca um livro como disponível novamente.

## 🛠️ Estrutura do Projeto

### Arquivos principais:

- **`app.py`**: Contém o menu principal e a lógica de interação com o usuário.
- **`biblioteca.json`**: Armazena os dados da biblioteca, como título, autor, status, etc.
- **`funcoes_biblioteca.py`**: Contém as funções para manipular os dados da biblioteca, como carregar, salvar, listar, adicionar, deletar, emprestar e devolver livros.

## 🚀 Como executar o projeto

1. Certifique-se de ter o Python instalado em sua máquina (versão 3.6 ou superior).
2. Clone este repositório ou baixe os arquivos.
3. No terminal, navegue até o diretório do projeto.
4. Execute o arquivo `app.py` com o comando:

   ```bash
   python app.py
   
6. Siga as instruções exibidas no menu para interagir com o sistema.

## 📂 Exemplo de `biblioteca.json`

O arquivo `biblioteca.json` armazena os dados da biblioteca no seguinte formato:

```json
{
    "biblioteca": [
        {
            "id": 1,
            "titulo": "Dom Quixote",
            "autor": "Miguel de Cervantes",
            "genero": "Romance",
            "status": "Disponível",
            "ano_publicacao": 1605,
            "paginas": 863
        }
    ]
}
```

## 💡 Dicas e Sugestões
Se você tiver alguma sugestão de melhoria ou encontrar algum problema no projeto, sinta-se à vontade para entrar em contato ou abrir uma issue (caso esteja utilizando um repositório Git).

Sugestões de melhorias futuras:

- Implementar uma interface gráfica para o sistema.
- Adicionar autenticação para diferentes usuários (administradores e leitores).
- Permitir busca de livros por título, autor ou gênero.
- Adicionar suporte a múltiplos arquivos JSON para diferentes bibliotecas.


