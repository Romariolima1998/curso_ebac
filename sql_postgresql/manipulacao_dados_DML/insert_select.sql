# para inserir valores
insert into customer (name, email, cpf) 
values(
    'romario',
    'romario@email.com',
    '111.222.333.44'
);

buscar dados
select * from customer;

# para buscar apenas uma coluna
select name from customer;

busca com where

select * from customer where name = 'romario';