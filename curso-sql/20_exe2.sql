-- Em 2024, quantas transações de lovers foram realizadas em 2024?
SELECT
    t1.IdCliente,
    t2.IdProduto,
    count(t1.IdTransacao),
    t3.DescCategoriaProduto

FROM transacoes AS t1

LEFT JOIN transacao_produto AS t2
ON t1.IdTransacao = t2.IdTransacao

LEFT JOIN produtos AS t3
ON t2.IdProduto = t3.IdProduto

WHERE DtCriacao >= '2024-01-01' AND DtCriacao < '2024-12-31'
--AND t3.DescCategoriaProduto = 'lovers'

GROUP BY t3.DescCategoriaProduto
HAVING count(DISTINCT t1.IdTransacao) < 1000

ORDER BY count(DISTINCT t1.IdTransacao) DESC;


