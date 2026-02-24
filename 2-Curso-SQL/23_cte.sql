WITH tb_cliente_primeiro_dia AS (
SELECT DISTINCT idCliente
FROM transacoes
WHERE substr(DtCriacao,1,10) = '2025-08-25'
),

tb_cliente_ultimos_dias AS (
SELECT DISTINCT idCliente
FROM transacoes
WHERE substr(DtCriacao,1,10) = '2025-08-29'
),

tb_join AS(

SELECT
t1.idCliente AS primeiroclientes,
t2.idCliente AS ultimosclientes

FROM tb_cliente_primeiro_dia AS t1

LEFT JOIN tb_cliente_ultimos_dias AS t2
ON t1.idCliente = t2.idCliente
)

SELECT count(primeiroclientes),
    count(ultimosclientes),
    1. * count(ultimosclientes)/ count(primeiroclientes) AS taxa_retorno
FROM tb_join