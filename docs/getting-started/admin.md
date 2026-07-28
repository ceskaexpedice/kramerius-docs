# Administrátor

Tato stránka je určena jako **vstupní rozcestník pro systémové administrátory a IT pracovníky**, kteří zajišťují instalaci, konfiguraci a provoz platformy Kramerius.

Určeno pro **administrátory Krameria**, kteří:
- instalují a nasazují systém
- konfigurují jednotlivé komponenty
- zajišťují provoz, monitoring a aktualizace
- odpovídají za bezpečnost a technické integrace

## Návody
Zde jsou návody, jak v systému provést dílčí úkol

➡️ **[Návody](../guides/admin/index.md)**.

---


## Role administrátora v Kramerius

Administrátor v Krameriovi typicky řeší:

- technickou instalaci a nasazení systému
- konfiguraci Core a navazujících komponent
- provozní dohled, monitoring a logování
- aktualizace, zálohování a obnovu dat
- nastavení bezpečnosti a integrací s externími systémy

---

## Přehled systému z pohledu administrátora

Administrátor by měl mít základní přehled o těchto částech systému:

- **Kramerius Core**  
  Centrální Java aplikace běžící v Tomcatu, poskytující REST API.

- **UI klienti**  
  Čtenářský klient a Admin Client napojené na Core.

- **Repository (Akubra / Fedora)**  
  Fyzické uložení digitálních objektů, struktura dat a zálohování.

- **Solr**  
  Indexace a vyhledávání nad digitálním obsahem.

- **Procesní framework**  
  Technický běh importních a dávkových procesů.

- **Autentizace a autorizace**  
  Integrace s IdP (např. Keycloak) a řízení rolí a oprávnění.

Detailní vysvětlení těchto pojmů najdete v části  
👉 **[Základní struktura systemu](../core-concepts/index.md)**

---

## Způsoby nasazení

Kramerius lze provozovat v různých typech prostředí:

- **Docker Compose**  
  Doporučený start pro testování a menší instalace.

- **Kubernetes**  
  Produkční provoz s důrazem na škálování a dostupnost.

- **On-premise instalace**  
  Tradiční instalace bez kontejnerizace (legacy scénáře).

Popis najdete v části  
👉 **[Deployment](../deployment/index.md)**

---

## Bezpečnost

Bezpečnost je průřezové téma, které se týká více částí systému.

Administrátor by měl rozumět:
- základním bezpečnostním principům Krameria
- vazbě mezi uživateli, rolemi a obsahem
- integraci s externím poskytovatelem identity

Detailní technické informace patří do  
👉 **[Bezpečnost](../reference/security/index.md)**

---

## Konfigurace

Jak konfigurovat základní core a integrované služby.

Detailní technické informace patří do  
👉 **[Konfigurace](../configuration/index.md)**

---

## Navazujici dokumentace

- ➡️ [Základní struktura](../core-concepts/index.md)
- ➡️ [Architektura](../architecture/index.md)
- ➡️ [Konfigurace](../configuration/index.md)
- ➡️ [Deployment](../deployment/index.md)
- ➡️ [Reference](../reference/index.md)
- ➡️ [Navody](../guides/admin/index.md)
