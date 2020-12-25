create database  if not exists accounts;
USE accounts;
drop table if exists addresses;
drop table if exists users;
create table if not exists users(
user_id INT PRIMARY KEY AUTO_INCREMENT,
user_password VARCHAR(255) NOT NULL
);

create table addresses
(
address_id INT PRIMARY KEY AUTO_INCREMENT,
user_id INT NOT NULL,
street VARCHAR(255),
pin_code CHAR(6),
state VARCHAR(50),
phone_no VARCHAR(50),
FOREIGN KEY fk_addresses_users(user_id)
	references users(user_id)
		on update cascade
        on delete no action

)
