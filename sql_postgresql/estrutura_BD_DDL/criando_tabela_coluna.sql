# para criar uma tabela
create table "store".test();

para criar tabela com colunas
create table "store".customer (
    id serial,
    cpf varchar(30),
    email varchar(50) not null
    unique (email)
);

para adicionar tabela
alter table store.customer add name varchar(30);

# para excluir uma tabela
drop table "store".custumer;

# para remover uma colna da tabela
alter table store.customer drop name_32;