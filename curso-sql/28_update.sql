SELECT * from relatorio_diario;

UPDATE relatorio_diario
SET qtdTransacao = 100000
WHERE dtDia >= '2025-08-25'
;

SELECT * FROM relatorio_diario;