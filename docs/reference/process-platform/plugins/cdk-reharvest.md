[Úvod](../../../index.md) > [Reference](../../index.md)  / [Process Platform](../../process-platform/index.md)  / [Pluginy](../plugins/index.md)

# Reharvest Document

Znovu načte jeden dokument do indexu Centrální digitální knihovny (CDK).

Proces nejprve odstraní dokument z cílového CDK indexu a následně jej znovu získá ze zdrojové knihovny. Používá se zejména v případech, kdy je potřeba opravit neaktuální nebo poškozená data v CDK indexu bez provedení úplné migrace.

## Worker

CDK Worker

## Definition ID

...

## Payload

| Parametr | Typ | Povinný | Popis |
|----------|-----|---------|-------|
| destinationUrl | String | Ano | URL cílového CDK indexu. |
| proxyApiUrl | String | Ano | URL Proxy API použitého pro komunikaci se zdrojovou knihovnou. |
| pid | String | Ano | PID dokumentu, který bude znovu načten. |
| ownPidPath | String | Ano | Cesta určující umístění PID v importovaných datech. |
| iterationUrl | String | Ne | URL zdrojové instance Kramerius. |
| iterationType | String | Ne | Typ reharvestu nebo způsob získávání dat. |
| iterationRows | String | Ne | Počet dokumentů načítaných v jednom požadavku. |
| iterationBatch | String | Ne | Velikost dávky při zpracování. |
| rootPid | String | Ne | PID kořenového objektu, pokud se reharvest týká části dokumentu. |
| type | String | Ne | Typ zpracování nebo importu. |
| libraries | String | Ne | Seznam knihoven, ze kterých lze dokument získat. |
| onlyShowConfiguration | Boolean | Ne | Pokud je nastaveno na `true`, proces pouze vypíše použitou konfiguraci a neprovede žádné změny. |
| maxItemsToDelete | Integer | Ne | Maximální počet dokumentů, které mohou být před reharvestem odstraněny z CDK indexu. |

## Výsledek

Po úspěšném dokončení procesu je původní dokument odstraněn z CDK indexu a znovu načten ze zdrojové knihovny. Výsledkem je aktuální verze dokumentu v cílovém indexu. Pokud je parametr `onlyShowConfiguration` nastaven na `true`, proces pouze zobrazí konfiguraci a žádná data se nemění.

## Související pluginy

* Migrate to CDK Index
