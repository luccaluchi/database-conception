-- junções de 2 ou mais tabelas, com ORDER BY
SELECT pokemon.nome, habilidade.nome AS habilidade
FROM pokemon
INNER JOIN pokemon_habilidade ON pokemon.pokemon_id = pokemon_habilidade.pokemon_pokemon_id
INNER JOIN habilidade ON pokemon_habilidade.habilidade_habilidade_id = habilidade.habilidade_id;

-- junções de 2 ou mais tabelas, com ORDER BY e filtros na cláusula WHERE
SELECT pokemon.nome, categoria.nome AS 'categoria(normal)'
FROM pokemon
INNER JOIN categoria ON pokemon.categoria_categoria_id = categoria.categoria_id WHERE categoria_id = 1;

-- junções de 3 ou mais tabelas, com ORDER BY e filtros na cláusula WHERE
SELECT p.nome, t.nome AS tipo, t.descricao
FROM tipo t
INNER JOIN pokemon_tipo tp ON t.tipo_id = tp.tipo_tipo_id
INNER JOIN pokemon p ON tp.pokemon_pokemon_id = p.pokemon_id WHERE t.nome = "Water" ORDER BY p.nome;

-- junção de 3 ou mais tabelas, usando os operadores LIKE e BETWEEN
SELECT p.nome, p.valor_ataque AS "valor de ataque", e.nome AS "espécie" , c.nome AS "categoria"
FROM pokemon p
INNER JOIN categoria c ON p.categoria_categoria_id = c.categoria_id
INNER JOIN especie e ON p.especie_especie_id = e.especie_id WHERE p.nome LIKE "Mega%" AND p.valor_ataque BETWEEN 30 and 150;

-- junção de 2 ou mais tabelas, usando os operadores IN e IS NULL/IS NOT NULL



