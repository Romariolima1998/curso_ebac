como juntar duas tabelas com inner join
select customer.name, customer.email, costumer_order.value 
from 
customer
inner join costumer_order 
on customer.id = costumer_order.id_customer;

filtrando dados com inner join
select customer.name, customer.email, costumer_order.value 
from 
customer
inner join costumer_order 
on customer.id = costumer_order.id_customer 
where
customer.email = 'diego@email.com' ;
