product client estoque
CREATE SCHEMA store;

create table "store".customer (
    id serial,
    name varchar(50) not null,
    cpf varchar(30),
    email varchar(50) not null,
    unique (id, email),

);


create table "store".product (
    id serial,
    name varchar(50) not null,
    value int not null,
    description text,
    unique (id)
);
        

create table "store".stock (
    id serial,
    name varchar(50) not null,
    amount int not null,
    unique (id, name)
);