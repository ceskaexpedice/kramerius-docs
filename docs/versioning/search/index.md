Popis aktuální podoby schématu: [Google spreadsheet](https://docs.google.com/spreadsheets/d/1DoDnSIGPqPnYbb0U2RSNLKm9eAY2FQNimJyTPeQsC2A/edit#gid=0)

# Přehled verzí Indexeru #
Pokud nastane změna v indexování (konverze dat Repozitář -> Index), je navýšena verze Indexeru.
Objekty indexované předchozími verzemi Indexeru jsou poté považovány za zastaralé a je vhodné je přeindexovat.

Není to ale nutné. Pokud je změna v Indexeru irelevantní pro daný objekt, vše bude stejně fungovat i bez reindexace.
Např. máme-li monografii bez souřadnice zaindexovanou ve verzi 2, a nasadíme jádro (search.war) s Indexerem ve verzi 3, reindexace této monografie fakticky nic nezmění, jen pole _indexer_version_ bude nově obsahovat hodnotu _3_, namísto původní _2_.

Pokud je změna v indexaci relevantní pro data daného objektu, nepřeindexování způsobí omezenou funkčnost pro tento objekt. Např. nevhodné řazení podle datumů (verze 3,4) a omezené filtrování na mapě (verze 1,2,3).

Protože reindexace celého obsah (resp. modelu) trvají dlouho a stojí nějaké hardwarové zdroje, může dávat smysl provádět reindexace až po nakupení více změn. A ne nutně po každém navýšení verze, speciálně pokud se změny netýkají dat v konkrétním Repozitáři.


## Navýšení verze Indexeru ##
Verze Indexeru je navýšena, pokud se změní logika indexace/konverze dat.

Někdy může být součástí změny také aktualizace solr schématu. Změna je vždy zpětně kompatibilní, typicky přidání nového pole, není tak nutné reindexovat celý obsah Repozitáře. Je ale potřeba v takové situaci aktualizovat schéma (soubor managed_schema) následovně:
1. vypnout solr
2. nahradit soubor schématu novou verzí (soubor $SOLR_HOME/server/solr/search/conf/managed-schema)
3. zapnout solr

Vždy je ale potřeba aktualizovat jádro (search.war). Informace o aktuální verzi Indexeru je dostupná přes API jádra.
V kombinaci s informací o tom, v jaké verzi Indexeru byl objekt naposledy indexován (pole _indexer_version_), tak Admin rozhraní i klient Digitální knihovny poznají, který objekt je indexován zastarale.

## Verze 21 ##
* přidáno pole _subtype_
    * issue #1206
    * např. pro rozlišení novin od časopisů (oboje model:periodical);
    * získává se z pole `<mods:genre authority="kdccv">TADY</mods:genre>`
    * hodnota se propaguje až dolů do stránek (jen od vlastních rodičů)
* přesnější určení souřadnic
    * issue #1205
    * indexují se 2 nové, přesnější formáty zápisu bounding boxu:
        * (W 25.4167° -- E 63.5000° / N 37.5333° -- S 34.8542°)
        * (-25.4167, -34.8542, 63.5000, 37.5333)
        * Více v cz.kramerius.searchIndex.indexer.conversions.extraction.CoordinatesExtractor
    * přidáno boolean pole _coords.is_point_ (true, pokud bounding box určuje bod na mapě)
    * parser je tolerantnější na nepřesný zápis pro všechny formáty (extra mezery, špatná velikost písmen třeba u "v.d."
* vylepšeno parsování datumů o další formáty
    * issue #1204
    * YYYY..YYYY
    * YYYY (YYYY)
    * tolerovány různé pomlčky, posuvníky, mínusy a podobné znaky namísto "-" pro znázornění rozsahu datumů/let/...
    * nově se parsují zápisy jako '[18--]-1891', '[18--]-[189-]', '[18uu]-[189x]'
* propagace klíčových slov až do stránek
    * issue #1203
    * pokud objekt nemá vlastní klíčová slova, použijí se klíčová slova vlastního rodiče. Případně i nevlastního, pokud to ale není sbírka.
* nová pole pro předměty
    * issue #1202
    * `subject_names_personal.search` a `subject_names_personal.facet` pro data z `mods/subject/name[@type='personal']/namePart[not(@type)]`
    * `subject_names_corporate.search` a `subject_names_corporate.facet` pro data z `mods/subject/name[@type='corporate']/namePart[not(@type)]`
    * `subject_temporals.search` a `subject_subject_temporals.facet` pro data z `mods/subject/temporal`
* nová pole pro počty potomků podle vazeb
    * issue #1150
    * existující `count_page` a `count_track` doplněny o několik dalších
    * _count_page_ - počet vazeb `hasPage` a `isOnPage`
    * _count_track_ - počet vazeb `hasTrack` a `containsTrack`
    * _count_monograph_unit_ - počet vazeb `hasUnit`, k rozlišení vícesvazků
    * _count_sound_unit_ - počet vazeb `hasSoundUnit`
    * _count_issue_ - počet vazeb `hasItem`
    * _count_volume_ - počet vazeb `hasVolume`
    * _count_internal_part_ - počet vazeb `hasIntCompPart`

## Verze 20 ##

## Verze 19 ##
* oprava schématu kvůli bugu u indexace dokumentů obsahujících geografické souřadnice
* **vyžaduje aktualizaci schématu!**

## Verze 18 ##
* doplněna pole pro lokalizovaný název a popis sbírky do obecného jazyka (_title.search_KOD-JAZYKA_, _collection.desc_KOD-JAZYKA_)
* **vyžaduje aktualizaci schématu!**

## Verze 17 ##
* doplněna podpora extrakce datumů ve formátech s nejistotou (pro lepší řazení):
    * [dd. mm. yyyy]
    * [mm.-mm.rrrr]
    * [dd.-dd.mm.rrrr]

## Verze 16 ##
* přidáno pole **licenses.facet**, které obsahuje sjednocení hodnot z polí _licenses_of_ancestors_, _contains_licenses_ a _licenses_
* umožněna indexace nekorektních OCR textů
* **vyžaduje aktualizaci schématu!**

## Verze 15 ##
* doplněno parsování datumů v dalších formátech používaných v MZK
    * nejistý rok, zaindexováno jako jistý
        * '[asi 1690]', 'asi 1690]', '[asi 1690', 'asi 1690'
    * dva roky, jen jeden z nich se vztahuje k publikaci a je použit
        * '1933, [přetisk 1936]', '2009 [soubor distribuován 2011]'
    * dva roky, není jasné, který je správný, zaindexováno jako rozmezí obou let:
        * '[1897 nebo 1898]', '[1897 nebo 1898?]', '[1897? nebo 1898]', '[1897 nebo 1898', '1897 nebo 1898]'
        * '1997 [i.e. 1998]', '1997, [i.e. 1998]', '1997, [i.e. c1998]'
        * '1948, [spr. 1947]', '1952, [v tir. spr. 1953]'
        * '1922 [na ob. 1923]', '1976, [na tit. listu nesprávně] 1975'
        * '1933, [přetisk 1936]', '2009 [soubor distribuován 2011]'
* slovní vyjádření ročního období česky; období je chápáno meteorologicky (jaro=březen-květen), nikoliv astronomicky (jaro=19./21.březen-20./22.červen na severní polokouli)
    * 'Jaro 1920', 'jaro 1920'
* slovní vyjádření měsíce (pozor, závisí na instalovaných LOCALE! tam, kde běží Indexer)
    * 'prosinec, 1999', 'prosinec 2000', 'Prosinec, 2000', 'Prosinec 2000',
    * 'march, 1999', 'march 2000', 'March, 2000', 'March 2000',
    * 'März, 2000', 'März 2000' (německy měsíc musí být velkým písmenem)
* datum se slovním vyjádřením měsíce (pozor, závisí na instalovaných LOCALE! tam, kde běží Indexer)
    * '1. února 1886', '1. Února 1886'
    * '1. March 1886', '1. march 1886'
    * '1. März 1886'

## Verze 14 ##
* oprava nekorektně zamítaných souřadnic, pokud bounding box proniká 180. poledníkem, např: _Tichý oceán_, _Čukotský autonomní okruh_
  , nebo _Nový Zéland (včetně východních ostrůvků)_

## Verze 13 ##
* oprava hodnot ukládaných do pole _pid_paths_. Doposud se pole používalo minimálně, ve většině případů ho nahradilo pole _own_pid_path_. Nově se používá v souvislosti s licencemi.
* úprava logiky pro naplňování pole _licenses_of_ancestors_ v souvislosti s licencemi od nevlastních předků (sbírky, obrázky, některé články)

## Verze 12 ##
* přidáno pole _licenses_of_ancestors_ (týká se licencí)
* upravena logika indexace lincencí: pro objekty, které jsou (vlastními) potomky objektu s licencí, se licence ukládá do pole _licenses_of_ancestors_, už ne _licenses_
* **vyžaduje aktualizaci schématu!**

## Verze 11 ##
* oprava hodnotách v poli _pid_paths_ (týká se jen sbírek)
* přidáno pole _track.length_ (délka audio v sekundách)
* **vyžaduje aktualizaci schématu!**

## Verze 10 ##
* neindexování původních jazyků překladů [#236](https://github.com/ceskaexpedice/kramerius/issues/236)
* oprava pořadí (pole rels_ext_index.sort)

## Verze 9 ##
* podpora licencí (pole _licenses_, _contains_licenses_)
* **vyžaduje aktualizaci schématu!**

## Verze 8 ##
* změna zpracování nonSort na základě realných (velmi chybových) [dat z MZK](https://docs.google.com/spreadsheets/d/1xkAhIgjN-DSSpYauMNkVUddo3y-mzT3qR_TEKOd9-2c/edit#gid=1128581108)
    * pro další zpracování jsou z hodnoty nonSort odebrání všechny začáteční a koncové mezery (proměnná _trimmed_nonsort_)
    * pro solr pole _title.search_ a _titles.search_ se spojí hodnoty _trimmed_nonsort_ a _title_ následovně:
        * pokud je _trimmed_nonsort_ prázdný: _title_
        * pokud _trimmed_nonsort_ končí na některý ze znaků **'[&quot;**: _trimmed_nonsort + " " + title_
        * jinak: _trimmed_nonsort + title_
* změna preference _titleInfo_ pro primární název (title.search): titleInfo s @type=uniform" je nově preferován před titeInfo bez @type

## Verze 7 ##
* změna pořadí v polích authors.*: pořadí je převzato z MODS (elementy name), přičemž autoři s _usage='primary'_ předcházejí ostatním autorům
* oprava špatného zápisu nonSort (chybějící mezera) pro konkrétní vyjmenované hodnoty ("The", "La", "Die", ...). Souvisí se [zavádějícím návodem v specifikaci DMF](https://github.com/NLCR/Standard_NDK/issues/154).

## Verze 6 ##
* pole _collection.desc_ je nově multiValued (český, anglický popis sbírky)
* **vyžaduje aktualizaci schématu!**

## Verze 5 ##
* odstraněno duplikování hodnot obecně pro všechna pole

## Verze 4 ##
* upraveno zpracování datumů: indexují se i některé nestandardní zápisy, doposud ignorované
    * rozsah let
        * '[mezi 1695 a 1730]', 'mezi 1620 a 1630', 'mezi 1680 a 1730]', '[mezi 1739? a 1750?]'
        * '[mezi 1897-1908]', '[mezi 1898-1914?]', '[mezi 1898?-1914]', '[mezi 1895-1919', 'mezi 1895-1919]'
    * století
        * '[18--]', '[18--?]', '18--?', '18--?]'
    * desetiletí
        * '[183-]', '[183-?]', '183-?', '183-?]', '183-'

## Verze 3 ##
* upraveno zpracování souřadnic a datumů: indexují se i některé nestandardní zápisy, doposud ignorované

## Verze 2 ##
* přidána další detekce neplatných souřadnic, opět v takovém případě špatná data nezpůsobí nezaindexování objektu, ale jen zalogování chyby

## Verze 1 ##

* přidáno pole _indexer_version_
    * udává verzi Indexeru, ve které byl konkrétní (top-level) objekt indexován; hodnota se zvýší jen při úplné (re)indexaci
    * všechny doposud indexované dokumenty, které pole nemají, budou interpretovány, jako by měly _indexer_version_ s hodnotou 0
    * číslo aktuální verze Indexeru bude dostupné přes API (GET /api/client/v6.0/info)
* přidáno pole _full_indexation_in_progress_
    * pro evidenci probíhajících úplných indexací
    * a k detekci dokumentů, u kterých úplná indexace nebyla dokončena kvůli chybám v datech některého potomka
* typ bbox je stored, v opačném případě nefunguje atomic update
* při neplatných souřadnicích (zeměpisná šířka mimo interval <-90°,90°>, nebo zeměpisná výška mimo interval <-180°,180°>) Indexer souřadnice zahazuje (a zaloguje chybu v datech), doposud to způsobovalo nedokončenou indexaci v důsledku chyby od SOLR.
* **vyžaduje aktualizaci schématu!**

## Verze 0 ##
Nultá verze, ještě neobsahuje informaci o verzi indexu.

Schéma: [https://github.com/ceskaexpedice/kramerius/blob/indexer/search-index/src/main/resources/solr_core/solr7x/search/conf/managed-schema](https://github.com/ceskaexpedice/kramerius/blob/indexer/search-index/src/main/resources/solr_core/solr7x/search/conf/managed-schema)

Testy: [https://github.com/ceskaexpedice/kramerius/tree/indexer/search-index/src/test/resources/xmlTests](https://github.com/ceskaexpedice/kramerius/tree/indexer/search-index/src/test/resources/xmlTests)

