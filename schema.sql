drop table if exists scheme;
drop table if exists document;
drop table if exists user;
create table user
(
	id int auto_increment,
	email varchar(50) not null,
	name varchar(255) not null,
	password varchar(255) not null,
	role int not null,
	is_enabled bool default true not null,
	created_time timestamp default current_timestamp not null,
	constraint user_pk
		primary key (id)
);

create unique index user_email_uindex
	on user (email);

create table document
(
	id int auto_increment,
	name varchar(255) not null,
	user_id int not null,
	created_time timestamp default current_timestamp not null,
	constraint document_pk
		primary key (id),
	constraint document_user_id_fk
		foreign key (user_id) references user (id)
			on update cascade
);

create unique index document_name_uindex
	on document (name);

create table scheme
(
	id int auto_increment,
	name varchar(255) not null,
	user_id int not null,
	description varchar(255) not null,
	created_time timestamp default current_timestamp not null,
	constraint scheme_pk
		primary key (id),
	constraint scheme_user_id_fk
		foreign key (user_id) references user (id)
			on update cascade
);

create unique index scheme_name_uindex
	on scheme (name);





