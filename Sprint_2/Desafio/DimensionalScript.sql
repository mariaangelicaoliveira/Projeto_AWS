-- modelo Dimensional 



---- tabela vendedor
	 
CREATE TABLE tb_vendedor_d (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255),
    sexo SMALLINT,
    estado_nome VARCHAR(255)    
);
INSERT INTO tb_vendedor_d (id, nome, sexo, estado_nome)
SELECT idVendedor AS id,
	nomeVendedor AS nome,
	sexoVendedor  AS sexo,
	estadoVendedor AS estado_nome
FROM tb_locacao
GROUP BY tb_locacao.idVendedor;

SELECT * FROM tb_vendedor_d
	  
---- tabela carro 

CREATE TABLE tb_carro_d (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    km VARCHAR(255),
    chassi VARCHAR,
    marca VARCHAR(255),
    modelo VARCHAR(255),
    ano VARCHAR(255),
    combustivel_nome INTEGER
);

INSERT INTO tb_carro_d (id, km, chassi, marca, modelo, ano, combustivel_nome)
SELECT idCarro  AS id,
	kmCarro  AS km,
	classiCarro  AS chassi,
	marcaCarro  AS marca,
	modeloCarro  AS modelo,
	anoCarro AS ano,
	tipoCombustivel AS combustivel_nome
FROM tb_locacao
GROUP BY tb_locacao.idCarro;

SELECT * FROM tb_carro_d 

---- tabela cliente
	 
CREATE TABLE tb_cliente_d (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255),
    cidade_nome VARCHAR(255),
    estado_nome VARCHAR(255),
    pais_nome VARCHAR(255)
);

INSERT INTO tb_cliente_d (id, nome, cidade_nome, estado_nome, pais_nome)
SELECT idCliente AS id,
	nomeCliente AS nome,
	cidadeCliente AS cidade_nome,
	estadoCliente AS estado_nome,
	paisCliente AS pais_nome	
FROM tb_locacao
GROUP BY tb_locacao.idCliente;

select * from tb_cliente_d
	 

---- tabela locacao
	 
CREATE TABLE tb_locar_d (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    id_carro INTEGER NOT NULL,
    id_vendedor INTEGER NOT NULL,
    dt_locacao DATETIME NOT NULL,
    hr_locacao TIME NOT NULL,
    qtn_diaria INTEGER NOT NULL,
    vlr_diaria DECIMAL NOT NULL,
    dt_entrega DATETIME NOT NULL,
    hr_entrega TIME NOT NULL,    
    FOREIGN KEY (id_cliente) REFERENCES tb_cliente_d(id),
    FOREIGN KEY (id_carro) REFERENCES tb_carro_d(id),
    FOREIGN KEY (id_vendedor) REFERENCES tb_vendedor_d(id)
);

INSERT INTO tb_locar_d (id, id_cliente, id_carro, id_vendedor, dt_locacao, hr_locacao, qtn_diaria, vlr_diaria, dt_entrega, hr_entrega)
SELECT idLocacao  AS id,
	idCliente AS id_cliente,
	idCarro AS id_carro,
	idVendedor AS id_vendedor,
	dataLocacao AS dt_locacao,
	horaLocacao AS hr_locaco,
	qtdDiaria AS qtn_diaria,
	vlrDiaria AS vlr_diaria,
	dataEntrega AS dt_entrega,
	horaEntrega AS hr_entrega
FROM tb_locacao
GROUP BY tb_locacao.idLocacao;

select * from tb_locar_d

---- View alguel por marca
CREATE VIEW vw_aluguel_marca AS
SELECT tb_carro_d.marca, COUNT(tb_locar_d.id) AS aluguel FROM tb_locar_d LEFT JOIN tb_carro_d ON tb_carro_d.id == tb_locar_d.id_carro GROUP BY tb_carro_d.marca

---- View alguel por Vendedor
CREATE VIEW vw_aluguel_vendedor AS
SELECT tb_vendedor_d.nome, COUNT(tb_locar_d.id) AS aluguel FROM tb_locar_d LEFT JOIN tb_vendedor_d ON tb_vendedor_d.id == tb_locar_d.id_vendedor GROUP BY tb_vendedor_d.id 

---- View dias alugados
CREATE VIEW vw_dia_aluguel AS
SELECT COUNT(tb_locar_d.id) AS quantidade, tb_locar_d.qtn_diaria AS diarias FROM tb_locar_d GROUP BY tb_locar_d.qtn_diaria 

---- View alugueis por estado
CREATE VIEW vw_aluguel_estado AS
SELECT tb_cliente_d.estado_nome, COUNT(tb_locar_d.id) AS quantidade FROM tb_locar_d LEFT JOIN tb_cliente_d ON tb_cliente_d.id == tb_locar_d.id_cliente GROUP BY tb_cliente_d.estado_nome 

