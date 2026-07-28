# ČDK 

Česká digitální knihovna (CDK) je centrální agregační vrstva nad více nezávislými instancemi systému Kramerius.

Každá knihovna (např. regionální nebo institucionální) provozuje vlastní instanci Krameria, která obsahuje:

- aplikační jádro Kramerius
- Apache Solr index
- Keycloak pro autentizaci
- Akubra repository pro ukládání digitálních objektů

CDK tyto knihovny sjednocuje do jednoho vyhledávacího a přístupového systému.

## Navazujici dokumentace

- ➡️ [ČDK architektura](../../architecture/cdk/index.md)
- ➡️ [ČDK reference](../../reference/cdk/index.md)
- ➡️ [ČDK konfigurace](../../configuration/core/configuration-properties/configuration-cdk.md)
