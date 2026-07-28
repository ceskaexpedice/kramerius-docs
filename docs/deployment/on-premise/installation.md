[Úvod](../../index.md) > [Deployment](../../deployment/index.md)

# Popis instalace a nastavení On premise

Před instalací aplikace Kramerius je třeba nainstalovat následující systémové komponenty:
* **Java: JDK 21**, je možno využít javu z balíčku OpenJDK případně Oracle JDK. 
    * Instalační balíčky naleznete zde [OpenJDK](https://openjdk.org/), [Oracle JDK](https://www.oracle.com/java/technologies/downloads/) 
* **Aplikační server: Tomcat 9.x nebo novejsi**
    *  Stáhnout Apache Tomcat je možno [zde](https://tomcat.apache.org/download-90.cgi)
* Databáze: **Postgres 8.4 nebo novější**
    * Stáhnout databázi je možno [zde](https://www.postgresql.org/download/), případně je možno využít [docker image](https://hub.docker.com/_/postgres) nebo předpřipravené image z projektu [bitnami](https://bitnami.com/stack/postgresql/containers) 
* Vyhledávací engine **Solr verze  8.0 a vyšší**
    * Pro instalaci je možno využít samostatného balíku dostupného [zde](https://solr.apache.org/downloads.html). 
    * V případě provozování v Dockeru nebo Kubernetes doporučujeme využít již předpřipravené image z projektu [bintami](https://bitnami.com/stack/solr) nebo [solr operator](https://solr.apache.org/operator/).  
* Autentizační server **Keycloak**
    * Server je možno stáhnout [zde](https://www.keycloak.org/downloads). Verze může být jakákoliv z volně dostupných. 
    * **Důležitá poznámka: Pro rozchození Federace eduID je nutné řešit pomocí klonu keycloaku, popis instalace je přítomen zde [keyckloak-eduid](https://github.com/ceskaexpedice/kramerius/wiki/Guides_Security_Keycloak-a-eduID)** 
* Webový server **Apache httpd** nebo **Nginx**
    * Verze může být jakákoliv z volně dostupných. 



---
U komponent u kterých není uvedené specifické jméno revize je rozumné používat jejich aktualizace. Popis instalace a administrace těchto systémových komponent není součástí této dokumentace, předpokládáme, že administrátor aplikace Kramerius 7 ovládá instalaci a administraci výše uvedených komponent.

Operační systém může být libovolný, na kterém je možno tyto komponenty provozovat, vlastní aplikace Kramerius žádné speciální požadavky na systém nemá. Systém je vyvíjen a testován na běžných distribucích Linuxu. Hardware serveru musí být dimenzován na uvažované množství dat, doporučujeme minimálně dvojnásobnou velikost pevného disku, než je plánovaná velikost obrazových dat. Vzhledem k velké paměťové náročnosti práce s grafickými daty (náhledy stránek, zoomování) je třeba i při minimálním provozu aplikace alespoň 8GB RAM. 

Kramerius je vhodné nainstalovat pod samostatným uživatelským účtem, například kramerius.

V produkčním prostředí je před J2EE server (Tomcat) vhodné předřadit webserver přístupný na portu 80, například Apache s nakonfigurovanými moduly mod_proxy a mod_proxy_ajp.

Každou komponentu systému Kramerius (tedy vlastní aplikaci Kramerius (search.war), indexer SOLR, databázi PostgreSQL)  je možné nainstalovat na samostatný server.  

### Distribuční soubory

Distribuční soubory jádra aplikace Kramerius najdete v sekci [Releases](https://github.com/ceskaexpedice/kramerius/releases)  

Všechny soubory jsou zabaleny do jednoho archivního souboru kramerius-x.x.x.zip (znaky x.x.x jsou samozřejmě nahrazeny konkrétním číslem verze). 

Pokud v konkrétním release některý z uvedených souborů chybí, znamená to, že v něm oproti předchozí verzi nedošlo k žádné změně.

V následujících odstavcích jsou uvedeny požadavky aplikace Kramerius na specifickou konfiguraci systémových komponent, pokud možno i s odkazy na příklady konkrétních úprav příslušných konfiguračních souborů. Tyto příklady jsou uvedeny pouze pro ilustraci jedné z možných konfigurací a nenahrazují dokumentaci k jednotlivým systémovým komponentám. V případě distribuované instalace je třeba uvedené příklady konfiguračních URL (localhost) nahradit adresami příslušných serverů. 

(v uvedených příkladech konfigurace předpokládáme instalaci Tomcatu do domácího adresáře uživatele kramerius4)

# PostgreSQL

* Vytvořit uživatele `fedoraAdmin` a pro něj databázi `kramerius4` a [nastavit datasource](https://github.com/ceskaexpedice/kramerius/wiki/Guides_Instalace#konfigurace-datasource). 


## Konfigurace úložiště Akubra

Umístění datových souborů je určeno následujícími parametry v souboru `configuration.properties`:

➡️ [Konfigurace Akubra](../../configuration/core/configuration-properties/configuration-akubra.md)

## Instalace indexu (SOLR)
1. Stáhněte si poslední verzi vyhledávacího enginu [SOLR](https://lucene.apache.org/solr/downloads.html) 
2. Spustěte příkazem  `<solr_home>/bin/solr start`
3. Nainstalujte potřebná jádra (Solr core), viz ➡️ [Konfigurace Vyhledavani](../../configuration/search/index.md)


# Instalace Tomcatu a jádra aplikace 

## Administrační aplikace 
Postup instalace je stejný jako u předchozí verze Kramerius 5. Zkopírujte soubor `search.war` do adresáře `<catalina_home>/webapps`.
Ve spouštěcím skriptu Tomcatu nastavte dodatečné spouštěcí parametry pro aplikační server : `-Djava.awt.headless=true  -XX:MaxPermSize=128m -Xms512m -Xmx1024m` 

## Autentizace  
Autentizace je řešena pomocí autentizačního serveru keycloak. Je nutno provést následující kroky. 

1. Přihlásit se do administračního prostředí keycloaku 
2. Vytvořit nový realm s názvem **kramerius**
3. Vytvořit roli s názvem **kramerius_admin**
4. V seznamu uživatelů vytvořit uživatele/administrátora a přiřadit výše zmíněnou roli 
5. V seznamu "clients" vytvořit nového klienta s názvem "krameriusClient", který má nastavené/povolené následující možnosti: 
   * Valid redirect URIs: ```*```
   * Web origins: ```*```
   * Web origins: ```*```
   * Client authentication: **ON**  
   * Authorization: **ON**  
   * Standard flow: **ON**  
   * Direct access grants: **ON**  
   * Implicit flow: **ON**  
   * OAuth 2.0 Device Authorization Grant: **ON**  
   * Front channel logout: **ON**
   * Backchannel logout session required: **ON**

Konfiguraci klienta je nutno exportovat ve formátu Keycloak OIDC JSON (kontextové menu Action -> Download adaptor configs) a uložit do konfiguračního adresáře: 
~/.kramerius4/keycloak.json

➡️ [Konfigurace Keycloak](../../configuration/security/index.md)
 

## Konfigurace datasource

Do souboru `$CATALINA_HOME/conf/context.xml` přidat definici datasource: 
```
<Resource name="jdbc/kramerius4" auth="Container" type="javax.sql.DataSource"
  initialSize="3"
  maxTotal="100" maxIdle="30" maxWaitMillis="10000"
  username="fedoraAdmin" password="fedoraAdmin" driverClassName="org.postgresql.Driver"
  url="jdbc:postgresql://localhost/kramerius4"/>

```

## Nastavení kódování URI

V aplikačním serveru nastavte kódování URI na UTF-8


# Import a  migrace dat

Pro import dat lze využít standardních importních procesů. 
* Import standardních foxml dat 
* Import NDK  balíčků 
* Replikace K4.

 
# Synchronizace paralelních zápisů

Synchronizace paralelních zápisů do jednoho úložiště z více souběžných procesů a případně více instancí Krameria je zajištěna sdílenou tabulkou zámků v distribuované paměťové databázi Hazelcast. Synchronizace probíhá automaticky a defaultní nastavení není obvykle třeba měnit. K nastavení jména instance a uživatele lze případně použít následující property:  

➡️ [Konfigurace Hazelcast](../../configuration/core/configuration-properties/configuration-akubra.md)


# [Konfigurace IIIF](../../configuration/iiif/index.md)

volitelné nastavení

# Aktualizace na novou verzi Krameria

Při aktualizaci existující instalace Krameria stačí na aplikační server nainstalovat nové verze souborů `*.war` (a případně sdílené knihovny `securtiy-core.jar` ) z distribučního balíčku `Core-x.x.x.tar.gz` a `security-core-x.x.x.tar.gz`. Konfiguraci systému a ostatních komponent z balíčku `installation-x.x.x.zip` a `Editors-x.x.x.zip` není obvykle třeba měnit (pokud u konkrétní verze není uvedeno jinak). 

Postup instalace je závislý na konkrétním aplikačním serveru. Pro server Tomcat je vhodné postupovat takto:
   
* vypněte Tomcat
* **Důležité:** smažte rozbalené adresáře `search` a `rightseditor` z adresáře `tomcat/webapps` a `tomcat/work/Catalina/localhost`
* do adresáře `tomcat/webapps` nakopírujte nové verze souborů `search.war` a `rightseditor.war`, do adresáře `tomcat/lib` soubor `security-core.jar`   
* restartujte Tomcat

Pokud se liší nasazené a nové schéma solr jádra `search` (soubor `managed-schema`), proveďte aktualizaci schématu na vyšší verzi, jako je to popsáno  [zde](https://github.com/ceskaexpedice/kramerius/wiki/Guides_Instalace#aktualizace-sch%C3%A9matu-j%C3%A1dro-search) nebo [zde](https://github.com/ceskaexpedice/kramerius/wiki/Vyhled%C3%A1vac%C3%AD-index#nav%C3%BD%C5%A1en%C3%AD-verze-indexeru).

# Doporučení pro instalaci 

* Klientské systémy (klientská aplikace a administrační aplikace) by měly být provozovány za systémem apache a propojené pomocí `mod_ajp` případně `mod_jk`.
* Doporučujeme pro provozování systému Kramerius  použít protokol `https`. 


# Instalace klientské aplikace

Kramerius klient je samostatná aplikace napsaná ve frameworku angular. Její popis instalace a nastavení všech parametrů je možno najít 
[zde](https://github.com/ceskaexpedice/kramerius-web-client/wiki/Nasazen%C3%AD-klienta) 


# Instalace administrační aplikace

Administrace jádra je nyní možná ze samostatného klienta. Popis instalace je vidět [zde](https://github.com/ceskaexpedice/kramerius-admin-client/wiki/Instalace-a-konfigurace#instalace-a-konfigurace)
