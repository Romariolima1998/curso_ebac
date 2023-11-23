para tornar uma coluna primary key
alter table customer add primary key (id);


para adicionar uma foreign key
alter table costumer_order add constraint fk_order_costumer foreign key (id_customer) 
references customer (id);
