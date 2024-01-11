DROP TABLE IF EXISTS aeroplane;


CREATE TABLE public.aeroplane
(
id bigint NOT NULL,
name character varying COLLATE pg_catalog."default",
CONSTRAINT aeroplane_pkey PRIMARY KEY (id)
);


insert into aeroplane (id, name) values (0,'airbus 320');