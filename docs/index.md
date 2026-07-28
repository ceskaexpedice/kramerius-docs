# Úvod

Kramerius je modulární platforma pro správu, ukládání a zpřístupnění digitálních knihovních dokumentů.

Tato dokumentace je určena organizacím, které systém Kramerius provozují, spravují nebo rozvíjejí. Najdou zde informace pro kurátory digitálních knihoven, 
administrátory systému i vývojáře rozšiřujících nebo integračních řešení.

Dokumentace není určena koncovým uživatelům (čtenářům digitálních knihoven), ale zaměřuje se na správu, konfiguraci, provoz a vývoj systému.
Tato dokumentace pokrývá celý životní cyklus systému Kramerius – od práce s digitálními dokumenty přes správu a konfiguraci 
až po vývoj a integraci jednotlivých komponent.

---

<style>
  .doc-chat-launch {
    margin: 8px 0 12px;
  }

  .doc-chat-launch__button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 40px;
    border: 0;
    border-radius: 4px;
    padding: 0 16px;
    background: #1f6feb;
    color: #fff;
    font: inherit;
    font-weight: 600;
    cursor: pointer;
  }

  .doc-chat-launch__button:hover {
    background: #1a5fc8;
  }

  .doc-chat-launch__button:focus-visible {
    outline: 3px solid rgba(31, 111, 235, 0.32);
    outline-offset: 3px;
  }
</style>

<div class="doc-chat-launch">
  <button type="button" class="doc-chat-launch__button" onclick="window.openKrameriusDocChat()">🤖 Zeptat se AI asistenta</button>
</div>

<kramerius-doc-chat api-url="https://ai-api.inovatika.dev/kramerius-doc-api/" use-mock-response=false></kramerius-doc-chat>
<script>
  window.openKrameriusDocChat = function () {
    if (!window.krameriusDocChat) {
      throw new Error('Kramerius doc chat neni nacteny.');
    }

    window.krameriusDocChat.open();
  };
</script>
<script type="module" src="assets/kramerius-doc-chat-ui/doc-chat-ui.js"></script>

> Tip: Můžete hledat „jak importovat dokument“, „co je metadata“, „problém s indexací“ apod.

---

## Kurátor / práce s dokumenty

Práce s digitálními dokumenty, sbírkami a jejich zpracováním.

👉 **[Návody pro kurátory](guides/curator/index.md)**
- import dokumentů
- indexace
- práce se sbírkami
- sledování procesů
- zapojení knihovny do ČDK

👉 **[Doménové pojmy](domain-concepts/index.md)**
- dokument
- metadata
- sbírka
- licence
- import

---

## Administrátor / provoz systému

Správa systému, procesů a konfigurace.

👉 **[Návody pro administrátora](guides/admin/index.md)**
- monitoring procesů
- správa běžících úloh
- konfigurace systému

👉 **[Konfigurace](configuration/index.md)**
- nastavení Krameria
- indexace
- storage a úložiště

👉 **[Deployment](deployment/index.md)**
- nasazení systému
- runtime prostředí
- Tomcat / služby

---

## Vývojář / integrace

Integrace, API a interní fungování systému.

👉 **[Reference](reference/index.md)**
- REST API
- datové modely
- formáty (FOXML, METS)

👉 **[Technické koncepty](core-concepts/index.md)**
- Akubra
- procesní platforma
- indexace
- security model

👉 **[Architektura](architecture/index.md)**
- komponenty systému
- vazby mezi moduly

---

## Rychlé vstupy

Pokud víte, co hledáte:

- [Doménové pojmy](domain-concepts/index.md)
- [Technické koncepty](core-concepts/index.md)
- [Návody](guides/index.md)
- [Reference](reference/index.md)
- [Verzovani](versioning/index.md)

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
