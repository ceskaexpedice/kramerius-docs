# 📖 Reference

Tato kapitola obsahuje technickou referenci jednotlivých částí systému. Každá podkapitola popisuje konkrétní modul, jeho rozhraní, konfiguraci a způsob použití.

---

## Hlavní komponenty

Systém obsahuje následující komponenty:

| Komponenta          | Účel                             | Zdroj                                                                                                                | Verze         | Distribuce |
|---------------------|----------------------------------|----------------------------------------------------------------------------------------------------------------------|---------------|------------|
| Kramerius Core      | REST API, integrace              | [https://github.com/ceskaexpedice/kramerius](https://github.com/ceskaexpedice/kramerius)                             | 7.2.1       | Kramerius  |
| Reader UI           | uživatelské rozhraní pro čtenáře | [https://github.com/ceskaexpedice/kramerius-web-client-v3](https://github.com/ceskaexpedice/kramerius-web-client-v3) | 3.0.20-beta   | Kramerius  |
| Admin UI            | administrace systému             | [https://github.com/ceskaexpedice/kramerius-admin-client](https://github.com/ceskaexpedice/kramerius-admin-client)   | 1.6.1         | Kramerius  |
| Keycloak            | autentizace                      | [https://www.keycloak.org/](https://www.keycloak.org/)                                                               | 22.0.11-1.10  | Kramerius|
| Solr                | vyhledavani                      | [https://solr.apache.org/](https://solr.apache.org/)                                                                 | 9.6.0         |Oficialni|
| Fedora / Akubra     | repository a storage             | [https://github.com/ceskaexpedice/akubra](https://github.com/ceskaexpedice/akubra)                                   | 1.7           |Kramerius|
| Image Server        | poskytování obrazových dat       | [https://hub.docker.com/r/ceskaexpedice/iipsrv-nginx](https://hub.docker.com/r/ceskaexpedice/iipsrv-nginx)           | vlastni build |Kramerius|
| Process Platform    | orchestrace background procesů   | [https://github.com/ceskaexpedice/process-platform](https://github.com/ceskaexpedice/process-platform)               | 1.5.1         |Kramerius|
| PostgreSQL          | persistence                      | [https://www.postgresql.org/](https://www.postgresql.org/)                                                           | 14.10         |Oficialni|
| Hazelcast           | distribuované zámky              | [https://github.com/ceskaexpedice/hazelcast-locks-server](https://github.com/ceskaexpedice/hazelcast-locks-server)   | 2.0           |Kramerius|

Minimální doporučená verze jádra pro ČDK:   7.2.1

Minimální doporučená verze jádra pro SDNNT: 7.2.1

---

## [REST API](api/index.md)
Dokumentace veřejného i interního API. Popisuje dostupné endpointy, formáty požadavků a odpovědí a autentizační mechanismy.

## Systém
Popisuje technické chování systému a jeho komponent.

### [Kramerius Core](core/index.md)
Jádro aplikace.

### [Akubra - úložiště dokumentů](akubra/index.md)
Modul pro práci s digitálním obsahem a správu repozitářů. Obsahuje pravidla pro ukládání, verzování a manipulaci s daty.

### [Vyhledávání](search/index.md)
Vyhledávací modul. Indexace dat, dotazovací API a konfigurace fulltextového vyhledávání.

### [Zabezpečení](security/index.md)
Bezpečnostní model systému. Autentizace, autorizace, správa tokenů a bezpečnostní politiky.

### [Process Platform](process-platform/index.md)
Jádro systému pro správu a vykonávání procesů. Popis workflow, plánování a komunikace mezi komponentami.

### [Distribuované zámky](distributed-locks/index.md)
Mechanismy pro distribuované zamykání v rámci clusteru. Popis implementace a použití pro synchronizaci procesů.

### [Image Server](image-server/index.md)
Služba pro ukládání, zpracování a poskytování obrázků. Obsahuje API pro transformace a optimalizaci.

### [Statistiky](statistics/index.md)
Modul pro sběr a vyhodnocování statistik. Reporty, agregace dat a analytické výstupy.

### [ČDK](cdk/index.md)
Ceska digitalni knihovna

### [Web klient](client/index.md)
Referenční popis klientské aplikace pro koncové uživatele. Obsahuje architekturu, integrace a základní chování UI.

### [Admin klient](client-admin/index.md)
Administrátorské rozhraní klientské aplikace. Slouží ke správě uživatelů, oprávnění a systémových nastavení.

---

## Operations
Popisuje provozní aspekty systému.

### [Monitoring](monitoring/index.md)
Systém pro sledování stavu aplikací a infrastruktury. Metriky, logy, alerty a dashboardy.

### [DevOps](devops/index.md)
Procesy a nástroje pro CI/CD, nasazování, monitoring buildů a správu provozního prostředí.

### Zalohovani](backup/index.md
...

---

## Navazujici dokumentace

- ➡️ [Architektura](../architecture/index.md)
- ➡️ [Reference](../reference/index.md)
- ➡️ [Navody](../guides/index.md)




