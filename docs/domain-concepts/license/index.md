[Úvod](../../index.md) > [Doménové pojmy](../../domain-concepts/index.md)

# Licence 

Od verze [7.0.26](https://github.com/ceskaexpedice/kramerius/releases/tag/v7.0.26) přináší Kramerius rozdílné typy licencí, a to `Globální licence` a `Lokální licence`. Globální licence jsou dostupné ve všech instancích Krameria a mají platnost na globální úrovni. (V České republice nebo případně na Slovensku).  Lokální licence jsou platné pouze pro konkrétní instituci, ve které jsou používány.

### Globální licence 

Globální licence jsou následující:

* [**dnnto** - Díla nedostupná na trhu – online](dnnto.md)    
* [**dnntt** -  Díla nedostupná na trhu – studovna](dnntt.md)    
* [**public** -  Díla volně dostupná dle autorského zákona](public.md)
* [**onsite** -  Díla dostupná v prostorách knihovny](onsite.md)
* [**onsite-sheetmusic** -  Hudebniny dostupné v prostorách knihovny  ](???)
* [**officialworks** -  Úřední díla volně dostupná dle autorského zákona](official-works.md)
* [**orphan** -  Osiřelá díla](orphan.md)
* [**special-needs** -  Licence pro osoby se speciálními potřebami](special-needs.md)
* [**cover-and-content** -  Licence pro zpřístupnění obálek a obsahů pro monografie](???)

### Lokální licence 

Lokální licence mají platnost jenom v rámce dané instituce a vyznačují se tím, že mají prefix organizace. Například u knihovny akademie věd by taková licence byla `knav_pracovisteAV`.  Zkratka instituce by měla korespondovat s [registrem kramériů](https://registr.digitalniknihovna.cz/).  Zkratku je nutno nastavit v konfigurační proměnné `acronym=<zkrakta instituce>` v souboru `configuration.properties`.

Upozornění: _V administračním rozhraní lze nyní zakládat pouze **lokální** licence a prefix je automaticky dodávan admin rozhraním._
 
### Runtime licence

Od verze [7.0.41](https://github.com/ceskaexpedice/kramerius/releases/tag/v7.0.41) je v jádře podpora runtime licencí, tedy těch licencí, které nejsou součástí dokumentu ale má resp. může ji mít každý dokument, který splňuje danou podmínku. V jádře jsou nyní dvě podmínky: 

1. Celý repozitář - runtime licenci bude mít každý dokument. 
2. Obálky knih - Licenci má pouze stránka, která má v metadatech BIBLIO_MODS specifikováno, že se jedná o obálku nebo o obsah.  

    
### Zámky u licencí

Od verze [7.0.33](https://github.com/ceskaexpedice/kramerius/releases/tag/v7.0.33) je možnost mít licence, které zaručují exkluzivní přístup 
jednoho nebo více čtenářů k danému dokumentu. Licence je obohacena zámkem, který čtenář při čtení získá. Webový klient periodicky zjišťuje aktivitu uživatele a pokud vyhodnotí, že uživatel čte, posílá informace na jádro krameria, že zámek je aktivně využíván.  Pokud není, zámek se uvolní pro další čtenáře. Zámek se uvolní i v případě, že čtenár dosáhl maximálního času čtení uvedeného ve vlastnostech licence. 

Vlastnosti zámku u licence: 

* Maximální doba čtení - doba po kterou jeden uživatel může držet jeden zámek, po uplynutí se zámek automaticky uvolní.
* Refresh interval - doba po kterou by mělo dojít k volání funkce refresh ze strany klienta. (Vyhodnocení, že uživatel čte)
* Počet souběžně čtoucích čtenářů - Kolik lidí může v jeden čas aktivně využívat daný zámek
* Typ zámku, Instance - Rule - Definuje zda počitadlo soubežně čtoucích čtenářů se vztahuje k celé instanci krameria nebo zda každé pravidlo v právech má samostatné počitadlo.



 
