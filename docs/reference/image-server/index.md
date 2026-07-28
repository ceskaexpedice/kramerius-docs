# Image Server

## Přehled

Kramerius používá externí image server pro poskytování obrazových dat digitalizovaných dokumentů.

Image server poskytuje:

- stránkové skeny
- dlaždice (tiles)
- zmenšeniny
- transformace obrazu
- zoom
- výřezy obrazu

Komunikace je založena na standardu IIIF Image API.

---

## IIIF Image API

Kramerius používá principy standardu IIIF Image API.

Viz:
- [https://iiif.io/get-started/image-servers/](https://iiif.io/get-started/image-servers/)

IIIF server umožňuje dynamické generování:

- výřezů obrazu
- různých velikostí
- rotací
- různých formátů

bez nutnosti ukládání všech variant obrazu.

---

## Role image serveru

Image server není součástí Krameria.

Kramerius funguje jako:

- klient IIIF serveru
- proxy vrstva
- access-control vrstva

Samotné generování obrazových dat provádí externí image server.

---

## Vazba na digitální objekty

Každý obrazový objekt může obsahovat vazbu na image server endpoint.

Endpoint je získáván z repository vrstvy:

- Akubra repository
- metadata objektu

Pokud objekt image endpoint nemá, nelze obrazová data získat.

---

## Získání IIIF endpointu

Kramerius získává URL image serveru z repository vrstvy (Akubra repository).

Informace o image endpointu je uložena v:

- Fedora RELS-EXT streamu
- atributu `tiles-url`

pro konkrétní obrazový objekt.

Backend:

1. načte `tiles-url` z RELS-EXT
2. ověří jeho dostupnost
3. transformuje starší image endpointy na IIIF endpoint

---

## Transformace legacy endpointů

Kramerius podporuje migraci starších image server formátů.

Pokud repository obsahuje URL založené na:

- Zoomify
- DeepZoom

backend automaticky transformuje endpoint na IIIF variantu.

Například:

| Původní endpoint | Výsledný endpoint |
|---|---|
| zoomify | iiif |
| deepZoom | iiif |

Tím je možné používat jednotný IIIF model i nad staršími repository daty.

---

## Chybějící endpoint

Pokud repository:

- neobsahuje `tiles-url`
- nebo obsahuje placeholder hodnotu

Kramerius považuje objekt za nepřipojený k image serveru.

V takovém případě nelze obrazová data poskytovat.

## IIIF URL model

Kramerius skládá IIIF request ve formátu:

{region}/{size}/{rotation}/{quality}.{format}

Typické parametry:

| Parametr | Význam |
|---|---|
| region | výřez obrazu |
| size | cílová velikost |
| rotation | rotace |
| quality | kvalita obrazu |
| format | výstupní formát |

---

## Typický request

Příklad logické struktury requestu:

region/size/rotation/default.jpg

Například:

- full/full/0/default.jpg
- pct:10,10,80,80/512,/0/color.jpg

---

## Podporované operace

Image server typicky podporuje:

- full image rendering
- tiled access
- region crop
- scaling
- rotation
- změnu kvality
- různé výstupní formáty

---

## MIME type handling

Kramerius mapuje formát requestu na MIME type.

Například:

| Formát | MIME type |
|---|---|
| jpg | image/jpeg |
| png | image/png |
| tif | image/tiff |

MIME type může být odvozena:

- z formátu
- z quality parametru

---

## Proxy režim

Kramerius funguje jako streaming proxy mezi klientem a image serverem.

Flow:

1. klient zavolá Kramerius endpoint
2. Kramerius vytvoří IIIF URL
3. request je přesměrován na image server
4. response stream je předán klientovi

---

## Streaming response

Obrazová data nejsou ukládána do paměti jako celek.

Kramerius používá streaming:

- InputStream z image serveru
- přímé kopírování do HTTP response

Tento přístup:

- snižuje memory usage
- umožňuje práci s velkými obrazy
- podporuje tiled rendering

---

## HTTP hlavičky

Kramerius přebírá vybrané HTTP hlavičky z image serveru.

Typicky:

- Cache-Control
- Last-Modified

Tím je zachováno:

- cache chování
- HTTP validace
- browser caching

---

## Error handling

Pokud objekt nemá image server endpoint:

- request selže
- backend vrací chybu

Kramerius také zachytává:

- connection reset
- broken pipe
- network chyby image serveru

---

## Bezpečnostní model

Image server může být:

- interní infrastruktura
- oddělená služba
- externí systém

Kramerius může fungovat jako access-control vrstva nad IIIF serverem.

Klient tedy nemusí komunikovat přímo s image serverem.

---

## Vztah ke storage vrstvě

Image server pracuje nad uloženými obrazovými daty.

Typicky:

Storage
↓
Image Server
↓
Kramerius
↓
UI klient

---

## Vztah k UI

Reader UI používá image server pro:

- zobrazení stránek
- zoom
- tiled rendering
- deep zoom navigaci

---

## Architektonický model

Zjednodušený model:

Digital Object
↓
Repository metadata
↓
IIIF endpoint
↓
Image Server
↓
Kramerius proxy
↓
Frontend viewer

---

## Shrnutí

Kramerius používá externí IIIF image server pro poskytování obrazových dat digitalizovaných dokumentů.

Backend funguje jako:

- IIIF klient
- streaming proxy
- access-control vrstva

a umožňuje efektivní práci s velkými obrazovými daty.

## Navazujici dokumentace

- ➡️ [Zakladni pojmy](../../core-concepts/index.md)
- ➡️ [Architektura](../../architecture/index.md)
- ➡️ [Konfigurace](../../configuration/iiif/index.md)
- ➡️ [Verzovani](../../versioning/index.md)
