/*INSERT INTO pokemon ( pokemon_id, nome, peso, valor_ataque, valor_defesa, velocidade_media, especie_especie_id, categoria_categoria_id) 
VALUES ( pokemon_id, "nome", peso, valor_ataque, valor_defesa, velocidade_media, especie_especie_id, categoria_categoria_id);

INSERT INTO pokemon_tipo (pokemon_pokemon_id, tipo_tipo_id, nivel) VALUES ( , , );

INSERT INTO pokemon_habilidade (pokemon_pokemon_id, habilida_habilidade_id, oculta) VALUES ( , ,);

-- VALUES ( pokemon_id, "nome", peso, valor_ataque, valor_defesa, velocidade_media, especie_especie_id, categoria_categoria_id);
*/

INSERT INTO pokemon ( pokemon_id, nome, peso, valor_ataque, valor_defesa, velocidade_media, especie_especie_id, categoria_categoria_id) 
VALUES ( pokemon_id, "nome", peso, valor_ataque, valor_defesa, velocidade_media, (SELECT especie_id FROM especie WHERE nome = ""), (SELECT categoria_id FROM categoria WHERE nome = ""));

INSERT INTO pokemon_tipo (pokemon_pokemon_id, tipo_tipo_id, nivel) VALUES ( ,(SELECT tipo_id FROM tipo WHERE nome = "", );