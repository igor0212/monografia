-- CREATE DATABASE

CREATE TABLE public."Type" (
	"id" int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,	
	"name" varchar(50) NOT NULL,	
	CONSTRAINT "PK_Type" PRIMARY KEY ("id")
);

CREATE TABLE public."Goal" (
	"id" int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,	
	"name" varchar(50) NOT NULL,	
	CONSTRAINT "PK_Goal" PRIMARY KEY ("id")
);	

CREATE TABLE public."City" (
	"id" int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,	
	"name" varchar(50) NOT NULL,	
	CONSTRAINT "PK_City" PRIMARY KEY ("id")
);		

CREATE TABLE public."District" (
	"id" int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,	
	"name" varchar(50) NOT NULL,	
	CONSTRAINT "PK_District" PRIMARY KEY ("id")
);		

CREATE TABLE public."Property" (
	"id" int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,	
	"partner_id" varchar(50) NOT NULL,
	"type_id" int4 NOT NULL,
	"district_id" int4 NOT NULL,
	"city_id" int4 NOT NULL,
	"goal_id" int4 NOT NULL,
	"number" varchar(50) NULL,
	"street" varchar(100) NOT NULL,
	"size" int4 NOT NULL,
	"bedroom_number" int4 NOT NULL,
	"room_number" int4 NOT NULL,
	"bath_number" int4 NOT NULL,
	"parking_number" int4 NOT NULL,
	CONSTRAINT "PK_Property" PRIMARY KEY ("id"),
	CONSTRAINT "FK_Property_Type_Id" FOREIGN KEY ("type_id") REFERENCES public."Type"("id") ON DELETE RESTRICT,
	CONSTRAINT "FK_Property_District_Id" FOREIGN KEY ("district_id") REFERENCES public."District"("id") ON DELETE RESTRICT,
	CONSTRAINT "FK_Property_City_Id" FOREIGN KEY ("city_id") REFERENCES public."City"("id") ON DELETE restrict,
	CONSTRAINT "FK_Property_Goal_Id" FOREIGN KEY ("goal_id") REFERENCES public."Goal"("id") ON DELETE RESTRICT
);		

CREATE INDEX "IX_Property_Type_Id" ON public."Property" USING btree ("type_id");
CREATE INDEX "IX_Property_District_Id" ON public."Property" USING btree ("district_id");
CREATE INDEX "IX_Property_City_Id" ON public."Property" USING btree ("city_id");
CREATE INDEX "IX_Property_Goal_Id" ON public."Property" USING btree ("goal_id");	

CREATE TABLE public."Management" (
	"id" int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,	
	"partner_id" varchar(50) NOT NULL,
	"price" numeric NOT NULL,
	"tax_rate" numeric NULL,
	"property_tax" numeric NULL,
	"created_on" timestamp NULL,
	"is_available" bool NOT NULL DEFAULT false,
	
	CONSTRAINT "PK_Management" PRIMARY KEY ("id")	
);

--GOAL
INSERT INTO public."Goal" ("name") VALUES('Sell');
INSERT INTO public."Goal" ("name") VALUES('Rent');

--TYPE
INSERT INTO public."Type" ("name") VALUES('Apartment');
INSERT INTO public."Type" ("name") VALUES('House');
INSERT INTO public."Type" ("name") VALUES('Condo');

--CITY
INSERT INTO public."City" ("name") VALUES('Belo Horizonte');

