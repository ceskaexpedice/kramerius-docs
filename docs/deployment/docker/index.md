# Docker Compose deployment

- ➡️ [Instalace](installation.md)

Kramerius může být nasazen pomocí Docker Compose.

Compose deployment obsahuje kompletní runtime infrastrukturu systému:

- aplikační backend
- PostgreSQL databáze
- Solr
- Keycloak
- image server
- Process Platform
- worker služby
- cache vrstvy
- distribuované locking služby

---

## Účel compose deploymentu

Docker Compose deployment slouží zejména pro:

- lokální instalace
- menší produkční instalace
- testovací prostředí
- integrační prostředí
- vývoj

---

## Architektonické vrstvy

Compose deployment typicky obsahuje následující vrstvy:

| Vrstva | Komponenty |
|---|---|
| API | Kramerius backend |
| Search | Solr |
| Security | Keycloak |
| Persistence | PostgreSQL |
| Processing | Process Platform + workers |
| Media | Image server |
| Cache | Memcached |
| Locking | Hazelcast |

---

## Hlavní služby

### Kramerius backend

Hlavní REST API aplikace.

Zodpovídá za:

- business logiku
- autorizaci
- komunikaci se search vrstvou
- komunikaci s image serverem

---

### Solr

Vyhledávací a indexační vrstva.

Obsahuje:

- fulltextový index
- metadata
- facety

---

### Keycloak

Identity provider systému.

Poskytuje:

- autentizaci
- OIDC tokeny
- správu identit
- federaci identity

---

### PostgreSQL

Persistence vrstva.

Deployment může používat více samostatných PostgreSQL instancí:

- aplikační databáze
- Keycloak databáze
- Process Platform databáze

---

### Process Platform

Background processing infrastruktura.

Skládá se z:

- Process Manager
- worker služeb

---

### Image server

Služby pro poskytování obrazových dat.

Typicky:

- IIIF endpointy
- tiled rendering
- zoom

---

## Sdílené volumes

Více služeb sdílí společná data pomocí mounted volumes.

Typicky:

- importní data
- image data
- audio data
- logy
- konfigurace

---

## Networking

Služby komunikují přes interní Docker síť.

Vybrané služby publikují externí porty.

---

## Health checks a startup pořadí

Deployment používá:

- health checks
- depends_on
- startup orchestration

pro správné pořadí startu služeb.

---

## Konfigurace

Většina konfigurace je realizována pomocí:

- environment variables
- mounted configuration files
- Docker volumes

---

## Produkční poznámky

Compose deployment je vhodný pro:

- menší a střední instalace
- jednodušší správu infrastruktury

V rozsáhlejších instalacích může být nahrazen:

- Kubernetes deploymentem
- externími managed službami
- oddělenou infrastrukturou

---

## Docker Compose source

Aktuální compose konfigurace:

`docker-compose.yml`
### Kramerius docker compose 

Pro snadnější instalaci a manipulaci vznikl projekt [Kramerius docker compose](https://github.com/ceskaexpedice/kramerius-docker-compose), který obsahuje všechny komponenty kontejnerizované.

## Navazujici dokumentace

- ➡️ [Konfigurace](../../configuration/index.md)


