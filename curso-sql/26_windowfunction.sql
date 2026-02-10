WITH tb_sumario_dias as(

SELECT substr(DtCriacao, 1, 10) AS dtDia,
    count(DISTINCT IdTransacao) AS qtdTransacoes
FROM transacoes

WHERE DtCriacao >= '2025-08-25' AND DtCriacao < '2025-08-30'

GROUP BY dtDia

)

SELECT *,
    sum(qtdTransacoes) OVER (PARTITION BY 1 ORDER BY dtDia) AS qtdTransacoesAcumulada

FROM tb_sumario_dias