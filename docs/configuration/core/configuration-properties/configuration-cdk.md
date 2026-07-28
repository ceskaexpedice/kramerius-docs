[Úvod](../../../index.md) > [Konfigurace](../../index.md)  / [Core](../index.md) / [Configuration properties](index.md)

# CDK konfigurace

Tato stránka poskytuje **referenční přehled konfiguračních parametrů CDK**. Obsahuje defaultní hodnoty, účel a doporučené nastavení.

Konfigurace se načítá z:

- **Default**: uvnitř JAR souboru knihovny `configuration.properties`
- **Uživatelské přetížení**: soubor `$USER_HOME/.kramerius4/configuration.properties`

Uživatel může ve svém souboru předefinovat libovolnou hodnotu z defaultního souboru.

---

| Parametr | Popis | Výchozí hodnota |
|-----------|--------|----------------|
| `cdk.server.mode` | Přepíná aplikaci do serverového režimu. | `true` |
| `cdk.secured.channel` | Pokud je nastaveno na `true`, komunikace mezi komponentami využívá zabezpečený kanál. | `false` |
| `cdk.secured.apikey` | Pokud je nastaveno na `true`, pro komunikaci je vyžadován API klíč. | `true` |
| `cdk.collections.sources.inovatika.baseurl` | Základní URL adresa služby Inovatika, ze které jsou získávána data o kolekcích. | `https://k7.inovatika.dev/search` |
| `cdk.collections.sources.inovatika.api` | Verze API používaná pro komunikaci se službou Inovatika. | `v7` |
| `cdk.collections.sources.inovatika.apikey` | API klíč používaný pro autentizaci vůči službě Inovatika. | – |
| `cdk.collections.sources.inovatika.forwardurl` | URL adresa používaná pro přesměrování nebo předávání požadavků službě Inovatika. | `https://k7.inovatika.dev/search` |
| `cdk.collections.sources.inovatika.licenses` | Pokud je nastaveno na `true`, načítají se také informace o licencích kolekcí. | `true` |

A v domovském adresáři ~/.kramerius4 mít vytvořený soubor, který reprezentuje API klíč pro komunikaci s ČDK - cdk.api.key. Pokud má jádro povolenou konfigurační proměnnou a daný soubor na cestě nenajde, vytvoří si ho.