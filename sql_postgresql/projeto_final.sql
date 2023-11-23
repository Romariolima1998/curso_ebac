select count(*) total_de_clientes from customer;

select name clientes_que_nao_compraram from customer where customer_id not in 
(select customer_id from customer_order);

select name produto_mais_vendido, sum(quantity) or from product 
inner join order_item
on product.product_id = order_item.product_id 
group by name 
order by sum(quantity) asc ;