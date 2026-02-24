SELECT  idCliente, QtdePontos,
    CASE WHEN QtdePontos = 100 THEN 1 ELSE 0 END AS SemPontos
FROM clientes