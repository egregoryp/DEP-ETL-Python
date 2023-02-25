use retail_db_prueba;
create table customer(customer_id int,customer_fname varchar(50), 
                      customer_lname varchar(50),customer_email varchar(50),
                      customer_password varchar(50),customer_street varchar(50),
                      customer_city varchar(50),customer_state varchar(50),
                      customer_zipcode varchar(50));
                      
create table orders(order_id int,order_date date,
                    order_customer_id int,order_status varchar(50));
                    
create table order_items(order_item_id int,order_item_order_id int,
			             order_item_product_id int,order_item_quantity int,
                         order_item_subtotal float,order_item_product_price float);                    
                    
create table products(product_id int,product_category_id int,
                      product_name varchar(150),product_description varchar(150),
                      product_price float, product_image varchar(150));    
                      
create table categories(category_id int,category_department_id int,
                        category_name varchar(50));
                        
create table departments(department_id int,
                         department_name varchar(50));                        
                      
                      
                      
                      