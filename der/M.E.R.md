# M.E.R. 

## Descrição

- Cada Pokémon possui um nome, altura, peso, valor de ataque, valor de defesa, e uma velocidade média.
- Cada Pokémon pertence a uma categoria. A categoria indica se um Pokémon é comum, sub-lendário, lendário ou mítico.
- Cada categoria possui um nome e descrição.  Cada Pokémon pertence a uma única categoria. Por exemplo, o Pikachu pertence a categoria  “comum”, enquanto Mewtwo é um Pokémon “lendário”.
- Cada Pokémon pertence a uma espécie. Cada espécie possui um nome e descrição. Por exemplo, Bulbasaur é um Pokémon da espécie “semente”.
- Cada Pokémon possui até dois tipos: um tipo primário, e um tipo secundário (se existir). Cada tipo inclui um nome e uma descrição. Por exemplo, Charizard possui o tipo primário “Fogo” e tipo secundário “Vôo”.
- Os Pokémons possuem habilidades. Além disso, alguns Pokémons possuem habilidades ocultas. Por exemplo, Meditite possui a habilidade oculta de “telepatia”.

## Entidades: 

### Fortes:
- Categoria, 
- Espécie, 
- Tipo, 
- Habilidade

### Fracas
- Pokemon 

## Atributos de cada entidade:

- ***Pokemon***: id(PK), nome, peso, valor_ataque, valor_defesa, velocidade_media, categoria_id(FK), especie_id(FK), tb_tipo_id(FK), tb_habilidade(FK)

- ***Categoria***: categoria_id(PK), nome, descricao

- ***Espécie***: especie_id(PK), nome, descricao

- ***Tipo***: tipo_id(PK), nome, descricao

- ***Habilidade***: habilidade_id(PK), nome, oculto

## Relacionamentos

- ***Pokemon***: N:1 com ***Categoria***, 
- ***Pokemon***: N:1 com ***Espécie***, 
- ***Pokemon***: N:M com ***Tipo***,
- ***Pokemon***: N:M com ***Habilidade***,