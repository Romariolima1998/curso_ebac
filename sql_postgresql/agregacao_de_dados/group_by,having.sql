agrupa deixando apenas um dado de cada

select id_customer from costumer_order 
group by id_customer;


vai agregrar os dados de uma coluna e somar a outra sum

select id_customer, sum(value) as total_value from costumer_order 
group by id_customer;

filtrando

select id_customer, sum(value) as total_value from costumer_order 
group by id_customer having sum(value) > 100;

# com inner join

select name, sum(costumer_order.value) total_value from costumer_order 
inner join customer using (id)
group by name;