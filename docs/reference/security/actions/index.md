[Úvod](../../../index.md) > [Reference](../../index.md)  / [Zabezpečení](../index.md)

# Actions

Akce představují oprávnění používaná autorizačním systémem.

Seznam je k dispozici [zde](https://github.com/ceskaexpedice/kramerius/blob/master/shared/common/src/main/java/cz/incad/kramerius/security/SecuredActions.java)

## Chráněné akce

- *a_read/Číst* - Akce čti definuje operaci číst data (obrázky). _Pokud má uživatel práva tuto akci provádět, objeví se mu  velký náhled, vygeneruje PDF nebo zobrazí deepZoom prohlížečka._
- *a_pdf_read/Pdf a tisk* - Definuje použití endpointu pro generování pdf dokumentů případně tisku
- *a_delete/Mazání* - Smazání objektu, resp. spuštění procesu mazání nad objektem.
- *a_process_read/Ćtení procesů* - Možnost si číst procesy (v admin rozhraní zobrazit tabulku spuštěných procesů)
- *a_process_edit/Správa procesů* - Možnost číst a spravovat procesy (v admin rozhraní zobrazit tabulku spuštěných procesů s
  možností spravovat proces = zastavit proces, smazat proces, vstoupit do detailu a prohlížet logy). Pokud má uživatel nadefinovanou tuto akci, nemusí mít již definovanou akci _a_process_read_
- *a_owner_process_edit/Správa vlastních procesů*  - Možnost číst a spravovat _svoje_ procesy, tedy procesy spuštěné konkrétním uživatelem.
- *a_index/Indexace*  - Možnost spustit indexaci na konkrétním objektu.
- *a_rebuild_processing_index/Rebuild procssing indexu*  - Možnost spuštění procesu pro rebuild processing indexu.
- *a_import/Import* - Možnost spuštění importního procesu. Pokrývá operace import FOXML a NDK-METS balíčku.
- *a_set_accessibility/Přístupnost* - Možnost spuštění procesu nastavení nastavení přístupnosti objetů,
  pokrývá operace nastavení příznaku i nastavování a rušení licencí
- *a_set_accessibility/Přístupnost* - Možnost spustit nastavení přístupnosti případně licence
- *a_export_cdk/Export do ČDK* - Přístup pro ČDK
- *a_statistics/Statistiky* - Možnost číst statistky
- *a_statistics_edit/Editace statistik* - Možnost mazání statistik
- *a_export_replications/Export replikace* - Umožnění replikace titulu
- *a_import_replications/Import replikace* - Umožnění spuštění procesu replikace
- *a_rights_edit/Editace práv* - Umožnění editace práv
- *a_criteria_read/Kritéria* - Umožnění čtení kritérií.
- *a_collections_read/Čtení sbírek* - Umožní číst/zobrazit seznam sbírek
- *a_collections_edit/Editace sbírek* - Umožní upravovat sbírky případně vybranou sbírku
- *a_able_tobe_part_of_collections* - Právo umožní uživatelům přidávat vybrané díla do sbírek.
  V případě, že je právo nastaveno na úrovni repositáře, pak má uživatel právo přidávat všechny objekty.
- *a_generate_nkplogs/Generování NKP logů* - Akce pro spuštění generování NKP logů
- *a_roles_edit/Editace rolí* - Akce přidávání/mazaní/editace rolí
- *a_roles_read/Čtení rolí* - Akce čtení rolí
- *a_admin_read/Admin čtení* - Přístup do administračního rozhraní