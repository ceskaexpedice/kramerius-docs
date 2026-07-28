# ⚙️ Konfigurace systému Kramerius

Tato kapitola popisuje konfiguraci systému Kramerius a jeho integrovaných komponent.

Konfigurace je rozdělena do techto hlavních úrovní:

- **Konfigurace Kramerius Core**
- **Konfigurace integrovaných služeb**
- **Konfigurace Operations**

Toto rozdělení je důležité pro správné pochopení toho, co se kde nastavuje:
- část konfigurace přímo ovlivňuje chování aplikace Kramerius
- část konfigurace se týká externích systémů, které Kramerius využívá

---


## [Kramerius Core](core/index.md)

Jádro aplikace (Java/Tomcat) obsahuje množství konfiguračních parametrů. Tyto parametry mají definované výchozí hodnoty přímo v distribučním balíčku (`.war`).
Typicky jde o parametry, které přímo ovlivňují chování systému:

- URL adresy integrovaných služeb (SOLR, Akubra, Keycloak)
- databázová připojení
- cache, timeouty
- nastavení procesní platformy
- další runtime parametry

---

## Konfigurace integrovaných služeb

Tato část popisuje konfiguraci externích systémů, které Kramerius využívá.

Tyto komponenty mají vlastní konfigurační mechanismy a často i vlastní dokumentaci.

### [Akubra](akubra/index.md)
- storage backend
- ukládání digitálních objektů
- konfigurace persistence

### [Vyhledávání](search/index.md)
- definice indexů
- analyzéry
- schema
- boostování a relevance

### [Zabezpečení](security/index.md)
- realm konfigurace
- klienti
- role a oprávnění
- mapování uživatelů

### [Process Platform](process-platform/index.md)
- asynchronni ulohy

### [Distribuované zámky](distributed-locks/index.md)
- synchronizace

### [IIIF Image Server](iiif/index.md)
- cachování obrazů
- limity generování
- zdroje obrazů

### [CDK](core/configuration-properties/configuration-cdk.md)
Konfigurace se děje skrze Kramerius Core

### [Web klient](https://github.com/ceskaexpedice/kramerius-web-client-v3/wiki)
- hlavní konfigurace
- úvodní stránka
- licence

---

## Konfigurace v Docker nasazení ([Deployment](../deployment/docker/index.md))

Při nasazení pomocí Docker Compose je veškerá konfigurace centralizovaná do jednoho místa – souboru `.env`, ze kterého čerpá `docker-compose.yml`.
Pro snadnější instalaci a manipulaci vznikl projekt [Kramerius docker compose](https://github.com/ceskaexpedice/kramerius-docker-compose), který obsahuje všechny komponenty kontejnerizované.

---

## Konfigurační strategie a hierarchie

Systém Kramerius využívá vrstvenou konfiguraci. Obecné pravidlo pro správu konfigurace je:

1. **Výchozí hodnoty (Defaults)**  
   Jsou zabaleny přímo v aplikaci (`.war` soubory) nebo definovány v Docker image.

2. **Globální / instalační konfigurace**  
   Společná nastavení pro celé nasazení (např. URL adresy, databáze, připojení ke službám) jsou řízena na úrovni **Docker Compose** pomocí proměnných prostředí.

3. **Detailní konfigurace komponent**  
   Specifické chování jednotlivých modulů nebo integrovaných služeb (např. Solr schema, Keycloak role) se konfiguruje v jejich vlastních konfiguračních souborech.

---

## Operations

### Logování
...

### Monitoring
...


## Navazujici dokumentace

- ➡️ [Architektura](../architecture/index.md)
- ➡️ [Reference](../reference/index.md)
- ➡️ [Deployment](../deployment/index.md)
- ➡️ [Navody](../guides/index.md)


