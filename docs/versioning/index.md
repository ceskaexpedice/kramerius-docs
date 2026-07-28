# 📦 Verzování

Kramerius je ekosystém vzájemně spolupracujících aplikací, nikoliv jeden samostatný software. Kromě **Kramerius Core** zahrnuje také další samostatně vyvíjené komponenty, například **Process Platform** nebo **Akubra**. 
Každá z těchto komponent má vlastní životní cyklus a vlastní schéma verzování.

## [➡️ Tabulka komponent a verzí](../reference/index.md)

Uvádíme vždy nejnovější "stable" verze.

## Kramerius Core

Kramerius Core používá čtyřdílné číslo verze:

```text
GENERACE.MAJOR.MINOR[.HOTFIX]
```

Příklady:

```text
7.2.1
7.2.1.1
7.2.1.2
```

Poslední část (**HOTFIX**) je nepovinná. Verze bez čtvrtého čísla představuje původní vydání dané verze. Hotfix je vydán pouze tehdy, pokud je potřeba opravit již publikovanou verzi.

### Generace

První číslo označuje dlouhodobou generaci produktu.

Například:

```text
7.x.x
```

Toto číslo se mění jen výjimečně. Není přímo odvozeno od rozsahu implementovaných změn, ale představuje strategické rozhodnutí o nové generaci produktu. O jeho zvýšení rozhoduje vedení projektu.

### Major

Druhé číslo označuje významné technické nebo architektonické změny.

Typicky se jedná o:

- zavedení nových subsystémů,
- rozsáhlý refaktoring,
- změnu architektury,
- změny ovlivňující více komponent současně.

Například verze **7.2.x** přinesla zavedení **Process Platform** a související refaktoring zpracování procesů.

### Minor

Třetí číslo označuje rozšíření funkcionality při zachování kompatibility v rámci stejné major verze.

Typicky se jedná o:

- nové funkce,
- nové možnosti konfigurace,
- rozšíření REST API,
- vylepšení uživatelského rozhraní.

Například zavedení nové konfigurace webového klienta představuje zvýšení minor verze.

### Hotfix

Čtvrté číslo označuje opravnou verzi již vydaného release.

Příklady:

```text
7.2.1      Původní vydání
7.2.1.1    První hotfix
7.2.1.2    Druhý hotfix
```

Hotfix obsahuje pouze opravy chyb a neměl by přinášet nové funkce ani měnit chování systému.

Pro každou vydanou verzi se hotfixy vyvíjejí na samostatné **hotfix větvi**, což umožňuje opravovat již vydané verze nezávisle na pokračujícím vývoji dalších verzí.

---

## Ostatní komponenty ekosystému

Samostatně vyvíjené komponenty, například **Process Platform** nebo **Akubra**, používají jednodušší třídílné schéma verzování:

```text
MAJOR.MINOR[.HOTFIX]
```

Příklady:

```text
1.5
1.5.1
2.0
```

Na rozdíl od Kramerius Core zde chybí úvodní **politická** verze. Tyto komponenty jsou verzovány nezávisle podle svého vlastního vývojového cyklu.

Jednotlivé části čísla verze mají následující význam:

- **Major** – významné technické nebo architektonické změny,
- **Minor** – nové funkce při zachování zpětné kompatibility,
- **Hotfix** – opravná verze obsahující opravy chyb.

---

## [Indexer](search/index.md)

## Databaze
...

## Nezávislé vydávání komponent

Komponenty ekosystému Kramerius jsou vydávány nezávisle na sobě. Nová verze Process Platform nebo Akubra proto nemusí znamenat vydání nové verze Kramerius Core a naopak.

Informace o kompatibilních verzích jednotlivých komponent jsou uvedeny v dokumentaci nebo v poznámkách k jednotlivým vydáním (GitHub Releases).