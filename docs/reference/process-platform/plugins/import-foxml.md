[Úvod](../../../index.md) > [Reference](../../index.md)  / [Process Platform](../../process-platform/index.md)  / [Pluginy](../plugins/index.md)

# Import FOXML

Importuje data ve formátu FOXML do repozitáře Kramerius.

Proces načte obsah z určeného adresáře a vytvoří nebo aktualizuje odpovídající objekty v repozitáři. Volitelně může po dokončení importu spustit indexaci.

## Worker

Curator Worker

## Definition ID

import

## Payload

| Parametr       | Typ     | Povinný | Popis                                                          |
| -------------- | ------- | ------- | -------------------------------------------------------------- |
| inputDataDir   | String  | Ano     | Cesta k adresáři obsahujícímu data určená k importu.           |
| startIndexer   | Boolean | Ano     | Určuje, zda má být po dokončení importu spuštěna indexace.     |
| license        | String  | Ne      | Licence, která bude přiřazena importovaným objektům.           |
| collections    | String  | Ne      | Seznam kolekcí, do kterých budou importované objekty zařazeny. |
| pathtype       | String  | Ne      | Typ interpretace cesty k importovaným datům.                   |
| indexationType | String  | Ne      | Strategie indexace použitá po dokončení importu.               |

## Výsledek

Po úspěšném dokončení procesu jsou data importována do Krameria. Pokud je parametr `startIndexer` nastaven na `true`, je následně spuštěna indexace importovaných objektů.

## Související pluginy

* Import NDK METS](import-ndk-mets.md
