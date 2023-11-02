CREATE TABLE registros_contables(
	id INT AUTO_INCREMENT PRIMARY KEY,
    dia DATETIME,
    monto DECIMAL(10,2),
    motivo VARCHAR(255)
)

CREATE TABLE ingresos(
	id AUTO_INCREMENT PRIMARY KEY,
    mes VARCHAR(255),
    año INT,
    monto DECIMAL(10,2)
)

CREATE TABLE saldos(
	id AUTO_INCREMENT PRIMARY KEY,
    mes VARCHAR(255),
    año INT,
	ingresos DECIMAL(10,2),
    gastos DECIMAL(10,2),
    saldo DECIMAL(10,2)
)