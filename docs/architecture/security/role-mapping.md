[Úvod](../../index.md) > [Architektura](../../architecture/index.md)  / [Zabezpečení](../../architecture/security/index.md)

# Mapování rolí

Role jsou spravovány v externím Identity Provideru.

Kramerius role neinterpretuje přímo jako oprávnění.

Místo toho jsou role mapovány na interní akce.

## Motivace

Role reprezentují organizační strukturu.

Akce reprezentují oprávnění aplikace.

Oddělení těchto konceptů umožňuje:

- měnit role bez zásahu do aplikace,
- používat stejnou roli pro více oprávnění,
- používat více rolí pro stejné oprávnění.

## Příklad

```text
ROLE_ADMIN
    ↓
ADMIN_ACCESS

ROLE_EDITOR
    ↓
MODIFY_METADATA

ROLE_READER
    ↓
VIEW_DOCUMENT
```

## Vyhodnocení

Při autorizaci:

1. získají se role uživatele,
2. vyhledají se odpovídající akce,
3. vyhodnotí se kritéria,
4. vrátí se výsledek.

