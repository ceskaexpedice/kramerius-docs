# Vývojář / Integrátor

Tato stránka slouží jako **vstupní rozcestník pro vývojáře a integrátory**, kteří pracují s platformou Kramerius z pohledu **integrace, rozšiřování a vývoje vlastních řešení**.

Určeno pro **vývojáře a integrátory**, kteří:
- integrují Kramerius s externími systémy
- využívají nebo rozšiřují REST API
- vyvíjejí vlastní moduly, nástroje nebo procesy
- automatizují práci nad obsahem

## Návody
Zde jsou návody, jak v systému provést dílčí úkol

➡️ **[Návody](../guides/developer/index.md)**.

---

## Role vývojáře v Kramerius

Vývojář v Krameriovi typicky řeší:

- práci s **REST API** Krameria
- integraci s externími systémy a službami
- vývoj doplňkových modulů a nástrojů
- napojení na **procesní framework**
- testování a ladění integračních scénářů

> Tato stránka slouží jako rozcestník a checklist, nikoli jako krokový návod.

---

## S jakými částmi systému vývojář pracuje

Z pohledu vývojáře se Kramerius skládá z následujících částí:

### Kramerius Core (REST API)
Hlavní integrační rozhraní systému:
- práce s digitálními objekty a metadaty
- správa procesů
- vyhledávání a přístup k obsahu

➡️ **[REST API](../reference/api/index.md)**.

---

### UI klienti
- čtenářské UI
- Admin Client

Vývojář:
- typicky UI nerozvíjí přímo
- ale musí rozumět jeho chování a vazbě na API

➡️ Viz **[Admin klient](../reference/client-admin/index.md)**.

---

### Repository (Akubra / Fedora)
- fyzické uložení digitálních objektů
- struktura a vztahy mezi objekty

Vývojář s repozitářem obvykle pracuje **nepřímo prostřednictvím API**, ale měl by znát základní principy.

➡️ Viz **[Akubra](../reference/akubra/index.md)**.

---

### Search
- indexace a vyhledávání obsahu
- práce s dotazy, filtry a výsledky

➡️ Viz **[Search](../reference/search/index.md)**.

---

### Procesní framework
- spouštění a řízení procesů
- automatizace a dávkové operace
- možnost vývoje vlastních procesů

➡️ Viz **[Procesy](../reference/process-platform/index.md)**.

---

### Bezpečnost a autentizace
- práce s autentizací (tokeny, role)
- respektování autorizačního modelu systému
- zabezpečení API volání

➡️ Viz **[Bezpecnost](../reference/security/index.md)**.

---

## Navazujici dokumentace

- ➡️ [Základní struktura](../core-concepts/index.md)
- ➡️ [Architektura](../architecture/index.md)
- ➡️ [Konfigurace](../configuration/index.md)
- ➡️ [Deployment](../deployment/index.md)
- ➡️ [Reference](../reference/index.md)
- ➡️ [Navody](../guides/developer/index.md)
