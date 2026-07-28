# Kramerius Core

## Přehled

Kramerius Core je centrální aplikační komponenta systému Kramerius.
Jedná se o Java WAR aplikaci běžící v aplikačním serveru (typicky Tomcat), která tvoří hlavní řídicí a integrační vrstvu systému.
Kramerius Core zajišťuje zpracování požadavků, orchestrace služeb a poskytuje REST API pro klientské aplikace.

---

## Role v architektuře systému

V rámci architektury systému Kramerius plní Kramerius Core roli:

- aplikační vrstvy (Application Layer)
- integrační vrstvy mezi komponentami
- řídicí logiky systému (orchestrátor)
- vstupního bodu pro klientské aplikace (API Gateway styl)

---

## Umístění v systému

Kramerius Core je nasazen jako samostatná aplikace v kontejnerizovaném prostředí.

Typické nasazení:

- Docker kontejner
- aplikační server Tomcat
- součást Docker Compose stacku

---

## Komunikace s ostatními komponentami

Kramerius Core komunikuje s následujícími systémy:

### Interní komponenty

- **Akubra**
    - ukládání a načítání digitálních objektů

- **Process Platform**
    - spouštění a orchestrace asynchronních úloh

### Externí komponenty

- **SOLR**
    - fulltextové a faceted vyhledávání
    - indexační a dotazovací vrstva

- **Keycloak**
    - autentizace uživatelů
    - poskytování identity a rolí

---

## Architektonické zodpovědnosti

Kramerius Core odpovídá za:

- příjem a zpracování HTTP požadavků
- řízení business logiky systému
- autentizaci a autorizaci uživatelů
- koordinaci volání externích služeb
- agregaci výsledků z více systémů

---

## Tok zpracování požadavku

Typický request flow:

1. Klient odešle HTTP request na REST API
2. Kramerius Core přijme požadavek
3. Provede autentizaci (Keycloak)
4. Provede autorizaci (role, oprávnění)
5. Deleguje operaci na příslušný subsystém:
    - Akubra → práce s digitálními objekty
    - SOLR → vyhledávání
    - Process Platform → asynchronní zpracování
6. Zpracuje odpovědi a vrátí výsledek klientovi

---

## Architektonické vlastnosti

- monolitická Java WAR aplikace
- stateless REST API vrstva
- integrační orchestrátor mezi službami
- komunikace přes HTTP/REST
- běh v kontejnerizovaném prostředí (Docker)

---

## Navazujici dokumentace

- ➡️ [Reference](../../reference/index.md)
- ➡️ [Konfigurace](../../configuration/index.md)
- ➡️ [Deployment](../../deployment/index.md)
