# Kramerius Core

**Kramerius Core je aplikační jádro systému Kramerius implementované jako Java WAR aplikace běžící v aplikačním serveru (typicky Tomcat).**
Tato komponenta poskytuje kompletní backend funkcionalitu systému prostřednictvím REST API, včetně zabezpečení, a tvoří hlavní integrační a řídicí vrstvu celého systému.
Kramerius Core neimplementuje všechny funkce izolovaně, ale **orchestruje a integruje další interní i externí komponenty**, které využívá při zpracování požadavků.

---

## Role v systému

Kramerius Core plní tyto klíčové role:

- poskytuje REST API pro klientské aplikace
- implementuje autentizaci a autorizaci (napojení na Keycloak)
- zajišťuje business logiku systému
- koordinuje práci s digitálními objekty
- řídí komunikaci mezi jednotlivými subsystémy

---

## Integrované komponenty

Kramerius Core využívá následující komponenty:

### Interní komponenty (součást ekosystému Kramerius)

- **Akubra** – úložiště digitálních objektů
- **Process Platform** – asynchronní zpracování úloh

### Externí komponenty

- **SOLR** – fulltextové a faceted vyhledávání
- **Keycloak** – autentizace a autorizace uživatelů

---

## Technická charakteristika

- Java WAR aplikace
- běh v aplikačním serveru (Tomcat)
- REST API architektura
- stateless komunikace přes HTTP
- integrace externích systémů přes API

---

## Shrnutí

Kramerius Core je centrální aplikační vrstva systému Kramerius, která poskytuje REST API, implementuje business logiku a bezpečnost a zároveň orchestruje spolupráci interních i externích komponent, na kterých je celý systém postaven.

---

## Navazujici dokumentace

- ➡️ [Architektura](../../architecture/index.md)