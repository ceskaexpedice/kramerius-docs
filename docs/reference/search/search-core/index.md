[Úvod](../../../index.md) > [Reference](../../../reference/index.md) / [Search](../../search/index.md) 

# Search core

Popis aktuální podoby schématu: [Google spreadsheet](https://docs.google.com/spreadsheets/d/1DoDnSIGPqPnYbb0U2RSNLKm9eAY2FQNimJyTPeQsC2A/edit#gid=0)

Search subsystém je zodpovědný za:

- fulltextové vyhledávání nad indexovanými objekty
- strukturované filtrování podle metadat
- fasetovou navigaci
- poskytování výsledků pro API a UI

Search pracuje nad předem připraveným indexem, který vzniká z repozitářových dat.

---

## Search model

Search index reprezentuje digitální objekty z repozitáře:

- monografie
- periodika
- ročníky / čísla
- stránky
- sbírky

Každý objekt je převeden do Solr dokumentu obsahujícího:

- metadata
- fulltext (pokud existuje)
- strukturu a hierarchii
- vazby na rodiče a potomky

---

## Hierarchie objektů

Index respektuje hierarchii repozitáře:

- Sbírka
    - Periodikum
        - Ročník
            - Číslo
                - Stránka

- Monografie
    - Stránka

Hierarchie je reflektována v indexu pro účely navigace a filtrování.

---

## Indexové schéma (Solr)

Search je postaven nad Solr schématem, které definuje indexovaná pole.

### Příklady polí

| Pole                    | Význam                                                                             |
| ----------------------- | ---------------------------------------------------------------------------------- |
| `pid`                   | Jedinečný identifikátor objektu v repozitáři.                                      |
| `model`                 | Model objektu (např. `monograph`, `periodical`, `periodicalvolume`, `page`).       |
| `root.pid`              | Identifikátor kořenového objektu, ke kterému dokument patří.                       |
| `root.title`            | Název kořenového objektu (např. název periodika nebo monografie).                  |
| `own_parent.pid`        | Identifikátor bezprostředního rodiče objektu.                                      |
| `pid_paths`             | Úplná cesta objektu v hierarchii repozitáře. Používá se při navigaci a filtrování. |
| `date.str`              | Datum určené pro zobrazení uživateli.                                              |
| `date.min` / `date.max` | Normalizovaný rozsah dat používaný pro řazení a filtrování.                        |
| `languages.facet`       | Jazyk dokumentu určený pro facety.                                                 |
| `licenses`              | Licence určující přístupnost dokumentu (např. `public`).                           |
| `accessibility`         | Výsledek vyhodnocení přístupových práv (např. `public`, `private`).                |
| `indexer_version`       | Verze indexeru, pomocí které byl objekt naposledy zaindexován.                     |
| `count_issue`           | Počet potomků daného typu (v tomto případě čísel periodika).                       |

## Model dotazování

Search podporuje:

### Fulltext
- vyhledávání v `title` atd

### Strukturované filtry
- typ objektu
- metadata
- hierarchie

### Fasety
- typy objektů
- autoři
- sbírky
- roky

---

## API rozhraní

Search je zpřístupněn přes REST API.

➡️ [REST API](../../api/index.md)


## Konfigurace

Search je řízen systémovou konfigurací.

➡️ [Konfigurace](../../../configuration/search/index.md)


## Solr a deployment

Search využívá Apache Solr jako indexační backend.

Detaily provozu Solr (cluster, škálování, replikace) nejsou součástí Search modelu.

Viz: ...

## Indexační pipeline (externí subsystém)

Indexace dat **není součástí Search**, ale je zajištěna samostatným subsystémem:

- Processing (Akubra / RELS-EXT logika)
- indexační pipeline
- synchronizace změn z repozitáře

➡️ [Curator Worker](../../process-platform/workers/curator/index.md)


Search pouze pracuje s výsledným indexem.

---

## Build systému indexu (externí)

Solr schema a index struktura jsou generovány při build procesu.

Tato oblast zahrnuje:

- generování `managed-schema`
- transformaci schema pro různé Solr environmenty
- kopírování Solr core konfigurací

Viz: ...

