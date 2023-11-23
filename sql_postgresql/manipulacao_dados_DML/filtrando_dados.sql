para fazer select com beetwin
select * from customer where name in ('romario', 'diego');

para fazer uma busca em duas tabelas
select * from costumer_order where user_email_order in 
(select email from customer);