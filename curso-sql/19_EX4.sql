-- Qual cliente fez mais transações no mês de maio de 2025?

SELECT idCliente,
    count(idTransacao) AS totalTransacoes

FROM transacoes

WHERE DtCriacao >= '2025-05-01'
AND DtCriacao < '2025-06-01'

GROUP BY idCliente

ORDER BY totalTransacoes DESC