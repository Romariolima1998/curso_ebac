alterar o tipo de campo da colunas
alter table customer alter column cpf type text;

para alterar para tipo numerico
alter table customer alter column cpf type int using cpf::integer;

para definir uma tabela como nao nulo
alter table customer alter column email set not null;

para adicionar constraint valor unico
alter table name_tabela add constraint name_unique unique (nome_coluna);