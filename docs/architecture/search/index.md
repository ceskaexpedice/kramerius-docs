# Vyhledavani

```text
Repository
│
Indexer
│
Solr Index
│
Search API
│
Web Client
```

➡️ [Jak probiha vyhledavani](search-api.md)

Kramerius používá několik nezávislých indexačních subsystémů, které pokrývají různé části systému:

- Search index (fulltext nad Fedora objekty)
- Processing model (RELS-EXT / Akubra interní stav)
- Logs index (audit a systémové události)
- Monitor index ...
- sdnnt-sync index ...

Všechny tyto subsystémy sdílejí společné principy:

- asynchronní aktualizace
- eventual consistency
- transformace dat z repozitáře
- závislost na indexačních pipeline

---

## Společné vlastnosti

### Eventual consistency
Všechny indexy mohou být dočasně nekonzistentní vůči repozitáři.

---

### Asynchronní zpracování
Změny v repozitáři jsou zpracovány přes queue/pipeline.

---

### Transformace dat
Data z repozitáře nejsou ukládána přímo, ale transformována do specializovaných modelů.

---

### Build-time struktura indexů

Indexy jsou částečně definovány build procesem:

- generování Solr schema
- příprava indexových struktur
- kopírování Solr core konfigurací

---

## Solr jako společná infrastruktura

Více indexů může sdílet:

- jednu Solr instanci
- nebo SolrCloud cluster
- různé cores / collections

---

## Přehled indexů

### Search index
Fulltextové vyhledávání nad Fedora objekty.

---

### Processing model
Interní model RELS-EXT a Akubra vztahů.

---

### Logs index
Audit a systémové události.


## Navazujici dokumentace

- ➡️ [Reference](../../reference/search/index.md)
- ➡️ [Konfigurace](../../configuration/search/index.md)
