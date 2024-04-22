--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2
-- Dumped by pg_dump version 14.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: so; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA so;


ALTER SCHEMA so OWNER TO postgres;

--
-- Name: clase; Type: DOMAIN; Schema: so; Owner: postgres
--

CREATE DOMAIN so.clase AS character varying
	CONSTRAINT clase_check CHECK (((VALUE)::text = ANY ((ARRAY['mamifero'::character varying, 'reptil'::character varying, 'pez'::character varying, 'insecto'::character varying])::text[])));


ALTER DOMAIN so.clase OWNER TO postgres;

--
-- Name: cultura_sagrado; Type: DOMAIN; Schema: so; Owner: postgres
--

CREATE DOMAIN so.cultura_sagrado AS character varying
	CONSTRAINT cultura_sagrado_check CHECK (((VALUE)::text = ANY ((ARRAY['China'::character varying, 'India'::character varying, 'Mesoamérica'::character varying, 'Egipto'::character varying, 'Vietnam'::character varying, 'Ghana'::character varying, 'Norteamerica'::character varying, 'ninguno'::character varying])::text[])));


ALTER DOMAIN so.cultura_sagrado OWNER TO postgres;

--
-- Name: dieta; Type: DOMAIN; Schema: so; Owner: postgres
--

CREATE DOMAIN so.dieta AS character varying
	CONSTRAINT dieta_check CHECK (((VALUE)::text = ANY ((ARRAY['omnivoro'::character varying, 'herbívoros'::character varying, 'carnivoro'::character varying, 'descomponedores'::character varying, 'Parásitos'::character varying, 'Coprófagos'::character varying])::text[])));


ALTER DOMAIN so.dieta OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: animales; Type: TABLE; Schema: so; Owner: postgres
--

CREATE TABLE so.animales (
    id_clase character varying NOT NULL,
    reino character varying(20) NOT NULL,
    clase so.clase NOT NULL,
    extremidades boolean
);


ALTER TABLE so.animales OWNER TO postgres;

--
-- Name: individuo; Type: TABLE; Schema: so; Owner: postgres
--

CREATE TABLE so.individuo (
    nombre_individuo character varying(20),
    id_individuo integer NOT NULL,
    id_subespecie character varying NOT NULL,
    edad numeric,
    peso_kg numeric,
    CONSTRAINT id_y_peso_animal CHECK (((((id_subespecie)::text = '1'::text) AND ((peso_kg >= (50)::numeric) AND (peso_kg <= (500)::numeric))) OR (((id_subespecie)::text = '2'::text) AND ((peso_kg >= (5)::numeric) AND (peso_kg <= (50)::numeric))) OR (((id_subespecie)::text = '3'::text) AND ((peso_kg >= (2)::numeric) AND (peso_kg <= (4)::numeric))) OR (((id_subespecie)::text = '4'::text) AND ((peso_kg >= 0.05) AND (peso_kg <= 0.30))) OR (((id_subespecie)::text = '5'::text) AND ((peso_kg >= (2)::numeric) AND (peso_kg <= (4)::numeric))) OR (((id_subespecie)::text = '6'::text) AND ((peso_kg >= (60)::numeric) AND (peso_kg <= (1400)::numeric))) OR (((id_subespecie)::text = '7'::text) AND ((peso_kg >= 0.05) AND (peso_kg <= 0.085))) OR (((id_subespecie)::text = '8'::text) AND ((peso_kg >= (45)::numeric) AND (peso_kg <= (113)::numeric))) OR (((id_subespecie)::text = '9'::text) AND ((peso_kg >= (1)::numeric) AND (peso_kg <= (100)::numeric))) OR (((id_subespecie)::text = '10'::text) AND ((peso_kg >= (5)::numeric) AND (peso_kg <= (250)::numeric))) OR (((id_subespecie)::text = '11'::text) AND ((peso_kg >= (40)::numeric) AND (peso_kg <= (450)::numeric))) OR (((id_subespecie)::text = '12'::text) AND ((peso_kg >= (1)::numeric) AND (peso_kg <= (4)::numeric))) OR (((id_subespecie)::text = '13'::text) AND ((peso_kg >= (45)::numeric) AND (peso_kg <= (1000)::numeric))) OR (((id_subespecie)::text = '14'::text) AND ((peso_kg >= 0.9) AND (peso_kg <= (1100)::numeric))) OR (((id_subespecie)::text = '15'::text) AND ((peso_kg >= (6)::numeric) AND (peso_kg <= (12)::numeric))) OR (((id_subespecie)::text = '16'::text) AND ((peso_kg >= (200)::numeric) AND (peso_kg <= (18400)::numeric))) OR (((id_subespecie)::text = '17'::text) AND ((peso_kg >= (200)::numeric) AND (peso_kg <= (12000)::numeric)))))
);


