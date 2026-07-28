## Podpora OAI PMH protokolu 

Systém Kramerius nyní poskytuje data pomocí protokolu OAI-PMH, což umožňuje automatizovaný sběr a sdílení metadat. Náš OAI provider je postaven na vyhledávacím indexu,
takže poskytuje pouze zaindexovaná data. Adresa providera je: `<kramerius_url>/search/api/harvest/v7.0/oai`  

---
### Dostupné metadatové formáty 

Pro sběr metadat jsou dostupné následující formáty:

* **drkramerius4**
* **dc**

Dostupné metadatové formáty na straně ČDK

* **edm**
* **dc**
 
---
### Příklady dotazů na provider 

Pro snadnější práci s providerem uvádíme několik příkladů dotazů:

* **Identifikace providera** -   [https://k7.inovatika.dev/search/api/harvest/v7.0/oai?verb=Identify](https://k7.inovatika.dev/search/api/harvest/v7.0/oai?verb=Identify)
* **Výpis metadat** - [https://k7.inovatika.dev/search/api/harvest/v7.0/oai?verb=ListMetadataFormats](https://k7.inovatika.dev/search/api/harvest/v7.0/oai?verb=ListMetadataFormats)
* **Výpis setů** - [https://k7.inovatika.dev/search/api/harvest/v7.0/oai?verb=ListSets](https://k7.inovatika.dev/search/api/harvest/v7.0/oai?verb=ListSets)
* **Výpis setů** - [https://k7.inovatika.dev/search/api/harvest/v7.0/oai?verb=ListRecords&metadataPrefix=dc](https://k7.inovatika.dev/search/api/harvest/v7.0/oai?verb=ListRecords&metadataPrefix=dc)

---
### Konfigurační parametry

Provider je možné konfigurovat pomocí následujících konfiguračních proměnných 

... presunout do kapitoly konfigurace

```
oai.adminEmail - email na administratora
oai.repositoryName - Jméno repozitáře, default hodnota je kramerius
oai.rowsInResults - Počet záznamů ve výpisu
```

### Definice nových setů 

Upravy existujících nebo nových setů je možno provádět pomocí administračního klienta. Viz následující screenshot: 
 
<img  alt="image" src="https://github.com/user-attachments/assets/e32c2b2b-73d6-4a9d-a391-f3f893453ef9" />

Tady je upravená verze, která je přehlednější a lépe strukturovaná.

Správa a definice setů
Jednotlivé sady (sety) metadat můžete snadno upravovat nebo vytvářet pomocí **administračního klienta**. Nový set definujete jako dotaz do **vyhledávacího enginu SOLR**.

Každý set obsahuje následující informace:

* **Identifikátor** a **název**
* **Stručný popis**
* **Dotaz do Solru**
* **Počet dokumentů** obsažených v setu

Set můžete editovat, mazat nebo vytvářet nový.




