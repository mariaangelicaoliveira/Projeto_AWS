	-- select * from tb_carro INNER JOIN tb_combustivel ON tb_combustivel.id == tb_carro.id_combustivel  
	-- select * from tb_combustivel 
	-- select * from tb_vendedor


-- modelo relacional 

----- tabela combustivel 

CREATE TABLE tb_combustivel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255)
);
INSERT INTO tb_combustivel (id, nome)
SELECT idcombustivel AS id,
		   tipoCombustivel AS nome
	  FROM tb_locacao
	  GROUP BY idcombustivel;
	 
	 
SELECT * FROM tb_combustivel 


----- tabela estado 

CREATE TABLE tb_estado (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255), 
    pais VARCHAR(255)
);

CREATE VIEW vw_estado AS 
SELECT estadoCliente AS estado,
       paisCliente AS pais 
       FROM tb_locacao
       GROUP BY estadoCliente;
      
INSERT INTO tb_estado (nome, pais)
SELECT estado, pais FROM vw_estado;

SELECT * FROM tb_estado 

---- tabela cidade

CREATE TABLE tb_cidade (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255),
    id_estado INTEGER, 
    FOREIGN KEY (id_estado) REFERENCES tb_estado(id)
);


INSERT INTO tb_cidade (nome, id_estado)
SELECT cidadeCliente AS nome,
	(SELECT tb_estado.id FROM tb_estado WHERE tb_estado.nome LIKE tb_locacao.estadoCliente  ) AS id_estado
	  FROM tb_locacao
	  GROUP BY cidadeCliente;
	 
SELECT * FROM tb_cidade INNER JOIN tb_estado ON tb_estado.id = tb_cidade.id_estado


---- tabela vendedor
	 
CREATE TABLE tb_vendedor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255),
    sexo SMALLINT,
    id_estado VARCHAR(255),
    FOREIGN KEY (id_estado) REFERENCES tb_estado(id)
    
);
INSERT INTO tb_vendedor (id, nome, sexo, id_estado)
SELECT idVendedor AS id,
	nomeVendedor AS nome,
	sexoVendedor  AS sexo,
	(SELECT tb_estado.id FROM tb_estado WHERE tb_estado.nome LIKE tb_locacao.estadoCliente) AS id_estado
	  FROM tb_locacao
	  GROUP BY tb_locacao.idVendedor;

SELECT * FROM tb_vendedor INNER JOIN tb_estado ON tb_estado.id == tb_vendedor.id_estado
---- tabela marca
CREATE TABLE tb_marca (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255)
);

INSERT INTO tb_marca (nome)
SELECT marcaCarro AS nome
	  FROM tb_locacao
	  GROUP BY marcaCarro;
	 
SELECT * FROM tb_marca;

---- tabela modelo

CREATE TABLE tb_modelo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255),
    id_marca INTEGER NOT NULL, 
    FOREIGN KEY (id_marca) REFERENCES tb_marca(id)
);


INSERT INTO tb_modelo (nome, id_marca)
SELECT modeloCarro AS nome,
	(SELECT tm.id FROM tb_marca AS tm  WHERE tm.nome LIKE tb_locacao.marcaCarro) AS id_marca
	  FROM tb_locacao
	  GROUP BY modeloCarro;
	 
SELECT * FROM tb_modelo INNER JOIN tb_marca ON tb_marca.id == tb_modelo.id
SELECT * FROM tb_locacao 
	LEFT JOIN tb_modelo  ON tb_modelo.nome == tb_locacao.modeloCarro 
	LEFT JOIN tb_marca ON tb_marca.nome == tb_locacao.marcaCarro 
	

---- tabela carro 

CREATE TABLE tb_carro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    km VARCHAR(255),
    chassi VARCHAR,
    ano VARCHAR(255),
    id_combustivel INTEGER,
    id_modelo INTEGER,
    FOREIGN KEY (id_combustivel) REFERENCES tb_combustivel(id)
    FOREIGN KEY (id_modelo) REFERENCES tb_modelo(id)
);

INSERT INTO tb_carro (id, km, chassi, ano, id_combustivel, id_modelo)
SELECT idCarro  AS id,
	kmCarro  AS km,
	classiCarro  AS chassi,	
	anoCarro AS ano,
	idcombustivel AS id_combustivel,
	(SELECT tb_modelo.id FROM tb_modelo WHERE tb_modelo.nome LIKE modeloCarro) AS id_modelo
FROM tb_locacao
GROUP BY tb_locacao.idCarro;

SELECT * FROM tb_carro 

---- tabela cliente
	 
CREATE TABLE tb_cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255),
    id_cidade INTEGER,
    FOREIGN KEY (id_cidade) REFERENCES tb_cidade(id)
);

INSERT INTO tb_cliente (id, nome, id_cidade)
SELECT idCliente AS id,
	nomeCliente AS nome,
	(SELECT tb_cidade.id FROM tb_cidade WHERE tb_cidade.nome LIKE tb_locacao.cidadeCliente)  AS id_cidade	
FROM tb_locacao
GROUP BY tb_locacao.idCliente;

select * from tb_cliente INNER JOIN tb_cidade AS tc ON tc.id == tb_cliente.id_cidade INNER JOIN tb_estado AS te ON te.id == tc.id_estado 
	 

---- tabela cliente
	 
CREATE TABLE tb_locar (
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
    FOREIGN KEY (id_cliente) REFERENCES tb_cliente(id),
    FOREIGN KEY (id_carro) REFERENCES tb_carro(id),
    FOREIGN KEY (id_vendedor) REFERENCES tb_vendedor(id)
);

INSERT INTO tb_locar (id, id_cliente, id_carro, id_vendedor, dt_locacao, hr_locacao, qtn_diaria, vlr_diaria, dt_entrega, hr_entrega)
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

select * from tb_locar

