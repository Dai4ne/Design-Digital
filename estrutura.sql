CREATE DATABASE universidade_veritas;

USE universidade_veritas;

CREATE TABLE contatos (
    id INT PRIMARY KEY AUTO_INCREMENT not null,
    email varchar(120) not null,
    assunto varchar(120) not null,
    descricao text not null,
    nome varchar(100) not null
);