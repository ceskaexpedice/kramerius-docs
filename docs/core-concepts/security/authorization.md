[Úvod](../../index.md) > [Základní koncepty](../../core-concepts/index.md) / [Zabezpečení](../../core-concepts/security/index.md)

# Autorizace

Autorizace odpovídá na otázku:

> Je autentizovaný uživatel oprávněn provést konkrétní akci?

Autorizace je vyhodnocována systémem Kramerius.

Rozhodování o přístupu je založeno na:

- rolích
- akcích
- podmínkách


```text
Role
  ↓
Action
  ↓
Condition
  ↓
Access Decision
```

---

## Pravidla přiřazení oprávnění

Ke každé akci lze přiřadit:

1. **Role** – uživatel musí mít danou roli, aby mohl akci provést.
2. **Podminky** – např. `IPAddress`, které omezí přístup podle sítě uživatele nebo kontrola, zda dokument nebo sbírka má přiřazenou licenci, která oprávnění umožňuje.

> Při vyhodnocování více pravidel hraje roli **priorita pravidel a licencí**.

---
 
## [Role](roles.md)
## [Akce](actions.md)
## [Podminky](conditions.md)
## [Licence](../../domain-concepts/license/index.md)

---

## Navazujici dokumentace

- ➡️ [Architektura](../../architecture/security/authorization.md)
- ➡️ [Reference](../../reference/security/authorization/index.md)

