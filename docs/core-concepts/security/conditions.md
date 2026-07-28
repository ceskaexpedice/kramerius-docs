[Úvod](../../index.md) > [Základní koncepty](../../core-concepts/index.md) / [Zabezpečení](../../core-concepts/security/index.md)

# Podmínky

Podmínky jsou dodatečné požadavky, které musí být splněny před tím, než je akce povolena.

Poskytují jemnozrnou kontrolu nad rámec jednoduché autorizace založené na rolích.

## Příklady

Mezi typické podmínky patří:

- povolené rozsahy IP adres
- licenční omezení
- omezení přístupu na úrovni konkrétních sbírek

Významným typem podmínky je **licence** (viz [Licence](../../domain-concepts/license/index.md)).

## Model vyhodnocení

I když role přidělí akci, přístup může být stále zamítnut, pokud nejsou splněny požadované podmínky.

```text
Role
  ↓
Action
  ↓
Condition
  ↓
Permit / Deny
```

## Proč podmínky existují

Mnoho případů v knihovních systémech vyžaduje pravidla přístupu, která nelze vyjádřit pouze pomocí rolí uživatelů.

Například:

- přístup může být povolen pouze z institucionálních sítí
- přístup může záviset na platné licenční smlouvě
- přístup může záviset na požadovaném obsahu

Podmínky umožňují tato pravidla konfigurovat bez nutnosti zavádět další role.

## Hierarchie licencí
Licence je jednim z typu Podminky, ktere lze priradit k roli. V Krameriu ma zvlastni dulezitost, protoze urcuje, zda ctenar ma
opravneni cist knihu s prislusnou licenci

- Licence jsou součástí FOXML dokumentů v Akubra repository.
- Každý objekt (stránka, kniha, periodikum) může mít 0–n licencí.
- Licence vyššího objektu (např. kniha nebo repo) se **implicitně uplatní na všechny nižší objekty** při vyhodnocování (ne fyzicky).
- Licence mohou být **globální** nebo **lokální**.

---

## Vyhodnocení oprávnění – příklad

Akce: READ

Role: krameriusAdmin

Kriterium = Licence = dnnto

Kritérium = IPAddress = 192.168.0.0/24

Výsledek: povolení, pokud uživatel má roli krameriusAdmin a dokument má licenci dnnto
a je přihlášen z IP v povoleném rozsahu


- K jedné akci lze přiřadit více pravidel – systém je vyhodnocuje postupně.
- Licence mohou mít **prioritu**, pokud se na akci vztahuje více licencí.

---

## Hierarchické vyhodnocování přístupů

Při vyhodnocování oprávnění Kramerius postupuje **hierarchicky** podle struktury objektů v repository:

- Každý digitální objekt (stránka, kniha, periodikum) může mít přiřazenu 0–n licencí.
- Pokud u konkrétního objektu není licence explicitně definována, systém **dědí licence z nadřazeného objektu**.
    - Například:
        - Licence je definována u **monografie**.
        - Stránka `page` uvnitř této monografie nemá žádnou vlastní licenci.
        - Při vyhodnocování přístupu pro stránku se použije licence definovaná u monografie.
- Toto dědění probíhá pouze při **runtime vyhodnocení přístupů**, licence se fyzicky nepřepisuje do nižších objektů.

> Poznámka: Tato hierarchie platí i pro skupiny dokumentů nebo celé repozitáře. Vyšší objekt určuje implicitní pravidla pro všechny podřízené objekty.

## Navazujici dokumentace

- ➡️ [Reference](../../reference/security/actions/index.md)


