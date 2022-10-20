/*Apaga os relacionamentos*/
ALTER TABLE LABDATABASE.TELEFONES DROP CONSTRAINT CLIENTES_TELEFONES_FK;
ALTER TABLE LABDATABASE.ENDERECOS DROP CONSTRAINT CLIENTES_ENDERECOS_FK;
ALTER TABLE LABDATABASE.ORDENSSERVICOS DROP CONSTRAINT CLIENTES_ORDENSSERVICOS_FK;
ALTER TABLE LABDATABASE.SERVICOS DROP CONSTRAINT ORDENSSERVICOS_SERVICOS_FK;

/*Apaga as tabelas*/
DROP TABLE CLIENTES;
DROP TABLE ORDENSSERVICOS;
DROP TABLE SERVICOS;
DROP TABLE ENDERECOS;
DROP TABLE TELEFONES;

/*Apaga as sequences*/
DROP SEQUENCE LABDATABASE.CLIENTES_CODCLIENTE_SEQ;
DROP SEQUENCE LABDATABASE.SERVICOS_CODS_ERVICO_SEQ;
DROP SEQUENCE LABDATABASE.ORDENSSERVICOS_COD_ORDEMSERVICO_SEQ;

/*Cria as tabelas*/
CREATE TABLE CLIENTES (
                CODCLIENTE INTEGER NOT NULL,
                NOME VARCHAR(100) NOT NULL,
                CONSTRAINT CLIENTES_PK PRIMARY KEY (CODCLIENTE)
);


CREATE TABLE ORDENSSERVICOS (
                CODCLIENTE INTEGER NOT NULL,
                COD_ORDEMSERVICO VARCHAR(100) NOT NULL,
                DT_ABERTURA VARCHAR(8) NOT NULL,
                DT_PREV_ATENDIMENTO VARCHAR(8) NOT NULL,
                DT_EFET_ATENDIMENTO VARCHAR(8) NOT NULL,
                CONSTRAINT ORDENSSERVICOS_PK PRIMARY KEY (CODCLIENTE, COD_ORDEMSERVICO)
);


CREATE TABLE ENDERECOS (
                CODCLIENTE INTEGER NOT NULL,
                CEP VARCHAR(8) NOT NULL,
                lOGRADOURO VARCHAR(100) NOT NULL,
                MUNICIPIO VARCHAR(30) NOT NULL,
                UF VARCHAR(2) NOT NULL,
                NUMERO VARCHAR(15) NOT NULL,
                COMPLEMENTO VARCHAR(25),
                CONSTRAINT ENDERECOS_PK PRIMARY KEY (CODCLIENTE)
);



CREATE TABLE TELEFONES (
                CODCLIENTE INTEGER NOT NULL,
                NUMERO VARCHAR(15) NOT NULL,
                TIPO_TELEFONE VARCHAR(30) NOT NULL,
                CONSTRAINT TELEFONES_PK PRIMARY KEY (CODCLIENTE)
);

CREATE TABLE SERVICOS (
                CODCLIENTE INTEGER NOT NULL,
                COD_ORDEMSERVICO VARCHAR(100) NOT NULL,
                COD_SERVICO VARCHAR(10) NOT NULL,
                NOME VARCHAR(100) NOT NULL,
                CAT VARCHAR(30) NOT NULL,
                VLR_UNITARIO VARCHAR(100) NOT NULL,
                TEMPO_EXECUO VARCHAR(100) NOT NULL,
                GARANTIA VARCHAR(100) NOT NULL,
                CONSTRAINT SERVICOS_PK PRIMARY KEY (CODCLIENTE, COD_ORDEMSERVICO, COD_SERVICO)
);

/*Cria as sequences*/
CREATE SEQUENCE LABDATABASE.CLIENTES_CODCLIENTE_SEQ;
CREATE SEQUENCE LABDATABASE.SERVICOS_CODS_ERVICO_SEQ;
CREATE SEQUENCE LABDATABASE.ORDENSSERVICOS_COD_ORDEMSERVICO_SEQ;

/*Cria os relacionamentos*/
ALTER TABLE TELEFONES ADD CONSTRAINT CLIENTES_TELEFONES_FK
FOREIGN KEY (CODCLIENTE)
REFERENCES CLIENTES (CODCLIENTE)
NOT DEFERRABLE;

ALTER TABLE ENDERECOS ADD CONSTRAINT CLIENTES_ENDERECOS_FK
FOREIGN KEY (CODCLIENTE)
REFERENCES CLIENTES (CODCLIENTE)
NOT DEFERRABLE;

ALTER TABLE ORDENSSERVICOS ADD CONSTRAINT CLIENTES_ORDENSSERVICOS_FK
FOREIGN KEY (CODCLIENTE)
REFERENCES CLIENTES (CODCLIENTE)
NOT DEFERRABLE;

ALTER TABLE SERVICOS ADD CONSTRAINT ORDENSSERVICOS_SERVICOS_FK
FOREIGN KEY (CODCLIENTE, COD_ORDEMSERVICO)
REFERENCES ORDENSSERVICOS (CODCLIENTE, COD_ORDEMSERVICO)
NOT DEFERRABLE;


