[Úvod](../../../index.md) > [Reference](../../index.md)  / [Process Platform](../../process-platform/index.md)  / [Pluginy](../plugins/index.md)

# Migrate to CDK Index

Migruje data ze zdrojové knihovny do indexu Centrální digitální knihovny (CDK).

Proces načítá data ze zdrojové instance Kramerius a zapisuje je do cílového CDK indexu. Podporuje dávkové zpracování, inkrementální migraci pomocí časových razítek a filtrování migrovaných dat. Lze jej také spustit pouze pro zobrazení výsledné konfigurace bez provedení samotné migrace.

## Worker

CDK Worker

## Definition ID

cdk-migration

## Payload

| Parametr | Typ | Povinný | Popis                                                                                                                                                                                                                                                   |
|----------|-----|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| configSource | String | Ano | Cesta ke konfiguračnímu souboru migrace. Napr. [/cz/incad/kramerius/services/workers/copy/K7.xml](https://github.com/ceskaexpedice/kramerius/blob/master/processes/cdk/cdkprocesses/src/main/resources/cz/incad/kramerius/services/workers/copy/K7.xml) |
| destinationUrl | String | Ano | URL cílového CDK indexu.                                                                                                                                                                                                                                |
| iterationDl | String | Ano | Identifikátor zdrojové digitální knihovny.                                                                                                                                                                                                              |
| iterationId | String | Ano | Identifikátor migrační iterace.                                                                                                                                                                                                                         |
| iterationUrl | String | Ano | URL zdrojové instance Kramerius.                                                                                                                                                                                                                        |
| iterationFQuery | String | Ne | Filtrační dotaz omezující migrované dokumenty.                                                                                                                                                                                                          |
| iterationApiKey | String | Ne | API klíč použitý pro přístup ke zdrojové instanci.                                                                                                                                                                                                      |
| iterationWorkingtime | String | Ne | Časové okno, ve kterém může migrace probíhat.                                                                                                                                                                                                           |
| timestampUrl | String | Ne | URL úložiště časových razítek pro inkrementální migraci.                                                                                                                                                                                                |
| comparingIdentifier | String | Ne | Identifikátor používaný pro porovnávání dokumentů mezi zdrojem a cílem.                                                                                                                                                                                 |
| feederBatchSize | String | Ne | Počet dokumentů zpracovaných v jedné dávce.                                                                                                                                                                                                             |
| showConfigurationOnly | Boolean | Ano | Pokud je nastaveno na `true`, migrace se neprovede a vypíše se pouze použitá konfigurace.                                                                                                                                                               |
| showEffectiveConfigurationOnly | Boolean | Ne | Zobrazí pouze výslednou efektivní konfiguraci po sloučení všech nastavení.                                                                                                                                                                              |

## Výsledek

Po úspěšném dokončení procesu jsou dokumenty ze zdrojové knihovny přeneseny do cílového CDK indexu. Pokud je parametr `showConfigurationOnly` nastaven na `true`, migrace se neprovede a vypíše se pouze konfigurace použitá pro běh procesu.

## Související pluginy

...