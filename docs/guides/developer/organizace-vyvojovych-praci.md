# Úkoly (issues)
* K evidenci úkolů využíváme prostředí Github
* Jednotlivá issue evidujeme u příslušné Github repository:
    * [Kramerius](https://github.com/ceskaexpedice/kramerius/issues)
    * [ČDK](https://github.com/ceskaexpedice/ceska-digitalni-knihovna/issues)
    * [Kramerius web klient](https://github.com/ceskaexpedice/kramerius-web-client/issues)
    * etc
* Pro dalsi pohledy na organizaci issues vytváříme Github projekty
# Projekty
Projekty vytváříme, protože potřebojeme organizovat issues z různých pohledů. Zde jsou existující projekty: [Projekty](https://github.com/orgs/ceskaexpedice/projects?query=is%3Aopen)
* Issues vznikaji v jednotlivých Github repositories a lze je následně přiřadit do jednoho nebo více projektů
* Pohledy na issue v jednotlivých projektech lze obohatit o různé informace, které daný projekt potřebuje
* Významnou informací u jednotlivých issue z hlediska plánování je odhadovaný čas na vyřešení, datum ETA a stav issue
V současné době využíváme tyto projekty:
* [Kramerius NPO](https://github.com/orgs/ceskaexpedice/projects/3/views/1) - úkoly NPO do konce roku pro potřeby projektového plánování
* [Interní řízení projektů (Kramerius, CDK)](https://github.com/orgs/ceskaexpedice/projects/5/views/1) = typicky adHoc úkoly, které nemají pevný deadline. Jako příklad takového úkolu může být tento [CDK ticket ](https://github.com/orgs/ceskaexpedice/projects/5/views/1?pane=issue&itemId=94893980&issue=ceskaexpedice%7Cceska-digitalni-knihovna%7C92)
# Stavy issue (Status)
Každé issue prochází těmito stavy (pole Status): Todo, In Progress, In Review, Done
## Status ToDo 
Tento stav získá issue po svém založení. Issue typicky eviduje uživatel aplikace u příslušné Github repository
## Status In Progress
### Vytvoření branch podle jmenné konvence
`{bugfix|feature|hotfix}/[projekt]-cisloIssue-[popis issue]`

Příklad: 
* feature/1106
* feature/cdk-1106
* feature/cdk-1106-merge

Údaj o projektu se využije například pokud vytváříme branch v projektu kramerius, ale inciciátorem je ticket vytvořený v repository CDK.
### Pull request
[Pull request](https://github.com/ceskaexpedice/kramerius/pulls) ma asociované tyto aktivity:
* Je nastaven reviewer pro code review
* Pomocí Github actions se automaticky provede build spolu se spuštěním JUnit testů. Lze nastavit i požadovaný [Code Coverage](https://github.com/marketplace/actions/code-coverage-summary). Další možnosti z [Github marketplace](https://github.com/marketplace?query=test)
* Po úspěšném code review se provede merge do hlavní větve

## Status In Preview
Stav nastaví programátor a tento stav je spojován s těmito aktivitami:
* vytvoření build a nasazení na testovací prostředí Inovatika, kde může autor issue řešení otestovat
* Build lze také nastavit na testovacím prostředí zákazníka
* Pokud nelse ani jeden způsob testování provést, provede se testování po následujícím release. Pokud se objeví chyba, provede se reopen daného issue
## Status Done
Nastaví autor issue po otestování a schválení


