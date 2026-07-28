[Úvod](../../index.md) > [Základní koncepty](../../core-concepts/index.md) / [Zabezpečení](../../core-concepts/security/index.md)

# Akce

Akce představují oprávnění, kterým rozumí systém Kramerius.

Akce popisuje operaci, kterou lze v systému provést.

Mezi příklady patří:

- zobrazení obsahu
- úprava metadat
- správa uživatelů
- přístup do administračních funkcí

Akce jsou přiřazovány rolím.

## Proč akce existují

Akce poskytují stabilní autorizační model nezávislý na externím poskytovateli identity.

Namísto vkládání aplikačních oprávnění přímo do Keycloaku je Kramerius vyhodnocuje interně.

## Vztah k rolím

```text
Role
  ↓
Action
```

Role uděluje jednu nebo více akcí.

Úplný seznam dostupných akcí je popsán v referenční dokumentaci.

## Navazujici dokumentace

- ➡️ [Reference](../../reference/security/actions/index.md)


