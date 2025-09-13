--
-- PostgreSQL database dump
--

\restrict ppFc1GatJKVuUjMBWQWxQC2mg4SONLPeQFaCa2QBSXnEmMxIQ6fo5P72YQEbdDq

-- Dumped from database version 17.6
-- Dumped by pg_dump version 17.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: profesores; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.profesores (
    id integer NOT NULL,
    nombre text NOT NULL,
    apellidos text NOT NULL,
    correo text,
    correo_institucional text,
    activo boolean,
    fecha_contratacion timestamp without time zone
);


ALTER TABLE public.profesores OWNER TO postgres;

--
-- Name: colegio_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.colegio_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.colegio_id_seq OWNER TO postgres;

--
-- Name: colegio_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.colegio_id_seq OWNED BY public.profesores.id;


--
-- Name: direcciones; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.direcciones (
    id integer NOT NULL,
    calle text NOT NULL,
    numero text,
    referencia text,
    distrito text,
    provincia text,
    profesor_id integer
);


ALTER TABLE public.direcciones OWNER TO postgres;

--
-- Name: direcciones_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.direcciones_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.direcciones_id_seq OWNER TO postgres;

--
-- Name: direcciones_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.direcciones_id_seq OWNED BY public.direcciones.id;


--
-- Name: direcciones id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.direcciones ALTER COLUMN id SET DEFAULT nextval('public.direcciones_id_seq'::regclass);


--
-- Name: profesores id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profesores ALTER COLUMN id SET DEFAULT nextval('public.colegio_id_seq'::regclass);