ALTER TABLE so.individuo OWNER TO postgres;

--
-- Name: individuo_id_individuo_seq; Type: SEQUENCE; Schema: so; Owner: postgres
--

CREATE SEQUENCE so.individuo_id_individuo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE so.individuo_id_individuo_seq OWNER TO postgres;

--
-- Name: individuo_id_individuo_seq; Type: SEQUENCE OWNED BY; Schema: so; Owner: postgres
--

ALTER SEQUENCE so.individuo_id_individuo_seq OWNED BY so.individuo.id_individuo;


--
-- Name: refugio; Type: TABLE; Schema: so; Owner: postgres
--

CREATE TABLE so.refugio (
    id character varying NOT NULL,
    nombre character varying(40),
    capacidad_individuos integer,
    id_clase character varying NOT NULL
);


ALTER TABLE so.refugio OWNER TO postgres;

--
-- Name: subespecie; Type: TABLE; Schema: so; Owner: postgres
--

CREATE TABLE so.subespecie (
    subespecie character varying(20),
    id_refugio character varying NOT NULL,
    id_subespecie character varying NOT NULL,
    dieta so.dieta NOT NULL,
    extinta boolean,
    lista_roja boolean,
    cultura_sagrado so.cultura_sagrado DEFAULT 'ninguno'::character varying,
    comido_en character varying(20) DEFAULT 'ninguno'::character varying,
    poblacion numeric DEFAULT 0
);


ALTER TABLE so.subespecie OWNER TO postgres;

--
-- Name: individuo id_individuo; Type: DEFAULT; Schema: so; Owner: postgres
--

ALTER TABLE ONLY so.individuo ALTER COLUMN id_individuo SET DEFAULT nextval('so.individuo_id_individuo_seq'::regclass);


--
-- Data for Name: animales; Type: TABLE DATA; Schema: so; Owner: postgres
--

COPY so.animales (id_clase, reino, clase, extremidades) FROM stdin;
1	animal	mamifero	t
2	animal	pez	f
3	animal	reptil	t
4	animal	insecto	t
\.


--
-- Data for Name: individuo; Type: TABLE DATA; Schema: so; Owner: postgres
--

COPY so.individuo (nombre_individuo, id_individuo, id_subespecie, edad, peso_kg) FROM stdin;
\N	1	17	\N	5000
jack	2	14	18	500
\N	3	4	\N	0.27
Motas	4	2	4	10
Rafa	5	2	10	40
Bruno	6	1	11	300
Thor	7	16	18	5000
Scarface	8	10	8	230
Tarantino	9	14	17	500
Kora	10	2	9	16
Laika	11	2	5	20
Cesar	12	13	12	500
\.


--
-- Data for Name: refugio; Type: TABLE DATA; Schema: so; Owner: postgres
--

COPY so.refugio (id, nombre, capacidad_individuos, id_clase) FROM stdin;
1	Refugio distrital para mamiferos	45	1
2	Refugio distrital para peces	150	2
3	Refugio distrital para reptiles	38	3
4	Refugio distrital para insectos	1000	4
\.


