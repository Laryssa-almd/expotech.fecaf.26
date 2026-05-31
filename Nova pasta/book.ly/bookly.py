import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2007",
    database="db_livros"
)

cursor = conexao.cursor()


# ===== FUNÇÕES =====

def cadastrar_usuario():
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")

    sql = """
    INSERT INTO tbl_usuarios (nome_usuario, email_usuario, senha_usuario)
    VALUES (%s, %s, %s)
    """
    cursor.execute(sql, (nome, email, senha))
    conexao.commit()

    print("Usuário cadastrado!\n")


def cadastrar_autor():
    nome = input("Nome do autor: ")

    sql = "INSERT INTO tbl_autores (nome_autor) VALUES (%s)"
    cursor.execute(sql, (nome,))
    conexao.commit()

    print("Autor cadastrado!\n")


def cadastrar_categoria():
    nome = input("Nome da categoria: ")

    sql = "INSERT INTO tbl_categorias (nome_categoria) VALUES (%s)"
    cursor.execute(sql, (nome,))
    conexao.commit()

    print("Categoria cadastrada!\n")


def cadastrar_livro():
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    ano = int(input("Ano: "))
    id_autor = int(input("ID do autor: "))
    id_categoria = int(input("ID da categoria: "))

    sql = """
    INSERT INTO tbl_livros
    (titulo_livro, descricao_livro, ano_livro, fk_autor_livro, fk_categoria_livro)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (titulo, descricao, ano, id_autor, id_categoria))
    conexao.commit()

    print("Livro cadastrado!\n")


def listar_livros():
    sql = """
    SELECT
    tbl_livros.id_livro,
    tbl_livros.titulo_livro,
    tbl_autores.nome_autor,
    tbl_categorias.nome_categoria
    FROM tbl_livros
    JOIN tbl_autores
    ON tbl_livros.fk_autor_livro = tbl_autores.id_autor
    JOIN tbl_categorias
    ON tbl_livros.fk_categoria_livro = tbl_categorias.id_categoria
    """

    cursor.execute(sql)
    resultados = cursor.fetchall()

    print("\n=== LIVROS CADASTRADOS ===")

    for livro in resultados:
        print(
            f"ID: {livro[0]} | "
            f"Título: {livro[1]} | "
            f"Autor: {livro[2]} | "
            f"Categoria: {livro[3]}"
        )

    print()


def deletar_livro():
    listar_livros()

    livro_id = input("Digite o ID do livro que deseja deletar: ")

    sql = "DELETE FROM tbl_livros WHERE id_livro = %s"

    cursor.execute(sql, (livro_id,))
    conexao.commit()

    print("Livro deletado com sucesso!\n")

def deletar_autor():
    listar_autores()
    autor_id = input("Digite o ID do autor que deseja deletar: ")

    sql = "DELETE FROM tbl_autores WHERE id_autor = %s"

    cursor.execute(sql, (autor_id,))
    conexao.commit()

    print("Autor deletado com sucesso!\n")

def deletar_categoria():
    categoria_id = input("Digite o ID da categoria que deseja deletar: ")

    sql = "DELETE FROM tbl_categorias WHERE id_categoria = %s"

    cursor.execute(sql, (categoria_id,))
    conexao.commit()

    print("Categoria deletada com sucesso!\n")

def atualizar_livro():
    listar_livros()

    livro_id = input("Digite o ID do livro que deseja atualizar: ")

    novo_titulo = input("Novo título: ")
    nova_descricao = input("Nova descrição: ")
    novo_ano = int(input("Novo ano: "))
    novo_autor = int(input("Novo ID do autor: "))
    nova_categoria = int(input("Novo ID da categoria: "))

    sql = """
    UPDATE tbl_livros
    SET
    titulo_livro = %s,
    descricao_livro = %s,
    ano_livro = %s,
    fk_autor_livro = %s,
    fk_categoria_livro = %s
    WHERE id_livro = %s
    """

    valores = (
        novo_titulo,
        nova_descricao,
        novo_ano,
        novo_autor,
        nova_categoria,
        livro_id
    )

    cursor.execute(sql, valores)
    conexao.commit()

    print("Livro atualizado com sucesso!\n")

def atualizar_autor():
    listar_autores()
    autor_id = input("Digite o ID do autor que deseja atualizar: ")

    novo_nome = input("Novo nome: ")

    sql = """
    UPDATE tbl_autores
    SET
    nome_autor = %s,
    WHERE id_autor = %s
    """

    valor = (novo_nome)

    
    print("Autor atualizado com sucesso!\n")

def listar_autores():
    sql = """
    SELECT id_autor, nome_autor
    FROM tbl_autores
    """

    cursor.execute(sql)
    resultados = cursor.fetchall()

    print("\n=== AUTORES CADASTRADOS ===")

    for autor in resultados:
        print(
            f"ID: {autor[0]} | "
            f"Nome: {autor[1]}"
        )

    print()


# ===== MENU =====

while True:
    print("===== SISTEMA DE LIVROS =====")
    print("1 - Cadastrar usuário")
    print("2 - Cadastrar autor")
    print("3 - Cadastrar categoria")
    print("4 - Cadastrar livro")
    print("5 - Listar livros")
    print("6 - Deletar livro")
    print("7 - Atualizar livro")
    print("8 - Deletar autor")
    print("9 - Deletar categoria")
    print("10 - Atualizar autores")
    print("11 - Listar autores")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_usuario()

    elif opcao == "2":
        cadastrar_autor()

    elif opcao == "3":
        cadastrar_categoria()

    elif opcao == "4":
        cadastrar_livro()

    elif opcao == "5":
        listar_livros()

    elif opcao == "6":
        deletar_livro()

    elif opcao == "7":
        atualizar_livro()

    elif opcao == "8":
        deletar_autor()

    elif opcao == "9":
        deletar_categoria()

    elif opcao == "10":
        atualizar_autor()

    elif opcao == "11":
        listar_autores()

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!\n")