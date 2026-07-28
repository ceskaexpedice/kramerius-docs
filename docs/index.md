# Úvod

Kramerius je modulární platforma pro správu, ukládání a zpřístupnění digitálních knihovních dokumentů.

Tato dokumentace je určena organizacím, které systém Kramerius provozují, spravují nebo rozvíjejí. Najdou zde informace pro kurátory digitálních knihoven, 
administrátory systému i vývojáře rozšiřujících nebo integračních řešení.

Dokumentace není určena koncovým uživatelům (čtenářům digitálních knihoven), ale zaměřuje se na správu, konfiguraci, provoz a vývoj systému.
Tato dokumentace pokrývá celý životní cyklus systému Kramerius – od práce s digitálními dokumenty přes správu a konfiguraci 
až po vývoj a integraci jednotlivých komponent.

---

## Kde začít?

<div class="grid cards" markdown>

-   :fontawesome-solid-book:{ .lg .middle } __Kurátor / práce s dokumenty__

    ---

    Import dokumentů, indexace, práce se sbírkami, sledování procesů a zapojení knihovny do ČDK.

    [:octicons-arrow-right-24: Návody pro kurátory](guides/curator/index.md)

-   :fontawesome-solid-server:{ .lg .middle } __Administrátor / provoz systému__

    ---

    Správa procesů, konfigurace, monitoring a nasazení systému Kramerius.

    [:octicons-arrow-right-24: Návody pro administrátory](guides/admin/index.md)

-   :fontawesome-solid-code:{ .lg .middle } __Vývojář / integrace__

    ---

    REST API, datové modely, formáty, komponenty systému a jejich vzájemné vazby.

    [:octicons-arrow-right-24: Informace pro vývojáře](getting-started/developer.md)

</div>

## Přehled dokumentace

<div class="grid cards" markdown>

-   :fontawesome-solid-circle-info:{ .lg .middle } __Doménové pojmy__

    ---

    Dokumenty, metadata, sbírky, licence, importy a další základní pojmy systému.

    [:octicons-arrow-right-24: Zobrazit pojmy](domain-concepts/index.md)

-   :fontawesome-solid-book:{ .lg .middle } __Návody__

    ---

    Praktické postupy pro kurátory, administrátory a vývojáře.

    [:octicons-arrow-right-24: Zobrazit návody](guides/index.md)

-   :fontawesome-solid-code:{ .lg .middle } __Technické koncepty__

    ---

    Akubra, procesní platforma, vyhledávání, zabezpečení, ČDK a API.

    [:octicons-arrow-right-24: Zobrazit koncepty](core-concepts/index.md)

-   :fontawesome-solid-sitemap:{ .lg .middle } __Architektura__

    ---

    Komponenty systému Kramerius, jejich odpovědnosti a vzájemné vazby.

    [:octicons-arrow-right-24: Zobrazit architekturu](architecture/index.md)

-   :fontawesome-solid-server:{ .lg .middle } __Konfigurace a nasazení__

    ---

    Nastavení jednotlivých komponent a provoz v Dockeru, Kubernetes i on-premise.

    [:octicons-arrow-right-24: Konfigurace](configuration/index.md)
    [:octicons-arrow-right-24: Nasazení](deployment/index.md)

-   :fontawesome-solid-book-open:{ .lg .middle } __Reference a verzování__

    ---

    Detailní technická reference, kompatibilita komponent a pravidla vydávání.

    [:octicons-arrow-right-24: Reference](reference/index.md)
    [:octicons-arrow-right-24: Verzování](versioning/index.md)

</div>

## Co je Kramerius

Kramerius je open-source systém pro správu a zpřístupnění digitálních knihovních sbírek.

Používá se pro:

- digitalizované knihy a periodika
- mapy, hudebniny a archivní materiály
- born-digital dokumenty

Klíčové vlastnosti:

- dlouhodobé úložiště digitálních objektů (Akubra)
- indexace a vyhledávání (Solr)
- řízení importních a dávkových procesů
- správa přístupových práv
- REST API
- klientské aplikace (administrace + čtení)

Jádro systému běží jako Java aplikace v Tomcatu a tvoří integrační vrstvu nad jednotlivými komponentami.

---

## Verze a vydávání

Informace o verzování produktů, kompatibilitě jednotlivých komponent a pravidlech vydávání.

👉 **[Verzování](versioning/index.md)**

- schéma verzování Kramerius Core
- verzování Process Platform a Akubra
- kompatibilita komponent
- pravidla pro hotfixy

---

## Přispívání

Dokumentace se vyvíjí spolu se systémem Kramerius.

Struktura je navržena tak, aby:

- byla stabilní v čase
- podporovala různé role uživatelů
- umožňovala rozšiřování systému bez redesignu dokumentace  
