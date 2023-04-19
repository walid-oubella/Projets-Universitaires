set datestyle to "ISO , DMY";



drop table if exists reservations;
drop table if exists infosupclients;
drop table if exists clients;


CREATE TABLE clients(
IdPassager int PRIMARY KEY,
nom varchar(100),
sexe varchar(15),
age varchar);

CREATE TABLE reservations(
Ticket varchar(30),
Cabine varchar(100),
Pclass int,
Embarcation char(1),
Prix float,
primary key (Ticket,IdPassager),
IdPassager int,
foreign key (IdPassager) references clients(IdPassager));

CREATE TABLE infosupclients(
IdPassager int,
Survivant int,
SibSp int,
Parch int,
primary key (IdPassager),
foreign key (IdPassager) references clients(IdPassager));

\copy clients from clients.txt
\copy reservations from reservations.txt
\copy infosupclients from infosupclients.txt



