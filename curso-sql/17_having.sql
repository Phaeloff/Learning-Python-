SELECT idCliente,
        count(IdTransacao),
        sum(qtdePontos)
FROM transacoes

WHERE DtCriacao >= '2025-07-01'
AND DtCriacao < '2025-08-01'

GROUP BY idCliente
HAVING sum(qtdePontos) >= 2000

ORDER BY sum(qtdePontos) DESC;

