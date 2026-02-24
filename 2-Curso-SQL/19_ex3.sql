-- Qual cliente mais pontos positivos em 2025.
SELECT idCliente,

    count(qtdePontos) AS totalPontos

FROM clientes
WHERE DtCriacao >= '2025-01-01'
AND DtCriacao < '2025-06-01'
AND qtdePontos > 1
ORDER BY totalPontos DESC

LIMIT 1