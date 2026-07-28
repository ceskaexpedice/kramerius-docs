[Úvod](../../index.md) > [Základní koncepty](../../core-concepts/index.md) / [Zabezpečení](../../core-concepts/security/index.md)

# Role

Role představují skupiny uživatelů se stejnými odpovědnostmi nebo oprávněními.

Role jsou spravovány poskytovatelem identity a jsou dostupné v Krameriu po úspěšné autentizaci.

Role přímo neudělují oprávnění, místo toho jsou role mapovány na akce v systému Kramerius.

Nektere role prideluje podle okolnosti sam system Kramerius automaticky

## Mapování rolí

```text
Role
  ↓
Action
```

Jedna role může udělovat více akcí.

Více rolí může udělovat stejnou akci.

## Navazujici dokumentace

- ➡️ [Reference](../../reference/security/roles/index.md)


