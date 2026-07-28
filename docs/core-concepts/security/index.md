# Zabezpečení

Tato dokumentace popisuje **aplikační úroveň zabezpečení** v systému Kramerius.

Nezabývá se infrastrukturním ani systémovým zabezpečením, jako je konfigurace HTTPS/TLS, oprávnění operačního systému nebo síťová bezpečnost.
Zabezpečení v systému Kramerius je založeno na dvou nezávislých konceptech:

- **Autentizace** – určení, kdo je uživatel.
- **Autorizace** – určení, co je uživatel oprávněn dělat.

Autentizace je delegována na externího poskytovatele identity, typicky Keycloak, pomocí standardů OAuth 2.0 a OpenID Connect.

Autorizaci provádí samotný Kramerius. Rozhodování o přístupu je založeno na kombinaci rolí, akcí a podminek.

## Bezpečnostní model

```text
User
  ↓
Role
  ↓
Action
  ↓
Condition
  ↓
Access Decision
```


Uživatel se autentizuje prostřednictvím poskytovatele identity a získá jednu nebo více rolí.

K rolim jsou v systému Kramerius prirazovany akce. Akce představují oprávnění, například zobrazování obsahu, úpravu metadat nebo správu systému.

Před udělením přístupu mohou být vyhodnocena další podminky. Podminky mohou omezovat přístup na základě faktorů, jako jsou rozsahy IP adres nebo licenční omezení.

## Pojmy

- [Autentizace](authentication.md)
- [Autorizace](authorization.md)
- [Role](roles.md)
- [Akce](actions.md)
- [Podminky](conditions.md)
- [Licence](../../domain-concepts/license/index.md)
- [ČDK](cdk.md)


---

## Navazujici dokumentace

- ➡️ [Architektura](../../architecture/security/index.md)
- ➡️ [Reference](../../reference/security/index.md)
