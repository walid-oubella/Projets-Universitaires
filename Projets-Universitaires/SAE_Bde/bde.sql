CREATE TABLE Inventaire (
  idProduit INTEGER PRIMARY KEY,
  nomProduit VARCHAR(30) NOT NULL,
  quantite INTEGER NOT NULL,
  prix VARCHAR(30) NOT NULL,
  description VARCHAR(30) ) ;
 
CREATE TABLE Clients (
  idEtudiant INTEGER PRIMARY KEY,
  nom VARCHAR(30) NOT NULL,
  prenom VARCHAR(30) NOT NULL,
  password VARCHAR(30) NOT NULL,
  Formation VARCHAR(30) ) ;
 
CREATE TABLE Commande (
  idEtudiant INTEGER,
  idProduit INTEGER,
  FOREIGN KEY (idEtudiant) REFERENCES Clients(idEtudiant),
  FOREIGN KEY (idProduit) REFERENCES Inventaire(idProduit)) ;
 
CREATE TABLE Historique (
  idEtudiant INTEGER,
  idProduit INTEGER,
  date DATE,
  totalPrix INTEGER,
  FOREIGN KEY (idEtudiant) REFERENCES Clients(idEtudiant)) ;
 
CREATE TABLE Panier (
  idProduit INTEGER,
  idEtudiant INTEGER NOT NULL,
  nomProduit VARCHAR(30) NOT NULL,
  quantite INTEGER NOT NULL,
  prix INTEGER NOT NULL,
  description VARCHAR(30),
  FOREIGN KEY (idProduit) REFERENCES Inventaire(idProduit) ) ;