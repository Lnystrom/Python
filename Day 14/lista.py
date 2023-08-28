"""This module contains all information that is needed for the sort function"""

data = """1	youtube.com	8,184,698,651
2	en.wikipedia.org	2,896,256,261
3	twitter.com	1,970,902,586
4	instagram.com	1,690,557,250
5	amazon.com	941,617,882
6	pinterest.com	834,802,079
7	imdb.com	726,030,044
8	es.wikipedia.org	602,904,595
9	facebook.com	551,954,710
10	fandom.com	527,692,324
11	apple.com	479,853,905
12	ja.wikipedia.org	457,146,037
13	de.wikipedia.org	410,650,975
14	live.com	380,165,003
15	cricbuzz.com	330,655,815
16	fr.wikipedia.org	309,400,383
17	linkedin.com	281,297,942
18	globo.com	265,597,387
19	microsoft.com	252,803,595
20	nytimes.com	251,707,985
21	etsy.com	251,597,151
22	it.wikipedia.org	244,951,362
23	mayoclinic.org	229,542,637
24	healthline.com	228,849,546
25	indiatimes.com	216,057,808
26	amazon.in	207,247,289
27	amazon.de	204,993,642
28	bbc.co.uk	184,907,100
29	ikea.com	184,895,409
30	amazon.co.jp	180,411,677
31	amazon.co.uk	178,254,939
32	indeed.com	177,065,528
33	flipkart.com	172,755,306
34	bbc.com	158,803,824
35	espn.com	156,286,007
36	mail.yahoo.com	155,627,263
37	ebay.com	155,399,761
38	hurriyet.com.tr	149,869,821
39	allegro.pl	143,848,076
40	booking.com	143,655,090
41	mercadolivre.com.br	143,134,791
42	britannica.com	142,397,079
43	google.com	141,297,176
44	kompas.com	139,963,591
45	nih.gov	134,053,666
46	cnn.com	125,779,675
47	merriam-webster.com	121,666,645
48	homedepot.com	118,195,967
49	amazon.fr	112,178,475
50	ar.wikipedia.org	109,840,894
51	detik.com	109,248,806
52	nike.com	108,103,178
53	medlineplus.gov	106,418,617
54	id.wikipedia.org	103,975,885
55	brainly.co.id	102,397,336
56	milliyet.com.tr	99,296,399
57	accuweather.com	98,689,506
58	magazineluiza.com.br	98,598,710
59	marca.com	98,550,894
60	medicalnewstoday.com	97,945,908
61	cdc.gov	97,933,405
62	hepsiburada.com	96,838,668
63	cambridge.org	96,607,060
64	cookpad.com	95,125,602
65	m.wikipedia.org	95,029,693
66	dailymail.co.uk	95,005,731
67	as.com	93,305,939
68	ilovepdf.com	93,243,977
69	gsmarena.com	92,247,265
70	byjus.com	89,725,133
71	amazon.it	88,848,535
72	adobe.com	88,668,874
73	investing.com	88,290,123
74	epfindia.gov.in	87,464,090
75	clevelandclinic.org	87,104,871
76	aliexpress.com	86,167,214
77	espncricinfo.com	86,069,721
78	india.com	85,940,027
79	ndtv.com	84,883,790
80	canva.com	82,990,122
81	amazon.es	81,719,879
82	craigslist.org	80,949,296
83	finance.yahoo.com	80,190,740
84	dailymotion.com	79,367,183
85	indiamart.com	78,155,956
86	kinopoisk.ru	77,694,674
87	nl.wikipedia.org	77,354,382
88	onet.pl	76,383,500
89	omegle.com	76,348,649
90	goal.com	73,866,626
91	americanas.com.br	73,344,240
92	investopedia.com	70,668,903
93	dictionary.com	70,350,892
94	mail.ru	68,176,299
95	ebay.co.uk	66,996,424
96	naver.com	66,784,762
97	hm.com	66,387,888
98	hotstar.com	65,480,184
99	bestbuy.com	64,746,994
100	collinsdictionary.com	64,628,918"""

# Split the data by lines
lines = data.strip().split('\n')

# Initialize an empty dictionary to store the result
website_data = {}

# Process each line and create the dictionary
for line in lines:
    rank, domain, visits = line.split('\t')
    rank = int(rank)  # Convert the rank to an integer
    visits = int(visits.replace(',', ''))  # Convert the visits to an integer
    website_data[rank] = {'domain': domain, 'visits': visits}

# Print the dictionary

