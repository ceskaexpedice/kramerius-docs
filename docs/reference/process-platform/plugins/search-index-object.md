[Úvod](../../../index.md) > [Reference](../../index.md)  / [Process Platform](../../process-platform/index.md)  / [Pluginy](../plugins/index.md)

# Search Index Objects

Spustí indexaci jednoho nebo více konkrétních objektů v repozitáři Kramerius.

Objekty určené k indexaci lze zadat přímo pomocí PID, seznamem PID nebo prostřednictvím souboru obsahujícího jejich seznam.

## Worker

Curator Worker

## Definition ID

new_indexer_index_object

## Payload

| Parametr                  | Typ     | Povinný | Popis |
|---------------------------|---------|---------|-------|
| type                      | String  | Ano     | Typ nebo strategie prováděné indexace. |
| pid                       | String  | Ne      | PID jednoho objektu určeného k indexaci. |
| pidlist                   | String  | Ne      | Seznam PID objektů oddělených zadaným formátem. |
| pidlist_file              | String  | Ne      | Cesta k souboru obsahujícímu seznam PID objektů. |
| ignoreInconsistentObjects | Boolean | Ne      | Přeskočí objekty, které jsou nekonzistentní nebo obsahují chyby. |
| title                     | String  | Ne      | Volitelný název procesu zobrazený v seznamu procesů. |

## Výsledek

Po úspěšném dokončení procesu jsou zadané objekty zařazeny do vyhledávacího indexu nebo je jejich existující index aktualizován podle zvolené strategie.

## Související pluginy

* Search Index Model
* Import FOXML
* Import NDK METS