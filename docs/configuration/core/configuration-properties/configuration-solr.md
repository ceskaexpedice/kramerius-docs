[Úvod](../../../index.md) > [Konfigurace](../../index.md)  / [Core](../index.md) / [Configuration properties](index.md)

# Solr konfigurace

Tato stránka poskytuje **referenční přehled konfiguračních parametrů Akubra storage**. Obsahuje defaultní hodnoty, účel a doporučené nastavení.

Konfigurace se načítá z:

- **Default**: uvnitř JAR souboru knihovny `configuration.properties`
- **Uživatelské přetížení**: soubor `$USER_HOME/.kramerius4/configuration.properties`

Uživatel může ve svém souboru předefinovat libovolnou hodnotu z defaultního souboru.

---

## Search index

Index **search** slouží pro vyhledávání klientskými aplikacemi (veřejné a administrativní rozhraní).

| Parametr | Popis | Default / Příklad |
|-----------|-------|-----------------|
| `solrSearchHost` | URL adresa Solr jádra `search`. Používá se pro připojení klientů. | `http://localhost:8983/solr/search` |
| `solrSearchLogin` | Přihlašovací jméno pro autentizaci k Solr jádru `search`, pokud je vyžadována. | `__` |
| `solrSearchPassword` | Heslo pro autentizaci k Solr jádru `search`. | `__` |

---

## Processing index

Index **processing** nahrazuje původní resource index Fedory. Každý importovaný objekt je do něj zaznamenán spolu se všemi vazbami.

| Parametr | Popis | Default / Příklad |
|-----------|-------|-----------------|
| `solrProcessingHost` | URL adresa Solr jádra `processing`, používaného pro interní indexaci objektů. | `http://localhost:8983/solr/processing` |

---

**Poznámky:**

- Pokud jsou Solr jádra provozována na jiném serveru nebo portu, je nutné upravit odpovídající parametry.
- Parametry `solrSearchLogin` a `solrSearchPassword` se používají jen při zapnuté autentizaci Solr.
