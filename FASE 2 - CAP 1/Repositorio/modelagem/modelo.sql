-- Script de Criação do Banco de Dados para Monitoramento Agrícola

CREATE TABLE Cultura (
    ID_Cultura INT PRIMARY KEY,
    Nome VARCHAR(50) NOT NULL,
    Data_Plantio DATE NOT NULL,
    Data_Colheita DATE
);

CREATE TABLE Sensor (
    ID_Sensor INT PRIMARY KEY,
    Tipo VARCHAR(50) NOT NULL,
    Localizacao VARCHAR(100)
);

CREATE TABLE Leitura (
    ID_Leitura INT PRIMARY KEY,
    Data_Hora DATETIME NOT NULL,
    Valor FLOAT NOT NULL,
    ID_Sensor INT,
    ID_Cultura INT,
    FOREIGN KEY (ID_Sensor) REFERENCES Sensor(ID_Sensor),
    FOREIGN KEY (ID_Cultura) REFERENCES Cultura(ID_Cultura)
);

CREATE TABLE Ajuste (
    ID_Ajuste INT PRIMARY KEY,
    Tipo_Ajuste VARCHAR(50) NOT NULL,
    Data_Hora DATETIME NOT NULL,
    Quantidade FLOAT NOT NULL,
    ID_Cultura INT,
    FOREIGN KEY (ID_Cultura) REFERENCES Cultura(ID_Cultura)
);

CREATE TABLE Sensor_Ajuste (
    ID_Sensor INT,
    ID_Ajuste INT,
    PRIMARY KEY (ID_Sensor, ID_Ajuste),
    FOREIGN KEY (ID_Sensor) REFERENCES Sensor(ID_Sensor),
    FOREIGN KEY (ID_Ajuste) REFERENCES Ajuste(ID_Ajuste)
);

-- Inserção de Culturas Padrão
INSERT INTO Cultura (ID_Cultura, Nome, Data_Plantio, Data_Colheita) VALUES
(1, 'Soja', '2025-01-15', '2025-05-20'),
(2, 'Milho', '2025-02-10', '2025-06-15'),
(3, 'Cana de Açúcar', '2025-03-01', '2026-02-28'),
(4, 'Algodão', '2025-01-25', '2025-05-30'),
(5, 'Café', '2025-04-10', '2026-03-15'),
(6, 'Feijão', '2025-02-05', '2025-06-01'),
(7, 'Arroz', '2025-01-20', '2025-05-25');
