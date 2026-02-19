DROP TABLE IF EXISTS clientes_d28;

CREATE TABLE IF NOT EXISTS cliente_d28 (
    idCliente varchar(250) PRIMARY KEY,
    Qtdetransacoes INTERGER
);

INSERT INTO clientes_d28
SELECT idCliente,
    count(DISTINCT IdTransacao) AS Qtdetransacoes

FROM transacoes
WHERE julianday('now') - julianday(substr(DtCriacao, 1,10)) <= 28
GROUP BY IdCliente
;

SELECT * FROM clientes_d28;