WITH tb_transacoes AS (
    SELECT
            IdTransacao,
            idCliente,
            qtdePontos,
            datetime(substr(DtCriacao,1,19)) AS DtCriacao,
            julianday('now') - julianday (substr(DtCriacao,1,10)) AS diffDate,
            CAST(strftime('%H', substr(DtCriacao, 1,19)) AS INTEGER) AS dtHora
    FROM transacoes
),

tb_cliente AS (
    SELECT idCliente,
        datetime(substr(DtCriacao,1,19)) AS DtCriacao,
        julianday('now') - julianday (substr(DtCriacao,1,10)) AS idadeBase
        FROM clientes
),

tb_sumario_transacoes AS (
    SELECT idCliente,
        count(IdTransacao) as qtdeTransacoesVida,
        count(CASE WHEN diffDate <= 56 THEN IdTransacao END) AS qtdeTransacoes56Dias,
        count(CASE WHEN diffDate <= 28 THEN IdTransacao END) AS qtdeTransacoes28Dias,
        count(CASE WHEN diffDate <= 14 THEN IdTransacao END) AS qtdeTransacoes14Dias,
        count(CASE WHEN diffDate <= 7 THEN IdTransacao END) AS qtdeTransacoes7Dias,

        sum(qtdePontos) AS saldoPontos,

        min(diffDate) AS diasDesdeUltimaInteracao,

        sum(CASE WHEN QtdePontos > 0 THEN qtdePontos ELSE 0 END) AS qtdePontosPosVida,
        sum(CASE WHEN qtdePontos > 0 AND diffDate <= 56 THEN qtdePontos END) AS qtdePontosPos56Dias,
        sum(CASE WHEN qtdePontos > 0 AND diffDate <= 28 THEN qtdePontos END) AS qtdePontosPos28Dias,
        sum(CASE WHEN qtdePontos > 0 AND diffDate <= 14 THEN qtdePontos END) AS qtdePontosPos14Dias,
        sum(CASE WHEN qtdePontos > 0 AND diffDate <= 7 THEN qtdePontos END) AS qtdePontosPos7Dias,

        sum(CASE WHEN QtdePontos < 0 THEN qtdePontos ELSE 0 END) AS qtdePontosNegVida,
        sum(CASE WHEN qtdePontos < 0 AND diffDate <= 56 THEN qtdePontos END) AS qtdePontosNeg56Dias,
        sum(CASE WHEN qtdePontos < 0 AND diffDate <= 28 THEN qtdePontos END) AS qtdePontosNeg28Dias,
        sum(CASE WHEN qtdePontos < 0 AND diffDate <= 14 THEN qtdePontos END) AS qtdePontosNeg14Dias,
        sum(CASE WHEN qtdePontos < 0 AND diffDate <= 7 THEN qtdePontos END) AS qtdePontosNeg7Dias

    FROM tb_transacoes
    GROUP BY idCliente
),

tb_transacao_produto AS (

    SELECT
        t1.*,
        t3.DescNomeProduto,
        t3.DescCategoriaProduto
        
    FROM tb_transacoes AS t1

    LEFT JOIN transacao_produto AS t2
    ON t1.IdTransacao = t2.IdTransacao

    LEFT join produtos AS t3
    ON t2.IdProduto = t3.IdProduto

),

tb_cliente_produto AS(
    SELECT idCliente,
        DescNomeProduto,
        count(*) AS qtdeVida,
        count(CASE WHEN diffDate <= 56 THEN IdTransacao END) AS qtde56,
        count(CASE WHEN diffDate <= 28 THEN IdTransacao END) AS qtde28,
        count(CASE WHEN diffDate <= 14 THEN IdTransacao END) AS qtde14,
        count(CASE WHEN diffDate <= 7 THEN IdTransacao END) AS qtde7

    FROM tb_transacao_produto
    GROUP BY idCliente, DescNomeProduto
),

tb_cliente_produto_rn AS (
    SELECT *,
        row_number() OVER (PARTITION BY idCliente ORDER BY qtdeVida DESC) AS rankingVida,
        row_number() OVER (PARTITION BY idCliente ORDER BY qtde56 DESC) AS ranking56,
        row_number() OVER (PARTITION BY idCliente ORDER BY qtde28 DESC) AS ranking28,
        row_number() OVER (PARTITION BY idCliente ORDER BY qtde14 DESC) AS ranking14,
        row_number() OVER (PARTITION BY idCliente ORDER BY qtde7 DESC) AS ranking7

    FROM tb_cliente_produto
),

tb_cliente_dia AS (

    SELECT idCliente,
            strftime('%w', DtCriacao) AS dtDia,
            count(*) AS qtdTransacao

    FROM tb_transacoes
    WHERE diffDate <= 28
    GROUP BY idCliente, dtDia
),

tb_cliente_dia_rn AS(
SELECT *,
    ROW_NUMBER() OVER (PARTITION BY idCliente ORDER BY qtdTransacao DESC) AS rnDia

FROM tb_cliente_dia
),

tb_cliente_periodo AS(
    SELECT idCliente,
            CASE WHEN dtHora BETWEEN 7 AND 12 THEN 'MANHÃ'
            WHEN dtHora BETWEEN 12 AND 18 THEN 'TARDE'
            WHEN dtHora BETWEEN 18 AND 24 THEN 'NOITE'
            ELSE 'MADRUGADA'
            END AS periodo,
            COUNT(*) AS qtdTransacao
    FROM tb_transacoes
    WHERE diffDate <=28
GROUP BY 1,2
),

tb_cliente_perioso_rn as (
    SELECT *,
            ROW_NUMBER() OVER (PARTITION by IdCliente ORDER BY qtdTransacao DESC) AS rnPeriodo
    FROM tb_cliente_periodo
),




tb_join AS (
    SELECT
            t1.*,
            t2.idadeBase,
            t3.DescNomeProduto AS produtoMaisConsumidoVida,
            t4.DescNomeProduto AS produtos56,
            t5.DescNomeProduto AS produtos28,
            t6.DescNomeProduto AS produto14,
            t7.DescNomeProduto AS produto7,
            COALESCE(t8.dtDia, -1) AS dtDia,
            COALESCE(t9.Periodo, 'SEM INFORMAÇÂO') AS periodoMaisTransacao28
            


    FROM tb_sumario_transacoes AS t1

    LEFT JOIN tb_cliente AS t2
    ON t1.idCliente = t2.idCliente

    LEFT JOIN tb_cliente_produto_rn AS t3
    ON t1.idCliente = t3.idCliente AND t3.rankingVida = 1

    LEFT JOIN tb_cliente_produto_rn AS t4
    ON t1.idCliente = t4.idCliente AND
    t4.ranking56 = 1

    LEFT JOIN tb_cliente_produto_rn AS t5
    ON t1.idCliente = t5.idCliente AND
    t5.ranking28 = 1

    LEFT JOIN tb_cliente_produto_rn AS t6
    ON t1.idCliente = t6.idCliente AND
    t6.ranking14 = 1

    LEFT JOIN tb_cliente_produto_rn AS t7
    ON t1.idCliente = t7.idCliente AND
    t7.ranking7 = 1

    LEFT JOIN tb_cliente_dia_rn AS t8
    ON t1.IdCliente = t8.idCliente AND
    t8.rnDia = 1

    LEFT JOIN tb_cliente_perioso_rn AS t9
    ON t1.IdCliente = t9.idCliente AND
    t9.rnPeriodo = 1

)


SELECT *,
        1. * qtdeTransacoes28Dias / qtdeTransacoesVida AS engajamento28vida
FROM tb_join
