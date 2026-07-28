[Úvod](../../../index.md) > [Konfigurace](../../index.md)  / [Core](../index.md) / [Configuration properties](index.md)

# Monitoring dotazu

Tato stránka poskytuje **referenční přehled konfiguračních parametrů Monitoring**. Obsahuje defaultní hodnoty, účel a doporučené nastavení.

Konfigurace se načítá z:

- **Default**: uvnitř JAR souboru knihovny `configuration.properties`
- **Uživatelské přetížení**: soubor `$USER_HOME/.kramerius4/configuration.properties`

Uživatel může ve svém souboru předefinovat libovolnou hodnotu z defaultního souboru.

Od verze 7.0.40 je možno monitorovat dotazy, u kterých je delší doba odpovědi než je definovaná hodnota threshold. 
Jednotlivé události jsou ukládány v solr jádře monitor.
---

| Parametr | Popis                                                                                                                  | Default / Příklad |
|-----------|------------------------------------------------------------------------------------------------------------------------|-------------------|
| `api.monitor.threshold` | Threshold in milliseconds for monitoring events. Events with duration above this value will be recorded.               | `1000`            |
| `api.monitor.point` | Endpoint for recording monitoring events. 'monitor' is the Solr core where events are stored.                          | `http://localhost:8983/solr/monitor`              |
| `labels` | Label to be included with each monitoring event. This allows distinguishing between different instances of Kramerius. (e.g., in a cloud or clustered environment where each node has a unique name). | `Instance_name` |

---
