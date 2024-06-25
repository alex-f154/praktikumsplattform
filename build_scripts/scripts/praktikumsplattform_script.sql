CREATE DATABASE Praktikumsplattform;
USE Praktikumsplattform;
 
 -- AUTO_INCREMENT = 1; setzen damit keine ID mit 0 belegt ist ausser bei Tabelle Bewerbungen

CREATE TABLE Betrieb (
    BetriebID INT AUTO_INCREMENT PRIMARY KEY,
    Strasse VARCHAR(100),
    Ort VARCHAR(100),
    Username_Betrieb VARCHAR(100),
    Passwort_Betrieb VARCHAR(100)) AUTO_INCREMENT = 1;
 
CREATE TABLE Schueler (
    SchuelerID INT AUTO_INCREMENT PRIMARY KEY,
    Wunschberuf VARCHAR(100),
    Strasse VARCHAR(100),
    Ort VARCHAR(100),
    Username_Schueler VARCHAR(100),
    Passwort_Schueler VARCHAR(100)) AUTO_INCREMENT = 1;
 
CREATE TABLE Praktikumsplatz (
    PlatzID INT AUTO_INCREMENT PRIMARY KEY,
    Beginn DATE,
    Bezahlung BOOLEAN,
    Zeitraum VARCHAR(100),
    Beruf VARCHAR(100),
    BetriebID INT,
    FOREIGN KEY (BetriebID) REFERENCES Betrieb(BetriebID)) AUTO_INCREMENT = 1;
 
CREATE TABLE HWK_Kronenburg (
    Benutzername VARCHAR(100) PRIMARY KEY,
    Passwort VARCHAR(100));
 
CREATE TABLE Bewerbungen (
    SchuelerID INT,
    PlatzID INT,
    PRIMARY KEY (SchuelerID, PlatzID),
    FOREIGN KEY (SchuelerID) REFERENCES Schueler(SchuelerID),
    FOREIGN KEY (PlatzID) REFERENCES Praktikumsplatz(PlatzID)) AUTO_INCREMENT = 1;
 
INSERT INTO Betrieb VALUES 
(1,"Olgastrasse 45","Heilbronn","Papier GmbH","Paperclip12."),
(2,"Rudi-Assauer-Strasse 1","Gelsenkirchen","Management AG","ganzvielgeld$"),
(3,"Bahnhofstrasse 40","Backnang","Gyros GmbH","123pita123"),
(4,"Quellweg 114","Sinsheim","Windpark OHG","whooosh456"),
(5,"Baldurs Tor 3","Faerun","Goblinschmiede GmbH & Co KG","mehrmehrimmermehr!");
 
INSERT INTO Schueler VALUES
(1,"Kaufmann für Büromanagement","Oststrasse 8","Heilbronn","Peter Schneider","binfertigihrnicht"),
(2,"Maurer","Inselgasse 10","Freudenstadt","Christopher Ronald","cr7great4eva"),
(3,"Schreiner","Holzweg 18","Holzmaden","German Hacker","hackermanishere"),
(4,"Zerspanungsmechanikerin","Hauptstrasse 178","Heidelberg","Louisa Müller","instaistsonice"),
(5,"Fachinformatiker für Systemintegration","Westweg 4","Dresden","Donald Biden","kanyemuskxx2xx"),
(6,"Kauffrau für Büromanagement","Hauptstrasse 63","Heilbronn","Felicitas Fitzgerald","fgleichbesterbuchstabe"),
(7,"Erzieherin","Hafenstraße 33","Heilbronn","Beatriz Lopez","backFromThailand"),
(8,"Polizist","Adolfstraße 2","Feuerbach","Murat Topac","DeutschlandBeste123"),
(9,"Zerspanungsmechaniker","Bahnhofstrasse 74","Frankfurt","Sofian Khalaila","Doppelapfelx2"),
(10,"Fachkraft für Lagerlogistik","Palisadenweg 5","Leipzig","Viktor Smirnov","workin4Jeffiscool");
 
INSERT INTO Praktikumsplatz VALUES
(1,'2024-10-01',FALSE,"3 Monate","Schreiner",5),
(2,'2024-09-01',TRUE,"4 Monate","Anlagenmechaniker",4),
(3,'2024-09-01',TRUE,"4 Monate","Kaufmann für Büromanagement",1),
(4,'2024-09-15',FALSE,"4 Wochen","Koch",3),
(5,'2024-10-01',TRUE,"2 Monate","Fachinformatiker für Systemintegration",2);
 
INSERT INTO HWK_Kronenburg VALUES
("Admin","adminadmin123"),
("ITSOL_extern","externinternusw");
 
INSERT INTO Bewerbungen VALUES
(1,3),
(10,4),
(3,1),
(8,4),
(5,5);