
-- Quem participu da primeira aula do curso no dia '2025-08-25'
WITH tb_prim_dia AS (
    SELECT DISTINCT idCliente
    FROM transacoes
    WHERE substr(DtCriacao, 1,10) = '2025-08-25'
),

-- Dias em que cada cliente esteve presente no curso

tb_dias_curso AS (
    SELECT DISTINCT
    idCliente, substr(DtCriacao, 1,10) AS presenteDia
    FROM transacoes
    WHERE substr(DtCriacao, 1,10) >= '2025-08-25'
    AND substr(DtCriacao, 1,10) < '2025-08-30'
    ORDER BY idCliente, presenteDia
),

-- contando quantas vezes quem participou da primeira aula esteve presente n curso e voltou

tb_cliente_dias AS (
    SELECT t1.idCliente,
        count(DISTINCT t2.presenteDia) AS qtdDias
    FROM tb_prim_dia AS t1
    LEFT JOIN tb_dias_curso AS t2
    ON t1.idCliente = t2.idCliente
    GROUP BY t1.idCliente
)

-- calculando a média de dias que os clientes que participaram da primeira aula estiveram presentes no curso
SELECT avg(qtdDias) FROM tb_cliente_dias
