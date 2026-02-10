WITH cliente_dia AS(
    SELECT
        DISTINCT
        idCliente,
        substr(DtCriacao, 1, 10) AS dtDia
    FROM transacoes
    WHERE substr(DtCriacao, 1, 4) = '2025'
    ORDER BY idCliente, dtDia
),

tb_lag AS(
SELECT *,
    lag(dtDia) OVER (PARTITION BY idCliente ORDER BY dtDia) AS lagDia

FROM cliente_dia
),

tb_diff_dt AS (

SELECT *,
    julianday(dtDia) - julianday(lagDia) AS difDias
FROM tb_lag
),

avg_cliente as(
SELECT idCliente, avg(difDias) AS avgDias
FROM tb_diff_dt
GROUP BY idCliente
)

SELECT avg(avgDias) FROM avg_cliente