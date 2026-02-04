-- qual mes tivemos mais lista de presença assinada?
SELECT
        substr(t1.DtCriacao, 1, 7) AS mes_ano,
        count(DISTINCT t1.IdTransacao) AS total_listas_assinadas
        


FROM transacoes AS t1

LEFT JOIN transacao_produto as t2
ON t1.IdTransacao = t2.IdTransacao

LEFT JOIN produtos as t3
ON t2.IdProduto = t3.IdProduto

WHERE t3.DescNomeProduto = 'Lista de presença'

GROUP BY substr(t1.DtCriacao, 1, 7)

ORDER by total_listas_assinadas DESC