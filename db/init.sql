drop table if exists users;
create table users (
    id serial primary key,
    email varchar(120) unique not null,
    password_hash varchar(155) not null
);
insert into users (email, password_hash) values ('admin@admin.com', 12345);