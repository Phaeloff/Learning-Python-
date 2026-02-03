SELECT idCliente,
    round(avg(qtdePontos),2) AS media_pontos,
    min(qtdePontos) AS min_pontos,
    max(qtdePontos) AS max_pontos,
    sum(flTwitch) AS max_twitch
FROM clientes