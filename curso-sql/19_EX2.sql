-- quantos clientes tem e-mail cadastrado.
SELECT idCliente,
    sum(flEmail) AS totalEmails

FROM clientes