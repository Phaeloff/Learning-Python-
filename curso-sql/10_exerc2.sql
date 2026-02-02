SELECT  idCliente, QtdePontos,
        CASE WHEN QtdePontos = 1 THEN 1 ELSE 0 END AS TemUmPonto
FROM clientes

WHERE QtdePontos = 1;