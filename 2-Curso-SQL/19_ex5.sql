-- Quantos produtos são de rpg?

select count(*) AS totalRPG

from produtos

where DescCategoriaProduto = 'rpg'