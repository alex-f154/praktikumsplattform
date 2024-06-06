#CREATE database	praktikumsplattform;
#USE praktikumsplattform;

CREATE TABLE schueler
	(schuelerid INT auto_increment PRIMARY KEY,
    username_schueler VARCHAR(16),
    password_schueler VARCHAR(16),
    wunschberuf VARCHAR(30),
    strasse VARCHAR(30),
    Ort VARCHAR(30)
    );
CREATE TABLE betriebe
	(betriebid INT auto_increment PRIMARY KEY,
    username_betrieb VARCHAR(16),
    password_betrieb VARCHAR(16),
    strasse VARCHAR(30),
    Ort VARCHAR(30)
    );
CREATE TABLE orte
	(ortid INT auto_increment PRIMARY KEY,
    ortname VARCHAR(255),
    PLZ INT(5)
    );
    
ALTER TABLE schueler
	ADD FOREIGN KEY (Ort) REFERENCES orte (OrtID)
    ;
ALTER TABLE betriebe
	ADD FOREIGN KEY (Ort) REFERENCES orte (OrtID)
    ;