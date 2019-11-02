drop table if exists violation;
drop table if exists document_release;
drop table if exists party;
drop table if exists level_specific_sensitivity;
drop table if exists specific_sensitivity;
drop table if exists stream;
drop table if exists level;
drop table if exists scheme;
drop table if exists document;
drop table if exists user;


create table user
(
    id           int auto_increment,
    email        varchar(50)                         not null,
    name         varchar(255)                        not null,
    password     varchar(255)                        not null,
    role         int                                 not null,
    is_enabled   bool      default true              not null,
    created_time timestamp default current_timestamp not null,

    constraint user_pk
        primary key (id)
);

create unique index user_email_uindex
    on user (email);

create table document
(
    id           int auto_increment,
    name         varchar(255)                        not null,
    user_id      int                                 not null,
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
    id           int auto_increment,
    name         varchar(255)                        not null,
    user_id      int                                 not null,
    description  varchar(255)                        not null,
    created_time timestamp default current_timestamp not null,

    constraint scheme_pk
        primary key (id),
    constraint scheme_user_id_fk
        foreign key (user_id) references user (id)
            on update cascade
);

create unique index scheme_name_uindex
    on scheme (name);

create table level
(
    id           int auto_increment,
    name         varchar(255)                        not null,
    scheme_id    int                                 not null,
    color        varchar(50)                         not null,
    description  varchar(255)                        not null,
    is_party     bool      default false             not null,
    created_time timestamp default current_timestamp not null,

    constraint level_pk
        primary key (id),
    constraint level_scheme_id_fk
        foreign key (scheme_id) references scheme (id)
            on update cascade
);


create table party
(
    id               int auto_increment,
    party_level_id   int                                 not null,
    include_level_id int                                 not null,
    created_time     timestamp default current_timestamp not null,

    constraint party_pk
        primary key (id),
    constraint party_level_level_id_fk
        foreign key (party_level_id) references level (id)
            on update cascade,
    constraint include_level_level_id_fk
        foreign key (include_level_id) references level (id)
            on update cascade
);

create unique index party_include_level_uindex
    on party (party_level_id, include_level_id);

create table stream
(
    id           int auto_increment,
    name         varchar(50)                         not null,
    description  varchar(255)                        not null,
    created_time timestamp default current_timestamp not null,

    constraint stream_pk
        primary key (id)

);

create unique index stream_name_uindex
    on stream (name);

create table specific_sensitivity
(
    id           int auto_increment,
    name         varchar(50)                         not null,
    stream_id    int                                 not null,
    description  varchar(255)                        not null,
    created_time timestamp default current_timestamp not null,

    constraint specific_sensitivity_pk
        primary key (id),
    constraint specific_sensitivity_steam_id_fk
        foreign key (stream_id) references stream (id)
            on update cascade

);

create unique index specific_sensitivity_name_uindex
    on specific_sensitivity (name);

create table level_specific_sensitivity
(
    id                      int auto_increment,
    level_id                int                                 not null,
    specific_sensitivity_id int                                 not null,
    created_time            timestamp default current_timestamp not null,

    constraint level_specific_sensitivity_pk
        primary key (id),
    constraint level_specific_sensitivity_level_id_fk
        foreign key (level_id) references level (id)
            on update cascade,
    constraint level_specific_sensitivity_specific_sensitivity_id_fk
        foreign key (specific_sensitivity_id) references specific_sensitivity (id)
            on update cascade

);

create unique index level_specific_sensitivity_level_uindex
    on level_specific_sensitivity (level_id, specific_sensitivity_id);

create table document_release
(
    id           int auto_increment,
    level_id     int                                 not null,
    document_id  int                                 not null,
    created_time timestamp default current_timestamp not null,

    constraint release_pk
        primary key (id),
    constraint release_level_id_fk
        foreign key (level_id) references level (id)
            on update cascade,
    constraint release_document_id_fk
        foreign key (document_id) references document (id)
            on update cascade
);

create table violation
(
    id           int auto_increment,
    release_id   int                                 not null,
    description  varchar(255)                        not null,
    created_time timestamp default current_timestamp not null,

    constraint violation_pk
        primary key (id),
    constraint violation_release_id_fk
        foreign key (release_id) references document_release (id)
            on update cascade
);
