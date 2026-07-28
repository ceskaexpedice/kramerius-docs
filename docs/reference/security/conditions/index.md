[Úvod](../../../index.md) > [Reference](../../index.md)  / [Zabezpečení](../index.md)

# Podmínky

Kritéria představují dodatečné podmínky autorizace.

Právo reprezentováno vazbou mezi rolí a akcí, kterou se uživatel snaží vykonat. V tomto jednoduchém případě vždy platí, že uživatel má právo vykonat danou akci.  
Vazba může být rozšířena o dodatečnou podmínky, ta pak dál specifikuje podmínky za kterých uživatel může danou akci vykonat.


## Available Criteria

### IP Address Criterion

Ověřuje IP adresu klienta.

#### Parameters

| Parameter | Description |
|------------|------------|
| allowedRanges | Povolené rozsahy IP adres |

---

### License Criterion

Ověřuje licenční podmínky.

#### Parameters

| Parameter | Description |
|------------|------------|
| licenseId | Identifikátor licence |

---

### ... další kriteria

