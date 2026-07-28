# Dokumentace Kramerius REST API

Kramerius je systém pro správu digitálních knihoven, který poskytuje komplexní řešení pro přístup, vyhledávání a správu digitálních dokumentů. Systém Kramerius je široce využíván na různých místech, kde umožňuje přístup k digitalizovaným knihovním zdrojům pomocí REST API.

Toto REST API je standardně dostupné na nainstalovaném serveru pod kontextem: `~/search/api/*` a je formálně rozděleno na tři části:

- **[Klientská část](https://k7.inovatika.dev/search/openapi/client/v7.0/index.html)**: Umožňuje uživatelům přistupovat k dostupným zdrojům knihovny.
- **[Administrační část](https://k7.inovatika.dev/search/openapi/admin/v7.0/index.html)**: Slouží pro správu a údržbu systému.
- **[Externí část](https://k7.inovatika.dev/search/openapi/exts/v7.0/index.html)**: Endpointy pro podporu externích aplikací
- **[OAI PMH](oai-pmh-protocol.md)**: OAI


API je rozděleno do modulů pro jednodušší integraci a údržbu. Klientské části API jsou zdokumentovány pomocí **OpenAPI** a je přístupná v každé instanci K7.

**Živá dokumentace** je dostupná na serveru pod kontextem: `<server>/search/openapi/index.html`. Tato dokumentace využívá rozhraní **Swagger UI**, kde je možné jednotlivé dotazy přímo vyzkoušet a rovněž podporuje přihlášení pro práci s chráněnými API funkcemi.

Kramerius REST API poskytuje přístup k digitalizovaným zdrojům knihovny. Pomocí tohoto API mohou klientské aplikace provádět různé operace, jako je vyhledávání, přístup ke konkrétnímu obsahu a 
správa sbírek, výstřížků, administrační část poskytuje pak plnou podporu pro plnou administraci. 

---

## Pravidla pro všechny typy volání

### Formát požadavků a odpovědí

- **Struktura žádostí**: Všechny žádosti by měly být odesílány ve formátu JSON s příslušnými HTTP metodami (např. GET, POST, PUT, DELETE). Je důležité používat odpovídající hlavičky HTTP (např. `Content-Type: application/json`).

- **Odpovědi**: Standardně vrací Kramerius API odpovědi ve formátu JSON. Výjimky se vyskytují u případů, kdy jsou zdrojová data uložena v jiných formátech. Mezi tyto výjimky patří:
  - **Metadata ve formátu XML**: Některé druhy metadat, jako **Dublin Core (DC)** nebo **Biblio MODS**, jsou vraceny ve formátu XML.
  - **ALTO**: Odpovědi obsahující strukturovaná metadata o stránkách a jejich uspořádání jsou vraceny ve formátu XML.
  - **OCR text**: Výsledky optického rozpoznávání znaků (OCR) jsou vraceny ve formátu **text/plain**.
  - **Solr odpovědi**: Při použití parametru `wt=xml` v dotazech na Solr API jsou odpovědi vráceny ve formátu XML.

V těchto případech je třeba zpracovat XML či textové odpovědi podle struktury odpovídající specifikacím konkrétních formátů.

### Zpracování chyb

- Kramerius REST API používá standardní HTTP status kódy k indikaci úspěšnosti nebo selhání požadavku:
  - **200 OK**: Požadavek byl úspěšně zpracován.
  - **400 Bad Request**: Špatný formát požadavku nebo neplatné parametry.
  - **401 Unauthorized**: Neoprávněný přístup k chráněným zdrojům.
  - **403 Forbidden**: Přístup k požadovanému zdroji je zakázán.
  - **404 Not Found**: Požadovaný zdroj nebyl nalezen.
  - **500 Internal Server Error**: Interní chyba serveru.

V případě chyby API vrací chybové odpovědi ve formátu JSON.

---

## Navazujici dokumentace

- ➡️ [Zakladni pojmy](../../core-concepts/api/index.md)
- ➡️ [Verzovani](../../versioning/index.md)





