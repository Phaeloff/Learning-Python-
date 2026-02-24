SELECT  idCliente, QtdePontos,DtCriacao,

        strftime('%w', datetime(substr(DtCriacao, 1, 19))) AS Datacriada
FROM clientes

WHERE Datacriada = '0' OR Datacriada = '6';