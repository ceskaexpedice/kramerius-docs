# Vyhledavani

Konfigurace přístupu k SOLR se děje skrze Kramerius Core:
➡️ [Vyhledávání](../core/configuration-properties/configuration-solr.md)

Zvazime take pouziti:
➡️ [Solr Cloud](solr-cloud.md)


## jádro Search
Jádro je určeno pro vyhledávání klientskými aplikacemi (veřejné, admininstrační rozhraní digitální knihovny). Popis instalace:

- V [administračním rozhraní](http://localhost:8983/) spuštěné instance vyhledávacího enginu solr vytvořte nové vyhledávací jádro.
    - Standardní název je `search`. Pokud je potřeba zvolit jiný název nebo je nutno provozovat solr na jiném portu, je nutno  změnit defaultní [konfiguraci](https://github.com/ceskaexpedice/kramerius/blob/master/shared/common/src/main/java/res/configuration.properties#L11).
- Postup pro vytvoření jádra je analogický k tomu, co je uvedeno [zde](https://github.com/ceskaexpedice/kramerius/wiki/P%C5%99echod-na-novou-verzi-SOLR).
    - Nejdříve je nutno zkopírovat vše z instalačního adresáře [kramerius-7.x.y.zip/installation-7.x.y/solr-7.x/search](https://github.com/ceskaexpedice/kramerius/tree/master/installation/solr-7.x/search) do
      adresáře `<solr_home>/server/solr/search` a poté v administračním rozhraní přidat jádro se jménem `search` a instalačním adresářem `search`.

## jádro Processing
Vyhledávací jádro nahrazuje funkcionalitu resource indexu (dříve používaný repozitář Fedora). Jde o interní index repozitáře.
Každý nově importovaný objekt je nyní popsán v tomto indexu spolu se svými vazbami.  Postup instalace je následující:
- V [administračním rozhraní](http://localhost:8983/) spuštěné instance vytvořte jádro `processing` obdobným způsobem, jako bylo vytvořeno jádro `search`.
    - Změna portu nebo názvu jádra je opět možná pomocí  možná pomocí [konf. souboru](https://github.com/ceskaexpedice/kramerius/blob/master/shared/common/src/main/java/res/configuration.properties#L12).
- Konf soubory pro jádro processing jsou v instalačním adresáři [kramerius-7.x.y.zip/installation-7.x.y/solr-7.x/processing](https://github.com/ceskaexpedice/kramerius/tree/master/installation/solr-7.x/processing/).

## jádro Logs
Jádro slouží pro ukládání informací o přístupu uživatelů. A následně jako zdroj dat pro generování statistika a reportů.
Popis instalace:

- V [administračním rozhraní](http://localhost:8983/) spuštěné instance vyhledávacího enginu solr vytvořte nové vyhledávací jádro s názvem logs.
- Postup pro vytvoření jádra je analogický k tomu, co je uvedeno [zde](https://github.com/ceskaexpedice/kramerius/wiki/P%C5%99echod-na-novou-verzi-SOLR).
    - Nejdříve je nutno zkopírovat vše z instalačního adresáře [kramerius-7.x.y.zip/installation-7.x.y/solr-7.x/logs](https://github.com/ceskaexpedice/kramerius/tree/master/installation/solr-7.x/logs) do adresáře <solr_home>/server/solr/logs a poté v administračním rozhraní přidat jádro se jménem logs a instalačním adresářem logs.

## jádro Monitor
...

## jádro sdnnt-sync
...

## Aktualizace schématu 



### Aktualizace schématu (jádro search) - single solr

Při přechodu na některou vyšší verzi Krameria může nastat potřeba aktualizovat schéma (zejména soubor `managed-schema`) Postup je následující:

- Stáhněte si konfigurační soubory a slovníky z instalačního balíčku. Verze instalačních balčků je [zde](https://github.com/ceskaexpedice/kramerius/releases) 
- Stáhnuté soubory umístěte do adresáře `<solr_home>/server/solr/search`. 

![solr-path](../assets/solr-core-path.png)


- Otevřte administrační prostředí solru `http://localhost:8983/`.


- V záložce core-admin vyberte jádro `search` a zmáčkněte tlačítko `reload`.

![solr-admin-reload](../assets/solr-admin-reload.png)



### Aktualizace schématu (jádro search) - solr cloud

...

## Navazujici dokumentace

- ➡️ [Reference](../../reference/search/index.md)

