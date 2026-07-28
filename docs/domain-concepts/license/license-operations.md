[Úvod](../../index.md) > [Doménové pojmy](../../domain-concepts/index.md)  / [Licence](../license/index.md)

Objektům v repozitáři může být přiřazena jedna nebo více licencí. Příkladem licence je _DNNT_ nebo _public domain_.
Licence, v kombinaci s dalším nastavením, umožňuje vykonávání akcí nad určenými objekty. Typickou akcí je zobrazení plných stránek.

Pokud má objekt přiřazenu licenci, licence platí pro všechny potomky objektu. A všichni případní předci licencovaného objektu mají vlastnost _"obsahuje něco s licencí"_.
#### Příklady
* Monografie M má licenci X: licence X **platí** pro **M** i pro všechny **stránky v M**
* Periodikum P má licenci X: licence X **platí** pro **P** a všechny **ročníky**, všechny **čísla** a všechny **stránky** v rámci P
* Ročník R1 periodika P má licenci X
  * licence X **platí** pro **R1**, všechny jeho **čísla** a všechny **stránky** těchto čísel
  * licence X **NEplatí** pro **P** ani ostatní ročníky **R2, R3, ...**
  * periodikum **P** má vlastnost **_obsahuje něco s licencí X_**
* Sbírka S má licenci X a obsahuje monografii M, periodikum P, grafiku G
  * licence X **platí** pro monografii **M** a všechny její **stránky**  
  * licence X **platí** pro periodikum **P**, všechny jeho **ročníky**, všechny jejich **čísla** a všechny jejich **stránky**
  * licence X **platí** pro grafiku **G** a všechny její **stránky**
* Sbírka S má licenci X a obsahuje ročník R1 periodika P
  * licence X **platí** pro ročník **R1**, všechny jeho **čísla** a všechny jejich **stránky**
  * licence X **NEplatí** pro periodikum **P**, ale **P** má vlastnost **_obsahuje něco s licencí X_**
  * licence X **NEplatí** pro ostatní ročníky P (**R2, R3, ...**)


#### Přiřazení a odebrání licence
Licenci lze objektu přiřadit nebo odebrat přes Admin rozhraní nebo přes Klienta digitální knihovny. Tyto akce mohou provádět jen autorizovaní uživatelé, na základě rolí a dalšího nastavení práv.
Akce přiřazení/odebrání licence naplánuje proces, který upravuje data v repozitáři a v indexu. To znamená, že se výsledek akce nemusí projevit okamžitě, typicky když je ve frontě více naplánovaných procesů (jakýchkoliv procesů, ne nutně jen těch souvisejících s licencemi).
#### Proces odebrání licence
Jeden objekt může mít více zdrojů stejné licence.
##### Příklad 1 
* Periodikum P má licenci X
* Sbírka S má licenci X
* Sbírka S obsahuje ročník R2, což je druhý ročník periodika P

Pokud odebereme licenci X periodiku P, licence X musí stále platit pro ročník R2, všechny jeho čísla a jejich stránky. Protože R2 má ještě jiný zdroj licence - sbírku S.

##### Příklad 2
* Periodikum P má licenci X
* Ročník R1 periodika P má číslo Č1
* Č1 má licenci X

Pokud odebereme licenci X periodiku P, licence X musí stále platit pro číslo Č1 a jeho stránky. Navíc periodikum P a ročník R1 si musí uchovat vlastnost _obsahuje něco s licencí X_.

Existuje více možných scénářů s několika zdroji licence. Proces _odebrání licence_ zajistí výslednou konzistenci dat u všech z nich s jedinou výjimkou. Tou je právě _příklad 1_. Výsledkem zde bude, že licence neplatí pro R2 (ani jeho čísla a jejich strany). Nastane tedy nekonzistence mezi daty v repozitáři a v indexu.
Situaci napraví jen plná reindexace R2, včetně jeho podstromu. Obecně platí, že plná reindexace jakéhokoliv objektu dostane objekt deterministicky do konzistentního stavu.

Proces _přidání licence_ zajistí výslednou konzistenci dat vždy.

#### Přidání/odebrání objektu do sbírky, která má licenci
Pokud odebíráme objekt ze sbírky, která má licenci, nastane podobná situace, jako při odebírání licence sbírce. Je nutné synchronizovat (záznam v indexu) pro strom objektu, který ze sbírky odebíráme. To zajistí proces _reindexace stromu_, jehož naplánování je součástí operace _odebrání objektu ze sbírky_. I zde tedy může nastat dočasná nekonzistence, dokud není dokončeno provádění procesu.

### Problémy při zásazích do repozitáře
Zásahy do dat repozitáře mimo nástroje Krameria, tedy přímé editace FOXML souborů, mohou způsobit nekonzistence, které neopraví ani plná reindexace. A také nedefinované chování jádra/API a v důsledku Admin rozhraní a Klienta digitální knihovny.
Například:
* Periodikum P má ročníky R1, R2, R3 a každý ročník má několik čísel, každé z čísel má několik stránek
* ručně přidám licenci objektu R1 editací jeho záznamu RELS-EXT ve FOXML souboru: ```<rel:license>DNNT</rel:license>```
* už nepřidám příznak "obsahuje něco s licencí" do RELS-EXT záznamu P: ```<rel:containsLicense>DNNT</rel:containsLicense>```







