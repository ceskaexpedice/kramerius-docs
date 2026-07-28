[Úvod](../../../index.md) > [Navody](../../../guides/index.md) / [Administrator](../index.md)  / [ČDK](../cdk/index.md)

# Zapojení knihovny do České digitální knihovny (ČDK)

Tento návod popisuje postup připojení nové knihovny do České digitální knihovny (ČDK). Je určen administrátorům zdrojových knihoven i administrátorům centrálního ČDK serveru.

Po dokončení postupu budou dokumenty zdrojové knihovny zaindexovány do centrálního vyhledávacího indexu ČDK a budou dostupné prostřednictvím uživatelského rozhraní ČDK.

```text
Zdrojová knihovna
        │
        │ 1. API key
        ▼
Centrální ČDK
        │
        │ 2. Test spojení
        ▼
CDK Migration
        │
        │ 3. Indexace dokumentů
        ▼
Centrální Solr index
        │
        │
Čtenář → ČDK UI → metadata z indexu + obsah ze zdrojové knihovny
```

## Předpoklady

Před zahájením musí být splněny následující podmínky:

- zdrojová knihovna používá podporovanou verzi Krameria,
- administrátor má přístup ke konfiguraci zdrojové knihovny,
- administrátor ČDK má přístup ke konfiguraci centrálního serveru,
- oba servery jsou vzájemně síťově dostupné.

Konfigurace parametrů potřebných pro komunikaci mezi knihovnami je popsána v kapitole ➡️ [Konfigurace](../../../configuration/core/configuration-properties/configuration-cdk.md).

## 1. Vygenerování API klíče

Na zdrojové knihovně vytvořte nový API klíč určený pro komunikaci s ČDK.

Klíč následně:

- zapište do konfigurace zdrojové knihovny,
- předejte administrátorovi ČDK,
- zapište také do konfigurace centrálního ČDK serveru.

Podrobný popis konfiguračních parametrů naleznete v kapitole ➡️ [Konfigurace](../../../configuration/core/configuration-properties/configuration-cdk.md).

## 2. Ověření komunikace

Po konfiguraci doporučujeme ověřit, že se centrální ČDK server dokáže ke zdrojové knihovně připojit.

Proveďte test pomocí příslušného REST API .

Úspěšná odpověď potvrzuje, že:

- API klíč je platný,
- komunikace mezi servery funguje,
- zdrojová knihovna je připravena pro migraci.

Popis endpointu je uveden v referenční dokumentaci ➡️ [REST API](../../../reference/api/index.md).

## 3. Spuštění migrace

První zaindexování knihovny se provádí pomocí procesu ➡️ [Migrace CDK](../../../reference/process-platform/plugins/cdk-migration.md).

Proces:

- projde dokumenty zdrojové knihovny,
- načte jejich metadata,
- vytvoří odpovídající záznamy v indexu ČDK.

Proces se spouští výhradně prostřednictvím ➡️ [REST API](../../../reference/api/index.md).

> Proces není dostupný z administrátorského uživatelského rozhraní.

Popis endpointu i formátu požadavku je uveden v referenční dokumentaci procesů.

## 4. Kontrola výsledku

Po dokončení migrace ověřte, že:

- dokumenty jsou dohledatelné ve vyhledávání ČDK,
- lze otevřít detail dokumentu,
- stránky dokumentu jsou načítány ze zdrojové knihovny.

Je důležité si uvědomit, že centrální ČDK neobsahuje vlastní repozitář dokumentů.

Obsah dokumentů zůstává uložen ve zdrojové knihovně. ČDK obsahuje pouze centrální vyhledávací index a při zobrazení dokumentu načítá data přímo ze zdrojového serveru.

## Aktualizace jednotlivých dokumentů

Pokud je potřeba znovu zaindexovat pouze jeden dokument, použijte proces ➡️ [Reharvest CDK](../../../reference/process-platform/plugins/cdk-reharvest.md).

Proces:

1. odstraní dokument z indexu ČDK,
2. znovu načte metadata ze zdrojové knihovny,
3. dokument znovu zaindexuje.

Použití je vhodné například po opravě metadat nebo po změně indexovaných polí.

Proces je dostupný prostřednictvím ➡️ [REST API](../../../reference/api/index.md).

## Odstranění knihovny z ČDK

Pro odstranění všech dokumentů jedné knihovny z centrálního indexu použijte proces pro smazání knihovny.

Proces odstraní všechny dokumenty dané knihovny z vyhledávacího indexu ČDK.

Zdrojová knihovna ani její repozitář nejsou tímto procesem nijak ovlivněny.

Proces se spouští prostřednictvím REST API.

