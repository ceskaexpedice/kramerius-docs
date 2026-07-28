[Úvod](../../../index.md) > [Reference](../../index.md)  / [Process Platform](../../process-platform/index.md)  / [Pluginy](../plugins/index.md)

# Search Index Model

Spustí indexaci objektů v repozitáři Kramerius.

Proces umožňuje indexovat všechny objekty nebo pouze objekty odpovídající zadaným kritériím. Lze omezit indexaci na konkrétní model, vybrané stavy indexace nebo ignorovat nekonzistentní objekty.

## Worker

Curator Worker

## Definition ID

new_indexer_index_model

## Payload

| Parametr                  | Typ     | Povinný | Popis |
|---------------------------|---------|---------|-------|
| type                      | String  | Ano     | Typ nebo strategie prováděné indexace. |
| pid                       | String  | Ne      | PID modelu nebo objektu, na který bude indexace omezena. Pokud není zadán, indexují se všechny odpovídající objekty. |
| indexNotIndexed           | Boolean | Ne      | Zahrne objekty, které dosud nebyly indexovány. |
| indexRunningOrError       | Boolean | Ne      | Zahrne objekty, jejichž předchozí indexace stále probíhá nebo skončila chybou. |
| indexIndexedOutdated      | Boolean | Ne      | Zahrne objekty, jejichž index je zastaralý a vyžaduje aktualizaci. |
| indexIndexed              | Boolean | Ne      | Zahrne i objekty, které jsou již korektně indexovány. |
| ignoreInconsistentObjects | Boolean | Ne      | Přeskočí objekty, které jsou nekonzistentní nebo obsahují chyby. |
| updateProcessName         | Boolean | Ne      | Průběžně aktualizuje název procesu podle právě zpracovávaného objektu. |

## Výsledek

Po úspěšném dokončení procesu jsou vybrané objekty zařazeny do vyhledávacího indexu nebo je jejich existující index aktualizován podle zvolené strategie.

## Související pluginy

* Import FOXML
* Import NDK METS
