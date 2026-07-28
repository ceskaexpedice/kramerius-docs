# Solr Cores Reference

Tato stránka poskytuje přehled hlavních Solr jader používaných v systému **Kramerius 7** a jejich účel.

Informace zde jsou určeny pro referenci při konfiguraci a práci se systémem.

---

## Solr Cores

Kramerius využívá vyhledávací engine **Solr** a definuje tato hlavní jádra (cores), každé s odlišným účelem:

| Jádro        | Popis                                                                                                                           | Konfigurace |
|--------------|---------------------------------------------------------------------------------------------------------------------------------|-------------|
| `search`     | Určeno pro vyhledávání klientskými aplikacemi (veřejné rozhraní i administrace).                                                | `solrSearchHost=http://localhost:8983/solr/search` <br> `solrSearchLogin=__` <br> `solrSearchPassword=__` |
| `processing` | Interní index repozitáře, nahrazuje dřívější resource index. Každý nově importovaný objekt je indexován spolu se svými vazbami. | `solrProcessingHost=http://localhost:8983/solr/processing` |
| `logs`       | Slouží pro ukládání informací o přístupu uživatelů, slouží jako zdroj dat pro statistiky a reporty.                             | - |
| `sdnnt`      | Slouží pro synchronizaci se systemem sdnnt.                                                                                     | - |


### [Search Core](search-core/index.md)

Hlavní vyhledávací jádro pro klientské aplikace (veřejné i administrační rozhraní).

### Processing Core
...

Interní index repozitáře, nahrazuje dříve používaný Resource Index Fedory.

### Logs Core
...
Ukládání informací o přístupu uživatelů a zdroj pro statistiky a reporty.

### Navazujici dokumentace

- ➡️ [Zakladni pojmy](../../core-concepts/search/index.md)
- ➡️ [Architektura](../../architecture/search/index.md)
- ➡️ [Konfigurace](../../configuration/search/index.md)
- ➡️ [Verzovani](../../versioning/search/index.md)

 