--
-- Data for Name: direcciones; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.direcciones (id, calle, numero, referencia, distrito, provincia, profesor_id) FROM stdin;
601	Jasmine Meadow	779	fight	Jesus Maria	Recuay	3
602	Michael Circles	7259	kind	Ilo	Pallasca	49
603	Lori Ranch	78393	imagine	Arequipa	Yungay	97
604	Brandon Brook	250	current	Cuzco	Santa Cruz	82
605	Carey Haven	37398	accept	Jesus Maria	Sihuas	97
606	Aaron Wells	345	ability	Arequipa	Cutervo	80
607	Julia Coves	48030	instead	Ilo	Santa Cruz	22
608	Hardin Knoll	387	southern	Ilo	Aija	93
609	Rivera Fork	72982	article	Ilo	Pomabamba	79
610	Hansen Union	97341	put	Lima	Cutervo	77
611	Sanders Valley	56880	old	Cuzco	Recuay	13
612	Frederick Flats	157	effort	Ite	Cutervo	45
613	James Ridges	22419	well	Ilo	Hualgayoc	20
614	Fischer Glen	10258	however	Ilo	Sihuas	55
615	Diana Plain	224	meeting	Arequipa	Sihuas	29
616	Scott Lodge	772	Congress	Ilo	Carhuaz	47
617	Moss Lights	34118	employee	Jesus Maria	Chota	3
618	Williams Run	195	say	Lima	Carhuaz	43
619	Brown Throughway	9052	about	Trujillo	Cajamarca	95
620	David Neck	812	hair	Cuzco	Carhuaz	42
621	Cooper Coves	22422	positive	Ite	Cutervo	56
622	Blankenship Pass	65113	able	Ilo	Sihuas	46
623	Tim Glens	879	player	Lima	Celendín	39
624	John Roads	80506	him	Trujillo	Carhuaz	36
625	Clarence Island	436	possible	Cuzco	Hualgayoc	24
626	Stevenson Viaduct	878	growth	Ilo	Asunción	15
627	Fields Rapid	4247	hot	Trujillo	San Miguel	77
628	Rhonda Path	9115	through	Arequipa	Celendín	18
629	Hughes Gardens	95063	line	Ite	Cajabamba	98
630	John Walks	973	door	Lima	San Ignacio	68
631	Woods Shores	62905	gas	Arequipa	Casma	94
632	Klein Locks	4852	natural	Jesus Maria	Pomabamba	4
633	Carolyn Rapids	4633	indicate	Arequipa	Cajabamba	6
634	Ashley Valleys	697	high	Ilo	Santa	35
635	David Corners	576	during	Tacna	Celendín	39
636	Jessica Vista	777	nation	Lima	San Miguel	94
637	Copeland Square	80191	when	Ite	Recuay	82
638	James Expressway	349	own	Ilo	Huaylas	23
639	Robert Brook	06432	town	Arequipa	Celendín	81
640	Ray Motorway	5574	city	Jesus Maria	Cajamarca	19
641	Brandi Junctions	626	body	Jesus Maria	San Ignacio	21
642	Smith Burgs	412	technology	Cuzco	San Pablo	88
643	Johnson Field	0933	leave	Jesus Maria	Casma	100
644	Howard Views	344	total	Lima	Pomabamba	57
645	Julie Lights	440	candidate	Jesus Maria	San Ignacio	18
646	Elliott Parks	622	attention	Ilo	Pallasca	82
647	Amber Camp	20597	girl	Jesus Maria	Huarmey	81
648	Angela Wall	644	pressure	Arequipa	Contumazá	48
649	Joseph Crossing	3333	suddenly	Arequipa	Recuay	62
650	Waters Valley	82245	cost	Ite	San Marcos	8
651	Martinez Burg	2499	suggest	Lima	Casma	96
652	Anderson Course	737	no	Ilo	Huarmey	16
653	Pedro Fields	9165	every	Cuzco	Sihuas	59
654	Sean Roads	385	citizen	Lima	Yungay	84
655	Vaughn Motorway	90994	support	Tacna	Jaén	93
656	Molly Point	60390	plan	Arequipa	Jaén	55
657	Douglas Mountains	1247	visit	Cuzco	Pomabamba	16
658	Edwards Oval	8856	either	Arequipa	San Miguel	84
659	Michael Land	30036	big	Cuzco	Corongo	20
660	Coleman Station	2982	serve	Jesus Maria	Jaén	87
661	David Burg	1605	challenge	Arequipa	Cajamarca	98
662	Ross Plains	67350	energy	Cuzco	San Ignacio	12
663	Jesus Walks	229	for	Ilo	San Marcos	30
664	Russell Lock	440	sit	Trujillo	Pallasca	46
665	Casey Canyon	1813	lay	Tacna	Huarmey	43
666	King Bypass	503	raise	Cuzco	Contumazá	45
667	Lester Avenue	48914	Democrat	Lima	Yungay	85
668	Price Freeway	88192	happy	Ite	Antonio Raimondi	100
669	Terry Loop	24880	report	Ite	San Marcos	100
670	Dean Place	389	house	Jesus Maria	Cutervo	51
671	Lee Path	816	interest	Ilo	Huarmey	2
672	Megan Orchard	344	front	Ite	Carhuaz	31
673	Cynthia Burgs	2896	cold	Jesus Maria	Carhuaz	63
674	Bennett Locks	322	enough	Lima	Pallasca	3
675	Toni Lights	067	senior	Jesus Maria	Antonio Raimondi	25
676	Vincent Gateway	1058	deep	Trujillo	Cajabamba	20
677	Carpenter Cliffs	466	chair	Cuzco	Cajabamba	78
678	David Land	8152	worker	Arequipa	Yungay	77
679	Mcdaniel Spurs	190	store	Tacna	San Marcos	17
680	Myers Squares	1781	must	Ite	Sihuas	28
681	Jackson Crest	32096	yes	Ilo	Cajabamba	38
682	Lopez Falls	99751	front	Jesus Maria	Antonio Raimondi	49
683	Clark Highway	18127	first	Jesus Maria	Yungay	2
684	Donald Greens	9251	by	Cuzco	Yungay	99
685	Sandra Heights	2387	magazine	Lima	Recuay	79
686	Nicole Islands	976	third	Tacna	Huarmey	98
687	Mitchell Shore	11926	where	Trujillo	Corongo	91
688	Adams Greens	451	beautiful	Tacna	San Pablo	68
689	Flowers Harbors	8428	street	Trujillo	Aija	66
690	Taylor Road	05788	continue	Trujillo	Pomabamba	56
691	Jessica Ranch	04382	economy	Cuzco	Cutervo	64
692	Shepherd Wall	357	series	Jesus Maria	Huaylas	27
693	Michelle Divide	6036	knowledge	Ilo	Chota	18
694	Regina Wall	84915	staff	Jesus Maria	San Pablo	60
695	Frederick Parks	1551	mind	Ilo	Chota	3
696	Linda Bridge	2383	power	Cuzco	Carhuaz	33
697	Sellers River	0241	and	Ite	Antonio Raimondi	74
698	Andrew Well	258	same	Ilo	Bolognesi	98
699	Jennifer Keys	3053	vote	Trujillo	Pomabamba	12
700	Luke Path	251	same	Ilo	Huaylas	71
701	Christopher Plaza	753	relationship	Arequipa	Bolognesi	71
702	Brady Tunnel	9417	common	Cuzco	Huaylas	8
703	Lisa Center	49367	size	Jesus Maria	Carhuaz	72
704	Best Run	782	article	Arequipa	Contumazá	97
705	Mark Grove	25498	religious	Ite	San Pablo	22
706	Marks Vista	0114	sport	Ite	Bolognesi	54
707	Smith Center	1968	where	Trujillo	Antonio Raimondi	96
708	Amy Views	845	college	Ilo	Celendín	57
709	Lauren Trail	80329	simply	Arequipa	Bolognesi	51
710	Gonzalez Fields	6725	water	Arequipa	Antonio Raimondi	59
711	Hernandez Row	8713	visit	Lima	Corongo	65
712	Hall Fields	25400	would	Trujillo	San Miguel	50
713	Long Skyway	317	response	Cuzco	Hualgayoc	64
714	Murphy Pines	603	owner	Jesus Maria	Recuay	47
715	Bethany Lake	09388	shoulder	Arequipa	Yungay	82
716	Gabriela Underpass	1643	stop	Ite	Carhuaz	4
717	Robinson Tunnel	32003	down	Cuzco	Recuay	47
718	Ramirez Fall	168	author	Tacna	Recuay	71
719	Courtney Island	3456	next	Ite	Cajabamba	72
720	King Cape	981	check	Trujillo	Pallasca	72
721	Fox Prairie	19283	exactly	Cuzco	San Ignacio	83
722	Buchanan Ranch	75194	one	Trujillo	Recuay	10
723	Taylor Circle	3961	oil	Lima	Pomabamba	59
724	Matthew Burg	09876	administration	Ite	Cajabamba	99
725	Harris Locks	56282	real	Tacna	Asunción	51
726	Logan Dam	5137	program	Trujillo	Cajabamba	47
727	Joshua Terrace	204	build	Trujillo	San Miguel	98
728	James Course	86213	would	Lima	Casma	42
729	Tammy Plains	61133	administration	Ilo	Celendín	46
730	Carter Estate	076	medical	Tacna	Jaén	81
731	Monroe Forest	4026	age	Lima	Huarmey	43
732	Moore Parks	7696	eight	Trujillo	Sihuas	71
733	Matthew Stream	773	treatment	Arequipa	Bolognesi	43
734	Jeffery Ramp	792	should	Trujillo	San Pablo	17
735	Douglas Extension	5236	you	Lima	Huarmey	61
736	Schwartz Center	595	cultural	Jesus Maria	Cutervo	39
737	Gray Causeway	60708	town	Trujillo	Recuay	93
738	Brian Forks	902	like	Lima	Pomabamba	47
739	Brooke Mount	916	rich	Trujillo	Cajabamba	18
740	Lara Dale	90232	opportunity	Ilo	Yungay	98
741	Desiree Bridge	1155	small	Cuzco	Carhuaz	30
742	Turner Views	182	pass	Tacna	Asunción	57
743	Johnson Spurs	2421	enjoy	Ilo	Jaén	79
744	Newman Trafficway	85356	moment	Trujillo	Contumazá	22
745	Jones Springs	9038	arrive	Lima	Casma	93
746	Luke Spur	037	model	Arequipa	Jaén	2
747	Brooks Courts	31147	especially	Jesus Maria	San Marcos	12
748	Johnson Springs	6588	tonight	Trujillo	Sihuas	13
749	Carrillo Drive	6749	in	Ite	Contumazá	94
750	Mary Oval	69184	enjoy	Trujillo	Huarmey	62
751	Abbott Manors	77356	different	Ilo	Hualgayoc	34
752	Sullivan Pike	430	peace	Lima	Corongo	92
753	Evan Prairie	89831	improve	Lima	Recuay	24
754	Hall Brook	733	public	Tacna	San Miguel	71
755	Lopez Circles	55234	standard	Arequipa	Antonio Raimondi	32
756	Stevens Groves	90316	material	Ilo	Pallasca	59
757	Adams Stravenue	88070	gas	Ite	Cajamarca	19
758	Anderson Lodge	071	enter	Ilo	Celendín	41
759	Ashley Crossing	947	structure	Ilo	Celendín	100
760	Saunders Manor	762	long	Lima	Chota	48
761	Kaitlyn Turnpike	64537	few	Ilo	Celendín	17
762	Victoria River	77766	second	Arequipa	Sihuas	26
763	Johnson Throughway	6914	benefit	Ilo	Recuay	81
764	Owens Inlet	3185	doctor	Lima	Contumazá	41
765	Sanders Divide	1032	who	Arequipa	Cajabamba	72
766	Renee Ranch	426	data	Trujillo	Bolognesi	4
767	Tanya Shores	503	approach	Arequipa	Chota	99
768	Rodriguez Manors	7056	occur	Tacna	San Ignacio	77
769	Arellano Run	299	rock	Ilo	Sihuas	99
770	Bob Bypass	104	reason	Tacna	Cajamarca	18
771	Fowler Neck	018	material	Jesus Maria	Pomabamba	67
772	Vaughan Key	47561	at	Lima	Cutervo	78
773	Walter Cliff	10296	away	Arequipa	Aija	58
774	Adams Island	084	sport	Lima	San Marcos	30
775	Garza Shoal	26093	administration	Ilo	Cajabamba	16
776	Pierce Drives	239	young	Tacna	San Marcos	100
777	Ford Square	99692	sport	Lima	Casma	57
778	Tom Walks	8924	board	Cuzco	Bolognesi	33
779	William Terrace	3518	our	Ite	Antonio Raimondi	99
780	Romero Fork	9715	customer	Tacna	Chota	50
781	Levi Dam	44079	civil	Jesus Maria	Santa	42
782	Stephen Pass	1925	maintain	Jesus Maria	Chota	1
783	Chung Divide	7689	its	Arequipa	Huaylas	37
784	Natalie Views	1595	far	Lima	Chota	16
785	Debra Underpass	693	still	Cuzco	Santa	2
786	Shane Gateway	018	short	Ilo	Pomabamba	36
787	Sanders Plaza	982	lay	Ilo	Antonio Raimondi	55
788	Davis Cliff	694	baby	Jesus Maria	Carhuaz	100
789	Jerry Drive	2462	him	Cuzco	Antonio Raimondi	72
790	Brandon Plaza	95822	family	Trujillo	Yungay	69
791	Walker Causeway	270	man	Trujillo	Cajabamba	43
792	Walters Way	448	remember	Cuzco	Aija	15
793	William Wall	278	worker	Jesus Maria	Santa	60
794	Jimmy Crossing	219	star	Lima	San Miguel	51
795	Jonathan Center	590	rest	Trujillo	Sihuas	82
796	Aguilar Pine	240	full	Arequipa	Recuay	45
797	Smith Lock	26231	little	Ilo	Huaylas	9
798	Carl Rapids	1799	protect	Arequipa	Asunción	30
799	Stephanie Islands	3823	assume	Lima	Santa Cruz	20
800	Alvarez Hills	578	minute	Lima	Huarmey	95
\.


