SELECT IdCliente, QtdePontos,
    CASE
        WHEN QtdePontos < 10 THEN 'BAIXO'
        WHEN QtdePontos >11 AND QtdePontos < 500 THEN 'MEDIO'
        ELSE 'ALTO'
    END AS NivelPontuacao
FROM transacoes

ORDER BY  QtdePontos DESC;