# Zpracování (Processing)

Subsystém Processing je zodpovědný za asynchronní vykonávání systémových operací, jako je indexace, import a údržbové úlohy.

Je postaven nad externí platformou Process Platform (PCP), která poskytuje infrastrukturní část (manager, worker nody, lifecycle, plánování).

Kramerius nad touto platformou definuje vlastní procesy a workery.

➡️ [Process Platform](https://github.com/ceskaexpedice/process-platform/wiki)

Processing zajišťuje:

- propagaci změn z repozitáře do odvozených dat (např. vyhledávací index)
- asynchronní vykonávání dlouhotrvajících operací
- řízené a spolehlivé spouštění systémových úloh

Processing je klíčová část systému a přímo ovlivňuje:

- Vyhledávání (Search)
- konzistenci dat
- výkon systému

---

## [Kramerius workery](workers/index.md)

Kramerius definuje vlastní worker aplikace nad PCP.

Worker je typicky distribuován jako kontejnerový image a obsahuje:

- PCP runtime (např. Tomcat + REST API)
- sadu pluginů definujících konkrétní procesy Krameria

Příklad:
- CuratorWorker

Worker je zodpovědný za vykonávání konkrétních typů procesů.

V systému může běžet více worker instancí paralelně.

---

##  [Kramerius procesy (pluginy)](plugins/index.md)

Procesy reprezentují konkrétní doménové operace.

Typické procesy:

- Import
- Index
- Reindex
- údržbové operace nad daty

Každý proces:

- je vykonáván asynchronně
- běží ve workeru
- je zabalen jako plugin
- ovlivňuje repozitář a/nebo odvozená data (např. index)
  
---

## Build a deployment

Kramerius definuje workery a procesní pluginy při buildu.

- worker image obsahuje konkrétní procesy
- každý worker poskytuje určitou funkcionalitu

Nasazení workerů je popsáno v:
➡️ **[Plugin a Worker build](https://github.com/ceskaexpedice/process-platform/wiki/PluginBuild)**

---

## Shrnutí

Subsystém Processing:

- vykonává asynchronní operace systému
- je postaven nad Process Platform
- definuje konkrétní procesy a workery Krameria
- zajišťuje aktualizaci odvozených dat (např. vyhledávací index)

Představuje „write“ část systému vůči subsystémům jako je Search.

## Navazujici dokumentace

- ➡️ [Zakladni pojmy](../../core-concepts/process-platform/index.md)
- ➡️ [Architektura](../../architecture/process-platform/index.md)
- ➡️ [Konfigurace](../../configuration/process-platform/index.md)
- ➡️ [Verzovani](../../versioning/index.md)
