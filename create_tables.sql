create table users
(
user_id int(5) PRIMARY KEY AUTO_INCREMENT,
username VARCHAR(20),
email VARCHAR(35),
password VARCHAR(80)
);

create table recipes
(
recipe_id int(5) PRIMARY KEY AUTO_INCREMENT,
recipe_name VARCHAR(70),
ingredients TEXT,
instructions TEXT,
serving_size VARCHAR(20),
category VARCHAR(30),
notes TEXT,
date_added DATE,
date_modified DATE
);