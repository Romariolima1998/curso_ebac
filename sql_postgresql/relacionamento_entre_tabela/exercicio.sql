create table product(
    id serial not null,
    name varchar(30) not null,
    brand varchar(30),
    value varchar(10),
    description text,
    primary key(id)
);



create table stock(
    product_id int not null,
    amount int not null,
    primary key(product_id),
    constraint fk_product_id foreign key 
    (product_id) references product (id)
);