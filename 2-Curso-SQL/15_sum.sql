--APENAS QUANTO ENTROU PONTOS NO MÊS DE JULHO DE 2025

SELECT
    sum(QtdePontos),
    
    sum(CASE
        WHEN QtdePontos > 0 THEN qtdePontos
    END)AS TotalPontosJulho2025,

    sum(CASE
        WHEN QtdePontos < 0 THEN qtdePontos
    END) AS PontosUtilizadosJulho2025

FROM transacoes

WHERE DtCriacao >= '2025-07-01'
AND DtCriacao < '2025-08-01'

ORDER BY qtdePontos
