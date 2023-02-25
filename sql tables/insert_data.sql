use retail_db_prueba;

SHOW VARIABLES WHERE `Variable_name` = 'secure_file_priv';

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/customers/customers.csv'
INTO TABLE customer FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n';

select * from customer;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/categories/categories.csv'
INTO TABLE categories FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n';

select * from categories;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/departments/departments.csv'
INTO TABLE departments FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n';

select * from departments;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/order_items/order_items.csv'
INTO TABLE order_items FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n';

select * from order_items;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/orders/orders.csv'
INTO TABLE orders FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n';

select * from orders;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/products/products.csv'
INTO TABLE products FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n';

select * from products;






