create database registrodeatendimentoRA;
use registrodeatendimentoRA;

CREATE TABLE tipo_usuarios (
    idTipo_usuario INT PRIMARY KEY NOT NULL auto_increment,
    nomeTipo_usuario VARCHAR(150) NOT NULL
);
create table usuarios ( 
cpf_usuario varchar (11) primary key not null, 
nome varchar (150) not null,
fk_tipo_usuario int not null,
foreign key (fk_tipo_usuario) references tipo_usuarios(idTipo_usuario)
);


CREATE TABLE servidores (
    cpf_servidor VARCHAR(11) PRIMARY KEY NOT NULL,
    nome VARCHAR(150) NOT NULL,
    senha VARCHAR(40)
);

CREATE TABLE status_senhas (
    idStatus_senha INT PRIMARY KEY NOT NULL auto_increment, 
    nomeStatus_senha VARCHAR(150) NOT NULL
);

CREATE TABLE senhas (
    idSenha VARCHAR(20) PRIMARY KEY NOT NULL, 
    fk_Status_senha INT,
    FOREIGN KEY (fk_Status_senha) REFERENCES status_senhas(idStatus_senha)
);

CREATE TABLE tipo_atendimento (
    id_tipoAtendimento INT PRIMARY KEY auto_increment,
    nomeTipoAtendimento VARCHAR(150)
);

create table atendimentos (
idAtendimento int primary key not null auto_increment,
 	comecoAtendimento TIMESTAMP,
 	finalAtendimento TIMESTAMP,
 	guiche int,
fk_cpf_usuario varchar (11),
 	fk_tipo_atendimento int,
fk_cpf_servidor varchar (11),
fk_idSenha varchar (20),
foreign key (fk_cpf_usuario) references usuarios (cpf_usuario),
foreign key (fk_cpf_servidor) references servidores (cpf_servidor),
foreign key (fk_idSenha) references senhas(idSenha),
foreign key (fk_tipo_atendimento) references tipo_atendimento (id_tipoAtendimento)
);

/*Inserção de dados na tabela tipo_Atendimento:*/
insert into tipo_atendimento (nomeTipoAtendimento) values ("Emissão de declaração");
insert into tipo_atendimento (nomeTipoAtendimento) values ("Trancamento de matrícula");
insert into tipo_atendimento (nomeTipoAtendimento) values ("Emissão de carteirinha");
insert into tipo_atendimento (nomeTipoAtendimento) values ("Emissão de históricos");
insert into tipo_atendimento (nomeTipoAtendimento) values ("Registro acadêmico");
insert into tipo_atendimento (nomeTipoAtendimento) values ("Trancamento de disciplina");
insert into tipo_atendimento (nomeTipoAtendimento) values ("Emissão de diplomas");
insert into tipo_atendimento (nomeTipoAtendimento) values ("Processo Seletivo");
insert into tipo_atendimento (nomeTipoAtendimento) values ("Elaboração de relatórios");

/*insert into tipo_usuarios (nomeTipo_usuario) values ("Aluno de Ensino Médio");*/
insert into tipo_usuarios (nomeTipo_usuario) values ("Aluno de Ensino Técnico");
insert into tipo_usuarios (nomeTipo_usuario) values ("Aluno de Graduação");
insert into tipo_usuarios (nomeTipo_usuario) values ("Aluno de Pós-Graduação");
insert into tipo_usuarios (nomeTipo_usuario) values ("Ex-aluno");
insert into tipo_usuarios (nomeTipo_usuario) values ("Ainda não é estudante");

/*Inserção de dados na tabela status_Senhas: */
insert into status_Senhas (nomeStatus_senha) values ("Na fila");
insert into status_Senhas (nomeStatus_senha) values ("Atendida");
insert into status_Senhas (nomeStatus_senha) values ("Não atendida");

