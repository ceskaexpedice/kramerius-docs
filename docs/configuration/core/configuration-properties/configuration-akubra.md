[Úvod](../../../index.md) > [Konfigurace](../../index.md)  / [Core](../index.md) / [Configuration properties](index.md)

# Akubra konfigurace

Tato stránka poskytuje **referenční přehled konfiguračních parametrů Akubra storage**. Obsahuje defaultní hodnoty, účel a doporučené nastavení.

Konfigurace se načítá z:

- **Default**: uvnitř JAR souboru knihovny `configuration.properties`
- **Uživatelské přetížení**: soubor `$USER_HOME/.kramerius4/configuration.properties`

Uživatel může ve svém souboru předefinovat libovolnou hodnotu z defaultního souboru.

---

| Parametr                  | Default                                          | Popis |
|---------------------------|--------------------------------------------------|-------|
| `objectStore.path`        | `${sys:user.home}/.kramerius4/data/objectStore`  | Kořenový adresář pro ukládání objektů (metadata + binární data). |
| `objectStore.pattern`     | `##/##`                                          | Struktura podadresářů pro objekty. Každé `#` odpovídá jednomu hexadecimálnímu znaku MD5 hashe názvu souboru. Defaultní hodnota znamená dvě úrovně adresářů s maximálně 256 adresáři na úroveň. |
| `datastreamStore.path`    | `${sys:user.home}/.kramerius4/data/datastreamStore` | Kořenový adresář pro ukládání datastreamů (obsah jednotlivých souborů). |
| `datastreamStore.pattern` | `##/##`                                          | Struktura podadresářů pro datastreamy. Stejná logika jako u `objectStore.pattern`. |
| `hazelcast.instance`      | `akubrasync`                                     | Jméno instance Hazelcast pro distribuované zámky, zajišťující synchronizaci paralelních zápisů. |
| `hazelcast.user`          | `dev`                                            | Uživatelské jméno pro Hazelcast zámky, slouží pro identifikaci instance. |
| `hazelcast.clientconfig`  |                                                  | Pokud nestačí defaultní konfigurace clusteru Hazelcast, je možné jak server, tak klienty Hazelcast konfigurovat pomocí XML souborů. K tomu slouží property `hazelcast.config` a `hazelcast.clientconfig`, kterými je možné definovat cestu ke konfiguračnímu souboru pro hazelcast server, resp. klient. Soubory mohou být určeny buď absolutní cestou nebo relativně ke konfiguračnímu adresáři `.kramerius4`. Popis obsahu konfiguračních XML souborů najdete v dokumentaci [Hazelcast](https://docs.hazelcast.org/docs/latest/manual/html-single/#understanding-configuration) |
| `hazelcast.waitTime`      |                                              | |
| `hazelcast.leaseTime`     |                                              | |

---

## Poznámky k použití

1. **Změna cest**
    - Při přechodu z Kramerius 5 nebo jiné instalace je potřeba nastavit `objectStore.path` a `datastreamStore.path` tak, aby odkazovaly na existující úložiště.
    - Při nové instalaci doporučujeme zachovat defaultní hodnoty.

2. **Změna patternu**
    - Pattern `##/##` znamená 2 úrovně adresářů, vhodné pro běžné instalace.
    - Pro velmi velké instalace (stovky milionů dokumentů) doporučujeme `##/##/##`.

3. **Hazelcast**
    - Parametry `hazelcast.instance` a `hazelcast.user` lze měnit pouze při znalosti distribuční konfigurace clusteru.
    - Pokud není cluster Hazelcast použit, defaultní hodnoty postačují.

4. **Přetížení defaultních hodnot**
    - Vlastní `configuration.properties` umístěný v `$USER_HOME/.kramerius4/` přepíše libovolnou defaultní hodnotu.

