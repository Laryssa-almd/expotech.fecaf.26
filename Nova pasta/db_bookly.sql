/*CREATE DATABASE db_livros;*/
USE db_livros;

/*CREATE TABLE tbl_usuarios (
id_usuario INT AUTO_INCREMENT PRIMARY KEY,
nome_usuario VARCHAR(100),
email_usuario VARCHAR(100),
senha_usuario VARCHAR(100)
);

CREATE TABLE tbl_autores (
id_autor INT AUTO_INCREMENT PRIMARY KEY,
nome_autor VARCHAR(100)
);

CREATE TABLE tbl_categorias (
id_categoria INT AUTO_INCREMENT PRIMARY KEY,
nome_categoria VARCHAR(100)
);

CREATE TABLE tbl_livros (
id_livro INT AUTO_INCREMENT PRIMARY KEY,
titulo_livro VARCHAR(100),
descricao_livro VARCHAR(300),
ano_livro INT,
fk_autor_livro INT,
fk_categoria_livro INT
);

ALTER TABLE tbl_livros ADD CONSTRAINT
FOREIGN KEY (fk_autor_livro)
REFERENCES tbl_autores(id_autor);

ALTER TABLE tbl_livros ADD CONSTRAINT
FOREIGN KEY (fk_categoria_livro)
REFERENCES tbl_categorias(id_categoria);*/

SELECT * FROM tbl_categorias;