--
-- Data for Name: profesores; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.profesores (id, nombre, apellidos, correo, correo_institucional, activo, fecha_contratacion) FROM stdin;
1	Gary	Anderson	mariahoward@example.com	benjamin60@codigo.edu.pe	t	2023-01-26 00:00:00
2	Kenneth	Webster	olang@example.org	jbarnes@codigo.edu.pe	t	2022-02-16 00:00:00
3	Chris	Hardin	laurie02@example.com	ucastillo@codigo.edu.pe	f	2022-04-22 00:00:00
4	Cory	Burke	rodriguezjade@example.org	stevenstanley@codigo.edu.pe	t	2022-12-17 00:00:00
5	Alejandro	Miller	david44@example.org	simmonsheather@codigo.edu.pe	t	2023-02-27 00:00:00
6	Timothy	Bullock	brianna76@example.com	lindseysmith@codigo.edu.pe	t	2024-05-20 00:00:00
7	Amy	Lara	wilsonwendy@example.org	kleinlisa@codigo.edu.pe	t	2024-05-09 00:00:00
8	Amber	Cummings	garciadanielle@example.com	thomas03@codigo.edu.pe	f	2022-09-05 00:00:00
9	Jasmine	Ortiz	hkelly@example.net	william93@codigo.edu.pe	f	2022-08-04 00:00:00
10	David	Conner	jacobsalan@example.com	turnerjean@codigo.edu.pe	t	2024-01-16 00:00:00
11	James	Juarez	starkbrandon@example.net	floresamy@codigo.edu.pe	f	2022-09-26 00:00:00
12	Dana	Chase	natalie25@example.com	gregory07@codigo.edu.pe	t	2024-10-03 00:00:00
13	Megan	Thompson	wyattboyle@example.net	proberts@codigo.edu.pe	f	2025-03-09 00:00:00
14	Steven	Hansen	dennislewis@example.org	mwade@codigo.edu.pe	f	2022-03-27 00:00:00
15	Francisco	Patterson	laurenhernandez@example.org	phillip92@codigo.edu.pe	f	2022-02-15 00:00:00
16	John	King	marktownsend@example.org	williamssamantha@codigo.edu.pe	f	2024-05-06 00:00:00
17	Harold	Long	zanthony@example.org	beverlyaguilar@codigo.edu.pe	f	2023-07-28 00:00:00
18	Brenda	Nguyen	mooneyjeffrey@example.com	greengary@codigo.edu.pe	f	2024-10-19 00:00:00
19	Joel	Robinson	thomas23@example.com	moodylisa@codigo.edu.pe	f	2022-08-22 00:00:00
20	Fernando	Snyder	aaron95@example.com	elizabeth26@codigo.edu.pe	t	2022-09-12 00:00:00
21	Heather	Adams	henryjeffrey@example.org	millerdaisy@codigo.edu.pe	t	2025-03-05 00:00:00
22	Renee	Lindsey	colonheather@example.org	danielle92@codigo.edu.pe	t	2025-04-17 00:00:00
23	Belinda	Hill	virginia58@example.org	kimberlyyoung@codigo.edu.pe	f	2025-03-15 00:00:00
24	Suzanne	Harrison	mharris@example.net	fking@codigo.edu.pe	t	2023-02-12 00:00:00
25	Caitlyn	Thompson	taylortracy@example.org	francisco87@codigo.edu.pe	f	2023-06-25 00:00:00
26	Ann	Davis	olivermolly@example.net	jefflawrence@codigo.edu.pe	f	2022-10-20 00:00:00
27	Bianca	Conway	nfriedman@example.org	grayjames@codigo.edu.pe	f	2025-04-09 00:00:00
28	Amanda	Lee	christopher50@example.net	pwarren@codigo.edu.pe	f	2023-11-25 00:00:00
29	Anthony	Schneider	caldwellwilliam@example.net	josephadams@codigo.edu.pe	f	2023-09-03 00:00:00
30	Joseph	Hernandez	amygreen@example.com	michael69@codigo.edu.pe	f	2022-07-02 00:00:00
31	Jacob	Gonzales	xwalker@example.net	andrewsparks@codigo.edu.pe	f	2023-12-17 00:00:00
32	Christopher	Yang	troy20@example.com	jesus38@codigo.edu.pe	f	2023-12-07 00:00:00
33	Marisa	Anderson	gregorywhite@example.org	devin46@codigo.edu.pe	t	2022-05-21 00:00:00
34	Christina	Chapman	pooledavid@example.net	hansenbridget@codigo.edu.pe	f	2023-07-29 00:00:00
35	Brittany	Crawford	qwiley@example.com	thomaspaula@codigo.edu.pe	t	2025-04-28 00:00:00
36	Martha	Parsons	cheryltaylor@example.com	tgarza@codigo.edu.pe	f	2023-09-12 00:00:00
37	David	Hardin	shannon74@example.org	jaclyn47@codigo.edu.pe	t	2023-07-06 00:00:00
38	Eric	Jones	james36@example.com	joshuaabbott@codigo.edu.pe	f	2023-06-06 00:00:00
39	Elizabeth	Woods	warnerchristopher@example.com	ofletcher@codigo.edu.pe	f	2024-08-13 00:00:00
40	Cody	Lee	david35@example.com	derrickerickson@codigo.edu.pe	f	2025-02-27 00:00:00
41	Selena	Herrera	spencerchristine@example.net	chloebrown@codigo.edu.pe	f	2023-02-07 00:00:00
42	Kelli	Oconnor	jthompson@example.net	lisa02@codigo.edu.pe	t	2023-12-28 00:00:00
43	Brian	Martin	drew66@example.net	xlopez@codigo.edu.pe	t	2024-03-14 00:00:00
44	Crystal	Vasquez	sfitzpatrick@example.org	gonzalesjoseph@codigo.edu.pe	f	2024-04-25 00:00:00
45	Erica	Banks	oweeks@example.org	howardcollins@codigo.edu.pe	f	2025-06-09 00:00:00
46	Aaron	Sanchez	carlos81@example.com	vwalls@codigo.edu.pe	t	2023-08-22 00:00:00
47	Carrie	Carter	hernandezstephen@example.org	sullivanjesse@codigo.edu.pe	t	2024-04-19 00:00:00
48	Aaron	Rivera	smithjacob@example.org	ejones@codigo.edu.pe	t	2024-02-14 00:00:00
49	James	Parsons	ysoto@example.net	becky46@codigo.edu.pe	f	2023-01-31 00:00:00
50	Erica	Allison	meghan80@example.com	kcain@codigo.edu.pe	t	2022-11-02 00:00:00
51	Micheal	Williams	lisa27@example.org	sandra69@codigo.edu.pe	t	2022-09-18 00:00:00
52	Stephanie	Riley	kristina60@example.com	macdonaldmichael@codigo.edu.pe	f	2022-11-05 00:00:00
53	Stephen	Mosley	cwyatt@example.net	colemarc@codigo.edu.pe	t	2024-08-07 00:00:00
54	Robin	Chavez	martinelizabeth@example.net	bakerjennifer@codigo.edu.pe	t	2023-09-27 00:00:00
55	Sarah	Bond	amiller@example.net	johnsonjeffery@codigo.edu.pe	t	2025-03-28 00:00:00
56	Angela	Dalton	davispatrick@example.com	amyjohns@codigo.edu.pe	f	2023-10-05 00:00:00
57	Amber	Fischer	zhernandez@example.com	angelicawilliams@codigo.edu.pe	f	2025-04-17 00:00:00
58	Derrick	Robinson	tanya86@example.org	phillipsstephen@codigo.edu.pe	f	2022-10-22 00:00:00
59	Kathy	Hunt	james89@example.org	susanward@codigo.edu.pe	t	2024-07-29 00:00:00
60	David	Graves	levi00@example.net	qjones@codigo.edu.pe	f	2022-01-28 00:00:00
61	Nicole	Miller	andrew41@example.com	fryan@codigo.edu.pe	t	2024-02-22 00:00:00
62	Kimberly	Gray	jeffreyhicks@example.org	plambert@codigo.edu.pe	t	2024-06-17 00:00:00
63	Katherine	Hill	vbrewer@example.net	christopher51@codigo.edu.pe	t	2022-06-21 00:00:00
64	Stephanie	Parker	robert55@example.org	sullivanjason@codigo.edu.pe	f	2022-08-31 00:00:00
65	Teresa	Robinson	sanchezdouglas@example.com	pamela50@codigo.edu.pe	f	2023-08-11 00:00:00
66	Paige	Johnson	david38@example.com	mmurphy@codigo.edu.pe	t	2023-01-28 00:00:00
67	Herbert	Hudson	corey28@example.com	frodriguez@codigo.edu.pe	t	2023-12-28 00:00:00
68	Justin	Hicks	ruthkennedy@example.com	kerry21@codigo.edu.pe	t	2022-12-20 00:00:00
69	Brandi	Williams	stephenstammy@example.net	jefferycarter@codigo.edu.pe	t	2024-11-29 00:00:00
70	Meredith	Marks	xlittle@example.com	christianleon@codigo.edu.pe	t	2024-12-21 00:00:00
71	Marvin	Horne	patricia21@example.net	williamscharles@codigo.edu.pe	t	2024-09-14 00:00:00
72	Allen	Brown	kathryn40@example.org	danielporter@codigo.edu.pe	t	2023-05-13 00:00:00
73	Robert	Cortez	rosstimothy@example.com	smithchristian@codigo.edu.pe	t	2025-03-08 00:00:00
74	David	Diaz	jonathancook@example.com	teresa54@codigo.edu.pe	t	2022-07-22 00:00:00
75	Krista	Garcia	dennis90@example.net	lauren87@codigo.edu.pe	t	2023-05-15 00:00:00
76	Joseph	Green	timothy04@example.org	cooperkathy@codigo.edu.pe	f	2025-06-06 00:00:00
77	Kathryn	Huffman	craigwhite@example.com	timothy29@codigo.edu.pe	t	2022-11-06 00:00:00
78	Ann	Harrison	ccastillo@example.com	chavezrobert@codigo.edu.pe	t	2024-07-11 00:00:00
79	Ashley	Wade	brenda65@example.net	jonathan19@codigo.edu.pe	f	2024-01-06 00:00:00
80	Nicholas	Donovan	xramirez@example.net	craigann@codigo.edu.pe	t	2025-02-18 00:00:00
81	Amanda	Barber	marcus14@example.net	bpatterson@codigo.edu.pe	f	2023-09-03 00:00:00
82	Erin	Ryan	hayesrobert@example.net	barbara19@codigo.edu.pe	f	2023-08-19 00:00:00
83	Brandon	Moreno	jaredsmith@example.org	vsmith@codigo.edu.pe	f	2025-02-09 00:00:00
84	Ryan	Clarke	josephrivera@example.org	hroberts@codigo.edu.pe	f	2024-10-21 00:00:00
85	Amber	Vance	austinlane@example.com	lewiserin@codigo.edu.pe	f	2024-12-19 00:00:00
86	Kim	Ayala	zpeterson@example.com	milleramanda@codigo.edu.pe	t	2022-05-22 00:00:00
87	Robert	Owens	johnsoncharles@example.org	kimberly01@codigo.edu.pe	t	2022-05-15 00:00:00
88	Jonathan	Barrett	hburton@example.net	kgregory@codigo.edu.pe	t	2025-06-25 00:00:00
89	Chelsea	Mendez	lancejohnson@example.com	uandrews@codigo.edu.pe	f	2023-02-01 00:00:00
90	Erik	Phillips	xortiz@example.com	billpatterson@codigo.edu.pe	f	2023-09-06 00:00:00
91	Heather	Gonzalez	taylormaria@example.com	davisrobin@codigo.edu.pe	t	2022-10-31 00:00:00
92	Heidi	Smith	swilson@example.net	kthomas@codigo.edu.pe	t	2023-06-08 00:00:00
93	Martin	Montgomery	robert05@example.net	matthewsalinas@codigo.edu.pe	f	2023-06-20 00:00:00
94	Richard	Golden	cmays@example.com	hayesmichael@codigo.edu.pe	t	2022-09-04 00:00:00
95	Drew	Watson	thomasjennifer@example.org	adrianreid@codigo.edu.pe	f	2024-06-09 00:00:00
96	Alexander	Vega	christine32@example.org	kspencer@codigo.edu.pe	f	2022-05-25 00:00:00
97	Steven	Hoffman	shepardkeith@example.com	vanessa50@codigo.edu.pe	t	2022-06-18 00:00:00
98	Paul	Thompson	lynn73@example.org	joshuabarnes@codigo.edu.pe	t	2022-03-03 00:00:00
99	Emily	Jones	ramseycalvin@example.org	eric41@codigo.edu.pe	t	2023-12-01 00:00:00
100	Ashlee	Lucas	fullersarah@example.org	tyler92@codigo.edu.pe	f	2025-01-17 00:00:00
\.


--
-- Name: colegio_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.colegio_id_seq', 100, true);


--
-- Name: direcciones_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.direcciones_id_seq', 800, true);


--
-- Name: profesores colegio_correo_institucional_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profesores
    ADD CONSTRAINT colegio_correo_institucional_key UNIQUE (correo_institucional);


--
-- Name: profesores colegio_correo_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profesores
    ADD CONSTRAINT colegio_correo_key UNIQUE (correo);


--
-- Name: profesores colegio_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profesores
    ADD CONSTRAINT colegio_pkey PRIMARY KEY (id);


--
-- Name: direcciones direcciones_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.direcciones
    ADD CONSTRAINT direcciones_pkey PRIMARY KEY (id);


--
-- Name: direcciones direcciones_profesor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.direcciones
    ADD CONSTRAINT direcciones_profesor_id_fkey FOREIGN KEY (profesor_id) REFERENCES public.profesores(id);


--
-- PostgreSQL database dump complete
--

\unrestrict ppFc1GatJKVuUjMBWQWxQC2mg4SONLPeQFaCa2QBSXnEmMxIQ6fo5P72YQEbdDq