--DISTRICT
INSERT INTO public."District" ("name") VALUES('Sagrada Família');
INSERT INTO public."District" ("name") VALUES('Buritis');
INSERT INTO public."District" ("name") VALUES('Padre Eustáquio');
INSERT INTO public."District" ("name") VALUES('Lindéia');
INSERT INTO public."District" ("name") VALUES('Santa Mônica');
INSERT INTO public."District" ("name") VALUES('Céu Azul');
INSERT INTO public."District" ("name") VALUES('Santa Cruz');
INSERT INTO public."District" ("name") VALUES('Santo Antônio');
INSERT INTO public."District" ("name") VALUES('Alto Vera Cruz');
INSERT INTO public."District" ("name") VALUES('Jardim dos Comerciários');
INSERT INTO public."District" ("name") VALUES('Piratininga');
INSERT INTO public."District" ("name") VALUES('Mantiqueira');
INSERT INTO public."District" ("name") VALUES('Serra');
INSERT INTO public."District" ("name") VALUES('Sion');
INSERT INTO public."District" ("name") VALUES('Lourdes');
INSERT INTO public."District" ("name") VALUES('Santa Amélia');
INSERT INTO public."District" ("name") VALUES('Cabana do Pai Tomás');
INSERT INTO public."District" ("name") VALUES('Santa Efigênia');
INSERT INTO public."District" ("name") VALUES('Pindorama');
INSERT INTO public."District" ("name") VALUES('Boa Vista');
INSERT INTO public."District" ("name") VALUES('Gutierrez');
INSERT INTO public."District" ("name") VALUES('Ouro Preto');
INSERT INTO public."District" ("name") VALUES('Castelo');
INSERT INTO public."District" ("name") VALUES('Planalto');
INSERT INTO public."District" ("name") VALUES('São João Batista');
INSERT INTO public."District" ("name") VALUES('Centro');
INSERT INTO public."District" ("name") VALUES('Goiânia');
INSERT INTO public."District" ("name") VALUES('Jaqueline');
INSERT INTO public."District" ("name") VALUES('Ribeiro de Abreu');
INSERT INTO public."District" ("name") VALUES('Santa Terezinha');
INSERT INTO public."District" ("name") VALUES('Santa Tereza');
INSERT INTO public."District" ("name") VALUES('Jardim Felicidade');
INSERT INTO public."District" ("name") VALUES('Cidade Nova');
INSERT INTO public."District" ("name") VALUES('Carlos Prates ');
INSERT INTO public."District" ("name") VALUES('Estrela Dalva');
INSERT INTO public."District" ("name") VALUES('Havaí');
INSERT INTO public."District" ("name") VALUES('Nova Suissa');
INSERT INTO public."District" ("name") VALUES('Conjunto Taquaril');
INSERT INTO public."District" ("name") VALUES('União');
INSERT INTO public."District" ("name") VALUES('Salgado Filho');
INSERT INTO public."District" ("name") VALUES('Araguaia');
INSERT INTO public."District" ("name") VALUES('Glória');
INSERT INTO public."District" ("name") VALUES('Serra Verde');
INSERT INTO public."District" ("name") VALUES('São Geraldo');
INSERT INTO public."District" ("name") VALUES('Prado');
INSERT INTO public."District" ("name") VALUES('São Gabriel');
INSERT INTO public."District" ("name") VALUES('Tupi B');
INSERT INTO public."District" ("name") VALUES('Paraíso');
INSERT INTO public."District" ("name") VALUES('Copacabana');
INSERT INTO public."District" ("name") VALUES('Caiçaras');
INSERT INTO public."District" ("name") VALUES('Camargos');
INSERT INTO public."District" ("name") VALUES('Rio Branco');
INSERT INTO public."District" ("name") VALUES('Anchieta');
INSERT INTO public."District" ("name") VALUES('Ipiranga');
INSERT INTO public."District" ("name") VALUES('Milionários');
INSERT INTO public."District" ("name") VALUES('Betânia');
INSERT INTO public."District" ("name") VALUES('Diamante');
INSERT INTO public."District" ("name") VALUES('Floresta');
INSERT INTO public."District" ("name") VALUES('Savassi');
INSERT INTO public."District" ("name") VALUES('Jardim Guanabara');
INSERT INTO public."District" ("name") VALUES('Vila Vista Alegre');
INSERT INTO public."District" ("name") VALUES('Tirol');
INSERT INTO public."District" ("name") VALUES('Jardim América');
INSERT INTO public."District" ("name") VALUES('Caiçara Adelaide');
INSERT INTO public."District" ("name") VALUES('Concórdia');
INSERT INTO public."District" ("name") VALUES('Tupi A');
INSERT INTO public."District" ("name") VALUES('Minascaixa');
INSERT INTO public."District" ("name") VALUES('Cardoso');
INSERT INTO public."District" ("name") VALUES('Colégio Batista');
INSERT INTO public."District" ("name") VALUES('Barreiro');
INSERT INTO public."District" ("name") VALUES('Europa');
INSERT INTO public."District" ("name") VALUES('Serrano');
INSERT INTO public."District" ("name") VALUES('Jardim Alvorada');
INSERT INTO public."District" ("name") VALUES('Santo Agostinho');
INSERT INTO public."District" ("name") VALUES('Aparecida');
INSERT INTO public."District" ("name") VALUES('Floramar');
INSERT INTO public."District" ("name") VALUES('Dom Bosco');
INSERT INTO public."District" ("name") VALUES('João Pinheiro');
INSERT INTO public."District" ("name") VALUES('Nossa Senhora de Fátima');
INSERT INTO public."District" ("name") VALUES('Jardim Vitória');
INSERT INTO public."District" ("name") VALUES('Alípio de Melo');
INSERT INTO public."District" ("name") VALUES('Nova Gameleira');
INSERT INTO public."District" ("name") VALUES('Itapoã');
INSERT INTO public."District" ("name") VALUES('Jardim Leblon');
INSERT INTO public."District" ("name") VALUES('Cachoeirinha');
INSERT INTO public."District" ("name") VALUES('Bairro das Indústrias I');
INSERT INTO public."District" ("name") VALUES('Santa Inês');
INSERT INTO public."District" ("name") VALUES('Lagoa');
INSERT INTO public."District" ("name") VALUES('São Bernardo');
INSERT INTO public."District" ("name") VALUES('Renascença');
INSERT INTO public."District" ("name") VALUES('Dona Clara');
INSERT INTO public."District" ("name") VALUES('Funcionários');
INSERT INTO public."District" ("name") VALUES('Belvedere');
INSERT INTO public."District" ("name") VALUES('Maria Goretti');
INSERT INTO public."District" ("name") VALUES('Nova Vista');
INSERT INTO public."District" ("name") VALUES('Independência');
INSERT INTO public."District" ("name") VALUES('Novo Aarão Reis');
INSERT INTO public."District" ("name") VALUES('Manacás');
INSERT INTO public."District" ("name") VALUES('Vila Pinho');
INSERT INTO public."District" ("name") VALUES('Esplanada');
INSERT INTO public."District" ("name") VALUES('Nazaré');
INSERT INTO public."District" ("name") VALUES('Cruzeiro');
INSERT INTO public."District" ("name") VALUES('Vale do Jatobá');
INSERT INTO public."District" ("name") VALUES('Vila Barragem Santa Lúcia');
INSERT INTO public."District" ("name") VALUES('Providência');
INSERT INTO public."District" ("name") VALUES('Flávio Marques Lisboa');
INSERT INTO public."District" ("name") VALUES('Novo Glória');
INSERT INTO public."District" ("name") VALUES('Guarani');
INSERT INTO public."District" ("name") VALUES('Letícia');
INSERT INTO public."District" ("name") VALUES('Maria Helena');
INSERT INTO public."District" ("name") VALUES('Coqueiros');
INSERT INTO public."District" ("name") VALUES('Coração Eucarístico');
INSERT INTO public."District" ("name") VALUES('Palmeiras');
INSERT INTO public."District" ("name") VALUES('Itaipu');
INSERT INTO public."District" ("name") VALUES('Candelária');
INSERT INTO public."District" ("name") VALUES('Calafate');
INSERT INTO public."District" ("name") VALUES('São Tomáz');
INSERT INTO public."District" ("name") VALUES('Alto Caiçaras');
INSERT INTO public."District" ("name") VALUES('Santo André');
INSERT INTO public."District" ("name") VALUES('Santa Lúcia');
INSERT INTO public."District" ("name") VALUES('Vila Clóris');
INSERT INTO public."District" ("name") VALUES('Santa Maria');
INSERT INTO public."District" ("name") VALUES('Ventosa');
INSERT INTO public."District" ("name") VALUES('Brasil Industrial');
INSERT INTO public."District" ("name") VALUES('Jardim São José');
INSERT INTO public."District" ("name") VALUES('São Marcos');
INSERT INTO public."District" ("name") VALUES('Santa Rosa');
INSERT INTO public."District" ("name") VALUES('Heliópolis');
INSERT INTO public."District" ("name") VALUES('Apolônia');
INSERT INTO public."District" ("name") VALUES('Marçola');
INSERT INTO public."District" ("name") VALUES('Minaslândia');
INSERT INTO public."District" ("name") VALUES('Bonsucesso');
INSERT INTO public."District" ("name") VALUES('Paquetá');
INSERT INTO public."District" ("name") VALUES('Luxemburgo');
INSERT INTO public."District" ("name") VALUES('Casa Branca');
INSERT INTO public."District" ("name") VALUES('São Pedro');
INSERT INTO public."District" ("name") VALUES('Grajaú');
INSERT INTO public."District" ("name") VALUES('Nossa Senhora da Conceição');
INSERT INTO public."District" ("name") VALUES('Paulo VI');
INSERT INTO public."District" ("name") VALUES('Barro Preto');
INSERT INTO public."District" ("name") VALUES('Teixeira Dias');
INSERT INTO public."District" ("name") VALUES('Miramar');
INSERT INTO public."District" ("name") VALUES('Santa Rita de Cássia');
INSERT INTO public."District" ("name") VALUES('Califórnia');
INSERT INTO public."District" ("name") VALUES('Nova Granada');
INSERT INTO public."District" ("name") VALUES('Lagoinha Leblon');
INSERT INTO public."District" ("name") VALUES('Horto Florestal');
INSERT INTO public."District" ("name") VALUES('Jardim Montanhês');
INSERT INTO public."District" ("name") VALUES('Juliana');
INSERT INTO public."District" ("name") VALUES('São Salvador');
INSERT INTO public."District" ("name") VALUES('Coração de Jesus');
INSERT INTO public."District" ("name") VALUES('Silveira');
INSERT INTO public."District" ("name") VALUES('Olaria');
INSERT INTO public."District" ("name") VALUES('Pompéia');
INSERT INTO public."District" ("name") VALUES('Vila CEMIG');
INSERT INTO public."District" ("name") VALUES('Nova Cintra');
INSERT INTO public."District" ("name") VALUES('Castanheira');
INSERT INTO public."District" ("name") VALUES('Palmares');
INSERT INTO public."District" ("name") VALUES('Cinquentenário');
INSERT INTO public."District" ("name") VALUES('Bandeirantes');
INSERT INTO public."District" ("name") VALUES('Santa Helena');
INSERT INTO public."District" ("name") VALUES('Santa Branca');
INSERT INTO public."District" ("name") VALUES('Vila Maria');
INSERT INTO public."District" ("name") VALUES('Alto Barroca');
INSERT INTO public."District" ("name") VALUES('Vista Alegre');
INSERT INTO public."District" ("name") VALUES('Vista do Sol');
INSERT INTO public."District" ("name") VALUES('Aparecida Sétima Seção');
INSERT INTO public."District" ("name") VALUES('Saudade');
INSERT INTO public."District" ("name") VALUES('Lajedo');
INSERT INTO public."District" ("name") VALUES('Graça');
INSERT INTO public."District" ("name") VALUES('São Luíz');
INSERT INTO public."District" ("name") VALUES('Estrela do Oriente');
INSERT INTO public."District" ("name") VALUES('Nova Cachoeirinha');
INSERT INTO public."District" ("name") VALUES('Ipê');
INSERT INTO public."District" ("name") VALUES('Urca');
INSERT INTO public."District" ("name") VALUES('Bairro Novo das Indústrias');
INSERT INTO public."District" ("name") VALUES('Boa Viagem');
INSERT INTO public."District" ("name") VALUES('Estoril');
INSERT INTO public."District" ("name") VALUES('Nova Floresta');
INSERT INTO public."District" ("name") VALUES('Monsenhor Messias');
INSERT INTO public."District" ("name") VALUES('Liberdade');
INSERT INTO public."District" ("name") VALUES('Madre Gertrudes');
INSERT INTO public."District" ("name") VALUES('Pedreira Prado Lopes');
INSERT INTO public."District" ("name") VALUES('Bonfim');
INSERT INTO public."District" ("name") VALUES('Nova Esperança');
INSERT INTO public."District" ("name") VALUES('Conjunto Minascaixa');
INSERT INTO public."District" ("name") VALUES('São Francisco');
INSERT INTO public."District" ("name") VALUES('Solar do Barreiro');
INSERT INTO public."District" ("name") VALUES('Nossa Senhora da Aparecida');
INSERT INTO public."District" ("name") VALUES('Trevo');
INSERT INTO public."District" ("name") VALUES('Confisco');
INSERT INTO public."District" ("name") VALUES('Dom Cabral');
INSERT INTO public."District" ("name") VALUES('Mineirão');
INSERT INTO public."District" ("name") VALUES('Dom Silvério');
INSERT INTO public."District" ("name") VALUES('Fernão Dias');
INSERT INTO public."District" ("name") VALUES('Ouro Minas');
INSERT INTO public."District" ("name") VALUES('Beira-Linha');
INSERT INTO public."District" ("name") VALUES('Santana do Cafezal');
INSERT INTO public."District" ("name") VALUES('Jaraguá');
INSERT INTO public."District" ("name") VALUES('Vila Primeiro de Maio');
INSERT INTO public."District" ("name") VALUES('Eymard');
INSERT INTO public."District" ("name") VALUES('Novo São Lucas');
INSERT INTO public."District" ("name") VALUES('Lagoinha');
INSERT INTO public."District" ("name") VALUES('Vera Cruz');
INSERT INTO public."District" ("name") VALUES('Maria Virgínia');
INSERT INTO public."District" ("name") VALUES('Carmo');
INSERT INTO public."District" ("name") VALUES('Oeste');
INSERT INTO public."District" ("name") VALUES('São Paulo');
INSERT INTO public."District" ("name") VALUES('Conjunto Jatobá');
INSERT INTO public."District" ("name") VALUES('Fazendinha');
INSERT INTO public."District" ("name") VALUES('São Bento');
INSERT INTO public."District" ("name") VALUES('Vila Novo São Lucas');
INSERT INTO public."District" ("name") VALUES('Leonina');
INSERT INTO public."District" ("name") VALUES('Bom Jesus');
INSERT INTO public."District" ("name") VALUES('Granja de Freitas');
INSERT INTO public."District" ("name") VALUES('Vila Paris');
INSERT INTO public."District" ("name") VALUES('Mariano de Abreu');
INSERT INTO public."District" ("name") VALUES('Minas Brasil');
INSERT INTO public."District" ("name") VALUES('Monte Azul');
INSERT INTO public."District" ("name") VALUES('Mangueiras');
INSERT INTO public."District" ("name") VALUES('Inconfidência');
INSERT INTO public."District" ("name") VALUES('Ermelinda');
INSERT INTO public."District" ("name") VALUES('Jatobá');
INSERT INTO public."District" ("name") VALUES('Vitória');
INSERT INTO public."District" ("name") VALUES('Horto');
INSERT INTO public."District" ("name") VALUES('Taquaril');
INSERT INTO public."District" ("name") VALUES('Conjunto Califórnia I');
INSERT INTO public."District" ("name") VALUES('Indaiá');
INSERT INTO public."District" ("name") VALUES('Barroca');
INSERT INTO public."District" ("name") VALUES('Dom Joaquim');
INSERT INTO public."District" ("name") VALUES('Pirajá');
INSERT INTO public."District" ("name") VALUES('Conjunto Paulo VI');
INSERT INTO public."District" ("name") VALUES('Alto dos Pinheiros');
INSERT INTO public."District" ("name") VALUES('Parque São José');
INSERT INTO public."District" ("name") VALUES('Vila Califórnia');
INSERT INTO public."District" ("name") VALUES('Novo Tupi');
INSERT INTO public."District" ("name") VALUES('Vila Independência I');
INSERT INTO public."District" ("name") VALUES('Conjunto Jardim Filadélfia');
INSERT INTO public."District" ("name") VALUES('São Lucas');
INSERT INTO public."District" ("name") VALUES('Vila Sumaré');
INSERT INTO public."District" ("name") VALUES('São Cristóvão');
INSERT INTO public."District" ("name") VALUES('Aarão Reis');
INSERT INTO public."District" ("name") VALUES('Pilar');
INSERT INTO public."District" ("name") VALUES('Santa Cecília');
INSERT INTO public."District" ("name") VALUES('Marajó');
INSERT INTO public."District" ("name") VALUES('Flávio de Oliveira');
INSERT INTO public."District" ("name") VALUES('São Jorge III');
INSERT INTO public."District" ("name") VALUES('Senhor dos Passos');
INSERT INTO public."District" ("name") VALUES('Universo');
INSERT INTO public."District" ("name") VALUES('Santa Rita');
INSERT INTO public."District" ("name") VALUES('Santa Sofia');
INSERT INTO public."District" ("name") VALUES('Conjunto Capitão Eduardo');
INSERT INTO public."District" ("name") VALUES('Campo Alegre');
INSERT INTO public."District" ("name") VALUES('Vila Jardim Alvorada');
INSERT INTO public."District" ("name") VALUES('São Jorge II');
INSERT INTO public."District" ("name") VALUES('Conjunto Celso Machado');
INSERT INTO public."District" ("name") VALUES('Venda Nova');
INSERT INTO public."District" ("name") VALUES('Pongelupe');
INSERT INTO public."District" ("name") VALUES('Zilah Spósito');
INSERT INTO public."District" ("name") VALUES('Canaã');
INSERT INTO public."District" ("name") VALUES('São Gonçalo');
INSERT INTO public."District" ("name") VALUES('Jonas Veiga');
INSERT INTO public."District" ("name") VALUES('Acaiaca');
INSERT INTO public."District" ("name") VALUES('Vila São João Batista');
INSERT INTO public."District" ("name") VALUES('Primeiro de Maio');
INSERT INTO public."District" ("name") VALUES('Novo Santa Cecília');
INSERT INTO public."District" ("name") VALUES('Etelvina Carneiro');
INSERT INTO public."District" ("name") VALUES('Parque São Pedro');
INSERT INTO public."District" ("name") VALUES('Santa Margarida');
INSERT INTO public."District" ("name") VALUES('Cenáculo');
INSERT INTO public."District" ("name") VALUES('Vila Nova Cachoeirinha I');
INSERT INTO public."District" ("name") VALUES('Belmonte');
INSERT INTO public."District" ("name") VALUES('Penha');
INSERT INTO public."District" ("name") VALUES('Alpes');
INSERT INTO public."District" ("name") VALUES('Petropolis');
INSERT INTO public."District" ("name") VALUES('Mariquinhas');
INSERT INTO public."District" ("name") VALUES('Esperança');
INSERT INTO public."District" ("name") VALUES('Ernesto do Nascimento');
INSERT INTO public."District" ("name") VALUES('Vila Santa Mônica');
INSERT INTO public."District" ("name") VALUES('Vila Aeroporto');
INSERT INTO public."District" ("name") VALUES('Granja Werneck');
INSERT INTO public."District" ("name") VALUES('Braúnas');
INSERT INTO public."District" ("name") VALUES('Águas Claras');
INSERT INTO public."District" ("name") VALUES('Alta Tensão I');
INSERT INTO public."District" ("name") VALUES('Frei Leopoldo');
INSERT INTO public."District" ("name") VALUES('Universitário');
INSERT INTO public."District" ("name") VALUES('Suzana');
INSERT INTO public."District" ("name") VALUES('Mangabeiras');
INSERT INTO public."District" ("name") VALUES('Vila Madre Gertrudes I');
INSERT INTO public."District" ("name") VALUES('Vila Mangueiras');
INSERT INTO public."District" ("name") VALUES('Barão Homem de Melo I');
INSERT INTO public."District" ("name") VALUES('Vila São Paulo');
INSERT INTO public."District" ("name") VALUES('Túnel de Ibirité');
INSERT INTO public."District" ("name") VALUES('Imbaúbas');
INSERT INTO public."District" ("name") VALUES('Ademar Maldonado');
INSERT INTO public."District" ("name") VALUES('Itatiaia');
INSERT INTO public."District" ("name") VALUES('João Paulo II');
INSERT INTO public."District" ("name") VALUES('Comiteco');
INSERT INTO public."District" ("name") VALUES('Conjunto Califórnia II');
INSERT INTO public."District" ("name") VALUES('Jardinópolis');
INSERT INTO public."District" ("name") VALUES('São Jorge I');
INSERT INTO public."District" ("name") VALUES('Vila Ecológica');
INSERT INTO public."District" ("name") VALUES('Vila Jardim São José');
INSERT INTO public."District" ("name") VALUES('Vila Piratininga');
INSERT INTO public."District" ("name") VALUES('São João');
INSERT INTO public."District" ("name") VALUES('Biquinhas');
INSERT INTO public."District" ("name") VALUES('Tiradentes');
INSERT INTO public."District" ("name") VALUES('Pousada Santo Antônio');
INSERT INTO public."District" ("name") VALUES('Vila Nossa Senhora Aparecida');
INSERT INTO public."District" ("name") VALUES('Vila Antena');
INSERT INTO public."District" ("name") VALUES('São Benedito');
INSERT INTO public."District" ("name") VALUES('Estrela');
INSERT INTO public."District" ("name") VALUES('Vila Átila de Paiva');
INSERT INTO public."District" ("name") VALUES('Olhos d''água');
INSERT INTO public."District" ("name") VALUES('Vila Coqueiral');
INSERT INTO public."District" ("name") VALUES('Cidade Jardim');
INSERT INTO public."District" ("name") VALUES('Vila Trinta e Um de Março');
INSERT INTO public."District" ("name") VALUES('São José');
INSERT INTO public."District" ("name") VALUES('Solimões');
INSERT INTO public."District" ("name") VALUES('Bernadete');
INSERT INTO public."District" ("name") VALUES('Xodó-Marize');
INSERT INTO public."District" ("name") VALUES('Vila da Luz');
INSERT INTO public."District" ("name") VALUES('Jardim Atlântico');
INSERT INTO public."District" ("name") VALUES('Vila Formosa');
INSERT INTO public."District" ("name") VALUES('Vila Nova Gameleira II');
INSERT INTO public."District" ("name") VALUES('Vila Santa Rosa');
INSERT INTO public."District" ("name") VALUES('Engenho Nogueira');
INSERT INTO public."District" ("name") VALUES('Vila Copacabana');
INSERT INTO public."District" ("name") VALUES('São Francisco das Chagas');
INSERT INTO public."District" ("name") VALUES('Vila Oeste');
INSERT INTO public."District" ("name") VALUES('Aeroporto');
INSERT INTO public."District" ("name") VALUES('Beija Flor');
INSERT INTO public."District" ("name") VALUES('Capitão Eduardo');
INSERT INTO public."District" ("name") VALUES('Marieta I');
INSERT INTO public."District" ("name") VALUES('Átila de Paiva');
INSERT INTO public."District" ("name") VALUES('Vila São Rafael');
INSERT INTO public."District" ("name") VALUES('Vitória da Conquista');
INSERT INTO public."District" ("name") VALUES('Acaba Mundo');
INSERT INTO public."District" ("name") VALUES('Conjunto Santa Maria');
INSERT INTO public."District" ("name") VALUES('Jardim do Vale');
INSERT INTO public."District" ("name") VALUES('Monte São José');
INSERT INTO public."District" ("name") VALUES('Álvaro Camargos');
INSERT INTO public."District" ("name") VALUES('Sport Club');
INSERT INTO public."District" ("name") VALUES('Bairro das Indústrias II');
INSERT INTO public."District" ("name") VALUES('Conjunto Bonsucesso');
INSERT INTO public."District" ("name") VALUES('Vila Dias');
INSERT INTO public."District" ("name") VALUES('Vila Esplanada');
INSERT INTO public."District" ("name") VALUES('Vila Independência II');
INSERT INTO public."District" ("name") VALUES('Vila de Sá');
INSERT INTO public."District" ("name") VALUES('Garças');
INSERT INTO public."District" ("name") VALUES('Vila Boa Vista');
INSERT INTO public."District" ("name") VALUES('Delta');
INSERT INTO public."District" ("name") VALUES('Corumbiara');
INSERT INTO public."District" ("name") VALUES('Madri');
INSERT INTO public."District" ("name") VALUES('Pantanal');
INSERT INTO public."District" ("name") VALUES('Conjunto Floramar');
INSERT INTO public."District" ("name") VALUES('Vila Pilar');
INSERT INTO public."District" ("name") VALUES('Vila Olhos d''água');
INSERT INTO public."District" ("name") VALUES('Marilândia');
INSERT INTO public."District" ("name") VALUES('Virgínia');
INSERT INTO public."District" ("name") VALUES('Vila Minaslândia');
INSERT INTO public."District" ("name") VALUES('Vila Nova Gameleira I');
INSERT INTO public."District" ("name") VALUES('Vila dos Anjos');
INSERT INTO public."District" ("name") VALUES('Ambrosina');
INSERT INTO public."District" ("name") VALUES('Andiroba');
INSERT INTO public."District" ("name") VALUES('Marmiteiros');
INSERT INTO public."District" ("name") VALUES('Guaratã');
INSERT INTO public."District" ("name") VALUES('Vila União');
INSERT INTO public."District" ("name") VALUES('Vila Mantiqueira');
INSERT INTO public."District" ("name") VALUES('Conjunto Novo Dom Bosco');
INSERT INTO public."District" ("name") VALUES('Vila Nova Paraíso');
INSERT INTO public."District" ("name") VALUES('Vila Paquetá');
INSERT INTO public."District" ("name") VALUES('Vila Inestan');
INSERT INTO public."District" ("name") VALUES('Vila São Gabriel Jacuí');
INSERT INTO public."District" ("name") VALUES('Vila Nova Cachoeirinha IV');
INSERT INTO public."District" ("name") VALUES('Vila Real II');
INSERT INTO public."District" ("name") VALUES('Vila Nossa Senhora do Rosário');
INSERT INTO public."District" ("name") VALUES('Vila Santo Antônio Barroquinha');
INSERT INTO public."District" ("name") VALUES('Vila Madre Gertrudes II');
INSERT INTO public."District" ("name") VALUES('Bela Vitória');
INSERT INTO public."District" ("name") VALUES('Vila Maloca');
INSERT INTO public."District" ("name") VALUES('Conjunto Lagoa');
INSERT INTO public."District" ("name") VALUES('Vila Suzana I');
INSERT INTO public."District" ("name") VALUES('Distrito Industrial do Jatobá');
INSERT INTO public."District" ("name") VALUES('Pirineus');
INSERT INTO public."District" ("name") VALUES('Vila Aeroporto Jaraguá');
INSERT INTO public."District" ("name") VALUES('Vila Nova');
INSERT INTO public."District" ("name") VALUES('Vila Ouro Minas');
INSERT INTO public."District" ("name") VALUES('Três Marias');
INSERT INTO public."District" ("name") VALUES('Vila Nova dos Milionários');
INSERT INTO public."District" ("name") VALUES('Mirante');
INSERT INTO public."District" ("name") VALUES('Vila Bandeirantes');
INSERT INTO public."District" ("name") VALUES('Boa Esperança');
INSERT INTO public."District" ("name") VALUES('Vila da Paz');
INSERT INTO public."District" ("name") VALUES('Vila Calafate');
INSERT INTO public."District" ("name") VALUES('São Vicente');
INSERT INTO public."District" ("name") VALUES('Novo Ouro Preto');
INSERT INTO public."District" ("name") VALUES('Canadá');
INSERT INTO public."District" ("name") VALUES('Antônio Ribeiro de Abreu');
INSERT INTO public."District" ("name") VALUES('Satélite');
INSERT INTO public."District" ("name") VALUES('Vila Antena Montanhês');
INSERT INTO public."District" ("name") VALUES('Grotinha');
INSERT INTO public."District" ("name") VALUES('Cônego Pinheiro');
INSERT INTO public."District" ("name") VALUES('Chácara Leonina');
INSERT INTO public."District" ("name") VALUES('Vila Madre Gertrudes III');
INSERT INTO public."District" ("name") VALUES('Vila São Gabriel');
INSERT INTO public."District" ("name") VALUES('Vila Paraíso');
INSERT INTO public."District" ("name") VALUES('Ápia');
INSERT INTO public."District" ("name") VALUES('Vila da Amizade');
INSERT INTO public."District" ("name") VALUES('Alta Tensão');
INSERT INTO public."District" ("name") VALUES('João Alfredo');
INSERT INTO public."District" ("name") VALUES('Alto das Antenas');
INSERT INTO public."District" ("name") VALUES('Maria Teresa');
INSERT INTO public."District" ("name") VALUES('Caetano Furquim');
INSERT INTO public."District" ("name") VALUES('Vila Independência IV');
INSERT INTO public."District" ("name") VALUES('Unidas');
INSERT INTO public."District" ("name") VALUES('Vila Piratininga Venda Nova');
INSERT INTO public."District" ("name") VALUES('São Sebastião');
INSERT INTO public."District" ("name") VALUES('Nova Pampulha');
INSERT INTO public."District" ("name") VALUES('Vila Havaí');
INSERT INTO public."District" ("name") VALUES('Mirtes');
INSERT INTO public."District" ("name") VALUES('Serra do Rola Moça');
INSERT INTO public."District" ("name") VALUES('Vila SESC');
INSERT INTO public."District" ("name") VALUES('Morro dos Macacos');
INSERT INTO public."District" ("name") VALUES('Vila da Área');
INSERT INTO public."District" ("name") VALUES('Vila Santo Antônio');
INSERT INTO public."District" ("name") VALUES('Flamengo');
INSERT INTO public."District" ("name") VALUES('Gameleira');
INSERT INTO public."District" ("name") VALUES('Vila COPASA');
INSERT INTO public."District" ("name") VALUES('São Damião');
INSERT INTO public."District" ("name") VALUES('Custodinha');
INSERT INTO public."District" ("name") VALUES('Boa União I');
INSERT INTO public."District" ("name") VALUES('Conjunto São Francisco de Assis');
INSERT INTO public."District" ("name") VALUES('Vila Petrópolis');
INSERT INTO public."District" ("name") VALUES('Conjunto Providência');
INSERT INTO public."District" ("name") VALUES('Marieta II');
INSERT INTO public."District" ("name") VALUES('Vila Engenho Nogueira');
INSERT INTO public."District" ("name") VALUES('Vila Jardim Montanhês');
INSERT INTO public."District" ("name") VALUES('Vila das Oliveiras');
INSERT INTO public."District" ("name") VALUES('Conjunto Serra Verde');
INSERT INTO public."District" ("name") VALUES('Camponesa III');
INSERT INTO public."District" ("name") VALUES('Vila Jardim Leblon');
INSERT INTO public."District" ("name") VALUES('Vila Tirol');
INSERT INTO public."District" ("name") VALUES('Barão Homem de Melo III');
INSERT INTO public."District" ("name") VALUES('CDI Jatobá');
INSERT INTO public."District" ("name") VALUES('Vila Madre Gertrudes V');
INSERT INTO public."District" ("name") VALUES('Vila Rica');
INSERT INTO public."District" ("name") VALUES('Grota');
INSERT INTO public."District" ("name") VALUES('Vila Betânia');
INSERT INTO public."District" ("name") VALUES('Vila São Dimas');
INSERT INTO public."District" ("name") VALUES('Vila Batik');
INSERT INTO public."District" ("name") VALUES('Barão Homem de Melo IV');
INSERT INTO public."District" ("name") VALUES('Vila Ipiranga');
INSERT INTO public."District" ("name") VALUES('Vila São Geraldo');
INSERT INTO public."District" ("name") VALUES('Boa União II');
INSERT INTO public."District" ("name") VALUES('Cidade Jardim Taquaril');
INSERT INTO public."District" ("name") VALUES('Nossa Senhora do Rosário');
INSERT INTO public."District" ("name") VALUES('Vila Canto do Sabiá');
INSERT INTO public."District" ("name") VALUES('Laranjeiras');
INSERT INTO public."District" ("name") VALUES('Pindura Saia');
INSERT INTO public."District" ("name") VALUES('Vila Nova Cachoeirinha II');
INSERT INTO public."District" ("name") VALUES('Vila do Pombal');
INSERT INTO public."District" ("name") VALUES('Santa Isabel');
INSERT INTO public."District" ("name") VALUES('Vila Satélite');
INSERT INTO public."District" ("name") VALUES('Várzea da Palma');
INSERT INTO public."District" ("name") VALUES('Camponesa I');
INSERT INTO public."District" ("name") VALUES('Vila Real I');
INSERT INTO public."District" ("name") VALUES('Bacurau');
INSERT INTO public."District" ("name") VALUES('Nova América');
INSERT INTO public."District" ("name") VALUES('Vila Nova Gameleira III');
INSERT INTO public."District" ("name") VALUES('Lorena');
INSERT INTO public."District" ("name") VALUES('Vila PUC');
INSERT INTO public."District" ("name") VALUES('Vila FUMEC');
INSERT INTO public."District" ("name") VALUES('Vila São Francisco');
INSERT INTO public."District" ("name") VALUES('Mala e Cuia');
INSERT INTO public."District" ("name") VALUES('Vila Suzana II');
INSERT INTO public."District" ("name") VALUES('Maravilha');
INSERT INTO public."District" ("name") VALUES('Cônego Pinheiro A');
INSERT INTO public."District" ("name") VALUES('Baleia');
INSERT INTO public."District" ("name") VALUES('Xangri-lá');
INSERT INTO public."District" ("name") VALUES('Belém');
INSERT INTO public."District" ("name") VALUES('Bispo de Maura');
INSERT INTO public."District" ("name") VALUES('Campus UFMG');
INSERT INTO public."District" ("name") VALUES('Guanabara');
INSERT INTO public."District" ("name") VALUES('Lagoa da Pampulha');
INSERT INTO public."District" ("name") VALUES('Sumaré');
INSERT INTO public."District" ("name") VALUES('Vila Vera Cruz I');
INSERT INTO public."District" ("name") VALUES('Vila Vera Cruz II');




--DELETE 
DELETE FROM "Management";
DELETE FROM "Property";
--DELETE FROM "Type";
--DELETE FROM "Goal";
--DELETE FROM "City";
DELETE FROM "District";

--DROP
DROP TABLE "Management";
DROP TABLE "Property";
DROP TABLE "Type";
DROP TABLE "Goal";
DROP TABLE "City";
DROP TABLE "District";