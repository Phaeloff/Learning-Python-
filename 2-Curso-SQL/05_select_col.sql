SELECT idCliente,
        -- QtdePontos,
        -- QtdePontos + 10 AS NovoSaldo,
        -- QtdePontos * 10 AS QtdePontosVezes10,
        DtCriacao,
        datetime(substr(DtCriacao, 1, 10)) AS DatadeCriacao,
        strftime('%w', datetime(substr(DtCriacao, 1, 10))) AS DiaSemana
FROM clientes