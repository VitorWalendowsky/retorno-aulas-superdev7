drop database if exists perifericos;
create database perifericos;
use perifericos;

CREATE TABLE monitores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    polegadas INT NOT NULL,
    frequencia INT NOT NULL,
    preco DECIMAL(10,2) NOT NULL
);

select * from monitores;


CREATE TABLE notebooks (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    polegadas DECIMAL(4,1) NOT NULL,
    quantidade_ram INT NOT NULL,
    processador VARCHAR(100) NOT NULL,
    placa_video VARCHAR(100) NOT NULL,
    rgb BOOLEAN NOT NULL,
    peso DECIMAL(5,2) NOT NULL,
    ssd BOOLEAN NOT NULL,
    preco DECIMAL(10,2) NOT NULL
);

select * from notebooks;


CREATE TABLE teclado (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    tipo_conexao VARCHAR(100) NOT NULL,
    cor VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL
);

select * from teclado;


CREATE TABLE mouse (
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	dpi INT NOT NULL,
	modelo VARCHAR(100) NOT NULL,
	rgb BOOLEAN NOT NULL,
	quantidade_botao INT NOT NULL,
	preco DECIMAL(10,2) NOT NULL
);

select * from mouse;



