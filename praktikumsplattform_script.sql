CREATE DATABASE Praktikumsplattform;
USE Praktikumsplattform;

CREATE TABLE Ort (
    OrtID INT PRIMARY KEY,
    OrtName VARCHAR(100),
    PLZ VARCHAR(10)
);

CREATE TABLE Betrieb (
    BetriebID INT PRIMARY KEY,
    Strasse VARCHAR(100),
    Username_Betrieb VARCHAR(100),
    Passwort VARCHAR(100),
    OrtID INT,
    FOREIGN KEY (OrtID) REFERENCES Ort(OrtID)
);

CREATE TABLE Schueler (
    SchuelerID INT PRIMARY KEY,
    Wunschberuf VARCHAR(100),
    Strasse VARCHAR(100),
    Username_Schueler VARCHAR(100),
    Passwort VARCHAR(100),
    OrtID INT,
    FOREIGN KEY (OrtID) REFERENCES Ort(OrtID)
);

CREATE TABLE Praktikumsplatz (
    PlatzID INT PRIMARY KEY,
    Verfügbarkeit DATE,
    Bezahlung DECIMAL(10, 2),
    Zeitraum VARCHAR(100),
    Beruf VARCHAR(100),
    BetriebID INT,
    FOREIGN KEY (BetriebID) REFERENCES Betriebe(BetriebID)
);

CREATE TABLE HWK_Kronenburg (
    Benutzername VARCHAR(100) PRIMARY KEY,
    Passwort VARCHAR(100)
);

CREATE TABLE Bewerbungen (
    SchuelerID INT,
    PlatzID INT,
    PRIMARY KEY (SchuelerID, PlatzID),
    FOREIGN KEY (SchuelerID) REFERENCES Schueler(SchuelerID),
    FOREIGN KEY (PlatzID) REFERENCES Praktikumsplatz(PlatzID)
);
