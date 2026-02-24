
SELECT *

FROM transacao_produto as t1

WHERE t1.IdProduto IN (

SELECT IdProduto

FROM produtos

WHERE DescNomeProduto = 'Resgatar Ponei'
)