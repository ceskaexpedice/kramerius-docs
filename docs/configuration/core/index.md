# Kramerius Core

Po prvním spuštění aplikačního serveru s nainstalovanou aplikací Kramerius (pod systémovým uživatelem `kramerius4`) je v domovském adresáři uživatele `kramerius4` 
vytvořen adresář `.kramerius4` a v něm prázdné soubory:

### [Configuration properties](configuration-properties/index.md)
### [Search properties](https://github.com/ceskaexpedice/kramerius/blob/master/search/src/java/res/configuration.properties)
### [Migration properties (konverze z K3)](https://github.com/ceskaexpedice/kramerius/blob/master/processes/import-cmdtool/src/main/resources/res/configuration.properties)
### [Migration properties (konverze z METS-NDK)](https://github.com/ceskaexpedice/kramerius/blob/master/processes/import-mets/src/main/resources/res/configuration.properties)

Konfigurační soubory využívají rozšířenou syntaxi properties podporovanou knihovnou Apache Commons-Configuration. Soubory jsou uspořádány ve dvoustupňové hierarchii: 
základní sdílené properties jsou v souboru `configuration.properties`, jednotlivé plugin moduly externích procesů je pak rozšiřují ve svých konfiguračních souborech 
(např. `migration.properties`). Konfigurační properties specifické pro GUI jsou v souboru `search.properties`.

Defaultní hodnoty properties jsou definovány uvnitř aplikačního archivu `search.war`. Hodnoty je možné předefinovat jejich uvedením ve stejně pojmenovaném souboru 
umístěném v adresáři `$USER_HOME/.kramerius4`. Tyto konfigurační soubory (prázdné) jsou vytvořeny automaticky při prvním spuštění Krameria, resp. příslušného externího procesu.

---

## Lokalizace textů

Texty jednotlivých součástí GUI Krameria jsou lokalizovány pomocí standardního mechanismu **ResourceBundle** jazyka Java, např. [Java ResourceBundle](http://docs.oracle.com/javase/6/docs/api/java/util/ResourceBundle.html). 
Výchozí obsah lokalizačního souboru `labels.properties` je k dispozici zde:

- [labels_cs.properties](https://github.com/ceskaexpedice/kramerius/blob/master/search/src/java/labels_cs.properties)

Požadované změny je možné provádět přepsáním hodnoty příslušného klíče v souboru:

- `~/.kramerius4/bundles/labels.properties`
- `~/.kramerius4/bundles/labels_cs.properties`

## Víceřádkové texty

Pro rozsáhlejší texty má Kramerius mechanismus zápisu do samostatného souboru. Tyto soubory mohou být předefinovány v adresáři `~/.kramerius4/texts`:

| Soubor | Popis | Výchozí obsah |
|--------|-------|---------------|
| `texts/first_page_nolines_xml` | Text o nedostupnosti, který se objeví při generování PDF i v dokumentu | [first_page_nolines_xml](https://github.com/ceskaexpedice/kramerius/blob/master/shared/common/src/main/java/texts/first_page_nolines_xml) |
| `texts/help` | Obsahuje text nápovědy. Pokud není definovaný, zobrazí interní nápovědu Kramerius | - |
| `texts/rightMsg` | Text o nedostupnosti dokumentu. Pokud není definovaný, použije se klíč `rightMsg` z labels.properties | - |
| `texts/intro` | Popisný text o digitální knihovně | [intro](https://github.com/ceskaexpedice/kramerius/blob/master/shared/common/src/main/java/cz/incad/kramerius/service/impl/res/default_intro) |
| `texts/k5info` | Popisný text zobrazený v klientské aplikaci | [k5info](https://github.com/ceskaexpedice/kramerius/blob/master/shared/common/src/main/java/cz/incad/kramerius/pdf/impl/res/k5info) |


## Navazujici dokumentace

- ➡️ [Reference](../../reference/core/index.md)

