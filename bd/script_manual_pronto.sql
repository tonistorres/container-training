create database dbrhxpe; 
use dbrhxpe;


create table empregados(
empregado_id int primary key auto_increment,
nome varchar(30),
sobrenome varchar(50),
salario decimal(8,2),
email varchar(50),
data_admissao date,
cargo_id int,
departamento_id int
);

create table cargos(
cargo_id int primary key auto_increment ,
cargo_nome varchar(50),
cargo_historico_id int
);



create table cargo_historico(
cargo_historico_id int primary key auto_increment,
data_inicio date,
data_fim date,
empregado_id int,
cargo_id int
);

create table departamentos(
departamento_id int primary key not null auto_increment,
departamento_nome varchar(50) not null,
localidade_id int
);

create table localidades(
lacalidade_id int primary key not null auto_increment,
cidade varchar(50),
estado varchar(50),
endereco varchar(100),
pais_id int
);



create table paises(
pais_id int primary key auto_increment,
pais varchar(50),
regiao_paises_id int
);


create table regioes(
regiao_id int primary key auto_increment,
regiao_nome varchar(50)
);



alter table empregados add constraint FK_EMP_DEPTO foreign key(departamento_id)
references departamentos(departamento_id);

alter table cargo_historico add constraint FK_CARGO_HISTO_EMP foreign key(empregado_id)
references empregados(empregado_id);

alter table empregados add constraint FK_EMP_CARGO foreign key(cargo_id)
references cargos(cargo_id);

alter table departamentos add constraint FK_DEPTO_LOCALIDADE foreign key(localidade_id)
references localidades(lacalidade_id);

alter table cargo_historico add constraint FK_CARGO_HISTO_CARGO foreign key(cargo_id)
references cargos(cargo_id);

alter table localidades add constraint FK_LOCALIDADES_PAISES foreign key(pais_id)
references paises(pais_id);


alter table paises add constraint FK_PAIS_REGIAO foreign key(regiao_paises_id)
references regioes(regiao_id);

