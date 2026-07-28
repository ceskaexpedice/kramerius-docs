# Česká digitální knihovna (CDK)

## Uvod

Česká digitální knihovna (CDK) je centrální agregační vrstva nad více nezávislými instancemi systému Kramerius.

Každá knihovna (např. regionální nebo institucionální) provozuje vlastní instanci Krameria, která obsahuje:

- aplikační jádro Kramerius
- Apache Solr index
- Keycloak pro autentizaci
- Akubra repository pro ukládání digitálních objektů

CDK tyto knihovny sjednocuje do jednoho vyhledávacího a přístupového systému.

➡️ [ČDK architektura](../../architecture/cdk/index.md)
➡️ [ČDK konfigurace](../../configuration/core/configuration-properties/configuration-cdk.md)

---

## Zdrojové knihovny

Každá zdrojová knihovna je nezávislá instance Krameria.

Tyto knihovny jsou do CDK připojeny jako **chráněné kanály (protected channels)**.

... zapojene knihovny ???

---

## Chráněný kanál a zabezpečení

Přístup mezi CDK a zdrojovou knihovnou je řízen pomocí API autentizace:

1. Zdrojová knihovna při inicializaci vygeneruje **API klíč**
2. Tento API klíč je nakonfigurován v CDK na úrovni konfigurace zdrojů
3. CDK používá tento klíč pro:
    - Migration procesy
    - runtime načítání digitálního obsahu

API komunikace probíhá přes standardizované Kramerius API vrstvu.

➡️ [Konfigurace chráněného kanálu](../../configuration/core/configuration-properties/configuration-cdk.md)

ČDK autentizace je vysvětlena zde:

➡️ [ČDK zabezpečení](../../core-concepts/security/cdk.md)


---

## Agregační model (Migrace)

Indexace obsahu probíhá pomocí Migration procesu:

- Migration plugin běží v CDK
- je spouštěn asynchronně CDK Workerem
- připojuje se ke zdrojovým knihovnám přes API
- používá API klíč pro autentizovaný přístup

Proces je opakovaný (incremental sync), aby zachytil změny ve zdrojových knihovnách.

Výsledkem je centrální Solr index obsahující metadata všech knihoven.

➡️ [CDK worker](../../reference/process-platform/workers/cdk/index.md)

---

## Přístup k obsahu dokumentů

CDK neuchovává digitální obsah (stránky, obrazy, PDF).

Při otevření dokumentu:

1. CDK identifikuje zdrojovou knihovnu
2. přes API vrstvu (chráněný kanál) zavolá zdrojový Kramerius
3. použije API klíč pro autentizaci
4. načte požadovaný digitální obsah

Tento přístup umožňuje:

- centralizované vyhledávání
- decentralizované ukládání dat
- zabezpečený přístup přes API klíče

---

## Navazujici dokumentace

- ➡️ [Zakladni pojmy](../../core-concepts/cdk/index.md)
- ➡️ [Architektura](../../architecture/cdk/index.md)
