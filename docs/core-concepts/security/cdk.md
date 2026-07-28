[Úvod](../../index.md) > [Základní koncepty](../../core-concepts/index.md) / [Zabezpečení](../../core-concepts/security/index.md)

# ČDK

V rámci ČDK mají všechny knihovny svůj Keycloak, ale k autentizaci se vyuzívá Keycloak ČDK jako takového. Potom při volání REST APi
jednotlivých knihoven instancí ČDK se autentizační údaje posílají jednotlivým knihovnám v HTTP hlavičkách. jednotlivé knihovny mohou
získávat své role ze svých Keycloak.
Autorizace se potom provádí na úrovni jednotlivých knihoven.

Dalším prvkem ochrany je tyv, chráněný kanál, kterým se pomocí API klíče chrání všechny REST požadavky. 

## Navazujici dokumentace

- ➡️ [Architektura](../../architecture/cdk/index.md)