--
-- Data for Name: subespecie; Type: TABLE DATA; Schema: so; Owner: postgres
--

COPY so.subespecie (subespecie, id_refugio, id_subespecie, dieta, extinta, lista_roja, cultura_sagrado, comido_en, poblacion) FROM stdin;
Mammut	1	17	herbívoros	t	f	ninguno	ninguno	0
perro	1	2	carnivoro	f	f	India	China	525000000
liebre	1	5	herbívoros	f	t	China	China	7000000
cocodrilo	3	14	carnivoro	f	t	China	China	7000000
cucaracha	4	4	descomponedores	f	f	ninguno	China	700000000
oso pardo	1	1	omnivoro	f	t	ninguno	China	7000
Tyrannosaurus Rex	3	16	carnivoro	t	f	ninguno	ninguno	0
caballo	1	13	herbívoros	f	f	ninguno	ninguno	10000000
león	1	10	carnivoro	f	t	ninguno	ninguno	230000
\.


--
-- Name: individuo_id_individuo_seq; Type: SEQUENCE SET; Schema: so; Owner: postgres
--

SELECT pg_catalog.setval('so.individuo_id_individuo_seq', 12, true);


--
-- Name: animales animales_pkey; Type: CONSTRAINT; Schema: so; Owner: postgres
--

ALTER TABLE ONLY so.animales
    ADD CONSTRAINT animales_pkey PRIMARY KEY (id_clase);


--
-- Name: subespecie check_subespecie; Type: CONSTRAINT; Schema: so; Owner: postgres
--

ALTER TABLE ONLY so.subespecie
    ADD CONSTRAINT check_subespecie UNIQUE (subespecie);


--
-- Name: individuo individuo_pkey; Type: CONSTRAINT; Schema: so; Owner: postgres
--

ALTER TABLE ONLY so.individuo
    ADD CONSTRAINT individuo_pkey PRIMARY KEY (id_individuo);


--
-- Name: refugio refugio_pkey; Type: CONSTRAINT; Schema: so; Owner: postgres
--

ALTER TABLE ONLY so.refugio
    ADD CONSTRAINT refugio_pkey PRIMARY KEY (id);


--
-- Name: subespecie subespecie_pkey; Type: CONSTRAINT; Schema: so; Owner: postgres
--

ALTER TABLE ONLY so.subespecie
    ADD CONSTRAINT subespecie_pkey PRIMARY KEY (id_subespecie);


--
-- Name: refugio id_clase; Type: FK CONSTRAINT; Schema: so; Owner: postgres
--

ALTER TABLE ONLY so.refugio
    ADD CONSTRAINT id_clase FOREIGN KEY (id_clase) REFERENCES so.animales(id_clase) ON UPDATE CASCADE;


--
-- Name: refugio id_clase_del; Type: FK CONSTRAINT; Schema: so; Owner: postgres
--

ALTER TABLE ONLY so.refugio
    ADD CONSTRAINT id_clase_del FOREIGN KEY (id_clase) REFERENCES so.animales(id_clase) ON DELETE CASCADE;


--
-- Name: subespecie id_refugio; Type: FK CONSTRAINT; Schema: so; Owner: postgres
--

ALTER TABLE ONLY so.subespecie
    ADD CONSTRAINT id_refugio FOREIGN KEY (id_refugio) REFERENCES so.refugio(id) ON UPDATE CASCADE;


--
-- Name: individuo id_subespecie; Type: FK CONSTRAINT; Schema: so; Owner: postgres
--

ALTER TABLE ONLY so.individuo
    ADD CONSTRAINT id_subespecie FOREIGN KEY (id_subespecie) REFERENCES so.subespecie(id_subespecie) ON UPDATE CASCADE;


--
-- PostgreSQL database dump complete
--

