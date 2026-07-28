[Úvod](../../../index.md) > [Konfigurace](../../index.md)  / [Core](../index.md) / [Configuration properties](index.md)

# Process platform konfigurace

Tato stránka poskytuje **referenční přehled konfiguračních parametrů Process Platform**. Obsahuje defaultní hodnoty, účel a doporučené nastavení.

Konfigurace se načítá z:

- **Default**: uvnitř JAR souboru knihovny `configuration.properties`
- **Uživatelské přetížení**: soubor `$USER_HOME/.kramerius4/configuration.properties`

Uživatel může ve svém souboru předefinovat libovolnou hodnotu z defaultního souboru.

---

| Parametr | Popis | Výchozí hodnota |
|-----------|--------|----------------|
| `processManagerUrl` |  | `http://processManager:8080/process-manager/api/` |

## Token pro procesy

Vybrané procesy vyžadují pro komunikaci s API Krameria autorizaci. K tomuto účely se využívá servisní účet (Keycloak), 
který se definuje v konfiguraci pomoci následujících parametrů:

| Parametr                 | Popis | Výchozí hodnota |
|--------------------------|--------|----------------|
| `process.token.clientId` |  | |
| `process.token.secret`   |  |  |

## Parametry Public Worker

| Parametr | Popis | Výchozí hodnota |
|-----------|--------|----------------|
| `dochub.storage.user` | Cesta, kde jsou uloženy vygenerované PDF, e-knihy a texty pro konkrétního uživatele. | `~/.kramerius4/docs/user-out` |
| `dochub.storage.permanent` | Cesta, kde jsou uloženy obecné části PDF a e-knih, které nejsou závislé na konkrétním uživateli. | `~/.kramerius4/docs/permanent` |
| `dochub.user.max.size.gb` | Maximální povolená velikost uživatelského úložiště v GB. Po překročení limitu jsou všechny soubory odstraněny. | – |
| `dochub.permanent.max.size.gb` | Maximální povolená velikost permanentního úložiště v GB. Po překročení limitu jsou všechny soubory odstraněny. | – |
| `dochub.permanent.expiration.hours` | Odstraní všechny dokumenty v permanentním úložišti starší než zadaný počet hodin. | `3000` |
| `dochub.user.expiration.hours` | Odstraní všechny dokumenty v uživatelském úložišti starší než zadaný počet hodin. | `100` |


| Parametr | Popis | Výchozí hodnota |
|-----------|--------|----------------|
| `api.client.point` | URL adresa API klienta používaná pro komunikaci se službou vyhledávání. | `<server>/search/api/client/v7.0` |
| `administrator.email` | E-mailová adresa administrátora systému. Používá se jako kontaktní adresa v notifikacích a chybových hlášeních. | – |
| `generate.pdf.subject` | Předmět e-mailu zasílaného po vygenerování dokumentu ke stažení. | – |
| `generate.pdf.text` | Text e-mailové notifikace zasílané po vygenerování dokumentu. Lze použít proměnnou `$link$`, která bude nahrazena odkazem ke stažení dokumentu. | `Download notification, download is accessible here $link$` |


## Parametry mail.properties

| Parametr | Popis | Výchozí hodnota |
|-----------|--------|----------------|
| `mail.from.user` | E-mailová adresa odesílatele, která bude uvedena v poli **From** u odesílaných zpráv. | – |
| `mail.smtp.user` | Uživatelské jméno používané pro autentizaci vůči SMTP serveru. Obvykle se jedná o e-mailovou adresu. | – |
| `mail.smtp.host` | Název nebo IP adresa SMTP serveru používaného pro odesílání e-mailů. | – |
| `mail.smtp.startttls.enable` | Povolení protokolu STARTTLS pro zabezpečení komunikace se SMTP serverem. Hodnoty: `true` nebo `false`. | – |
| `mail.smtp.port` | Port SMTP serveru. Například `25`, `465` nebo `587`. | – |
| `mail.smtp.auth` | Určuje, zda je pro připojení k SMTP serveru vyžadována autentizace. Hodnoty: `true` nebo `false`. | – |
| `mail.smtp.socketFactory.port` | Port používaný SSL socket factory. Obvykle odpovídá hodnotě `mail.smtp.port`. | – |
| `mail.smtp.socketFactory.class` | Implementace socket factory používaná pro SSL/TLS spojení. | `javax.net.ssl.SSLSocketFactory` |